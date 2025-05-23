import os
from google import genai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog
import datetime
import pypandoc
from pathlib import Path

# --- Configuration ---
MODEL_NAME = "gemini-2.5-flash-preview-05-20"  # Updated to use the newer model

# --- Helper Functions ---

def configure_gemini():
    """Loads API key and configures the Gemini client."""
    print("--- Step: Configuring Gemini Client ---")
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("🛑 ERROR: GOOGLE_API_KEY not found in .env file or environment variables.")
        print("Please create a .env file in the script's directory with your API key:")
        print("GOOGLE_API_KEY=\"YOUR_API_KEY_HERE\"")
        return None
    
    try:
        client = genai.Client(api_key=api_key)
        print("✅ Gemini client configured successfully.")
        return client
    except Exception as e:
        print(f"🛑 ERROR: Could not configure Gemini client: {e}")
        return None

def select_audio_file():
    """Opens a dialog to select an audio file."""
    print("\n--- Step: Selecting Input Audio File ---")
    root = tk.Tk()
    root.withdraw() # Hide the main tkinter window
    
    # Bring the dialog to the front
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    audio_path = filedialog.askopenfilename(
        title="Select an audio file for processing",
        filetypes=(
            ("Audio Files", "*.mp3 *.wav *.aac *.ogg *.flac *.aiff *.m4a *.mp4"),
            ("MP3 Files", "*.mp3"),
            ("WAV Files", "*.wav"),
            ("AAC Files", "*.aac"),
            ("M4A Files", "*.m4a"),
            ("MP4 Files", "*.mp4"),
            ("FLAC Files", "*.flac"),
            ("OGG Files", "*.ogg"),
            ("AIFF Files", "*.aiff"),
            ("All files", "*.*")
        )
    )
    
    root.destroy()  # Properly destroy the root window
    
    if audio_path:
        print(f"✅ Audio file selected: {audio_path}")
    else:
        print("⚠️ No audio file selected. Exiting.")
    return audio_path

def select_output_directory():
    """Opens a dialog to select an output directory."""
    print("\n--- Step: Selecting Output Directory ---")
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory(title="Select a directory to save results")
    if output_dir:
        print(f"✅ Output directory selected: {output_dir}")
        Path(output_dir).mkdir(parents=True, exist_ok=True) # Ensure directory exists
    else:
        print("⚠️ No output directory selected. Results will be saved in the script's directory.")
        output_dir = "." # Default to current directory
    return output_dir

def upload_file_to_gemini(client, file_path):
    """Uploads a file to Gemini and returns the file object."""
    print(f"\n--- Step: Uploading '{Path(file_path).name}' to Gemini ---")
    try:
        # Upload file using the correct SDK method as per Google documentation
        uploaded_file = client.files.upload(file=file_path)
        print(f"✅ File '{uploaded_file.name}' uploaded successfully. URI: {uploaded_file.uri}")
        return uploaded_file
    except Exception as e:
        print(f"🛑 ERROR: Failed to upload file to Gemini: {e}")
        return None

def call_gemini_api(client, contents):
    """Calls the Gemini API with the given contents and returns the text response."""
    print(f"⏳ Calling Gemini API with model '{MODEL_NAME}'...")
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents
        )
        print("✅ Gemini API call successful. Response received.")
        return response.text
    except Exception as e:
        print(f"🛑 ERROR: Gemini API call failed: {e}")
        return f"Error during API call: {e}"

def save_to_file(content, filepath):
    """Saves content to a specified filepath."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"💾 Content saved to: {filepath}")
    except Exception as e:
        print(f"🛑 ERROR: Could not save file {filepath}: {e}")

def convert_md_to_docx(md_filepath, docx_filepath):
    """Converts a Markdown file to a DOCX file using Pandoc."""
    print(f"\n--- Step: Converting Markdown to DOCX ---")
    print(f"⏳ Converting '{md_filepath}' to '{docx_filepath}'...")
    try:
        pypandoc.convert_file(md_filepath, 'docx', outputfile=docx_filepath)
        print(f"✅ DOCX file created successfully: {docx_filepath}")
    except FileNotFoundError:
        print("🛑 ERROR: Pandoc not found. Please ensure Pandoc is installed and in your system's PATH.")
        print("Visit: https://pandoc.org/installing.html")
    except Exception as e:
        print(f"🛑 ERROR: Failed to convert Markdown to DOCX: {e}")

# --- Main Processing Logic ---
def main():
    print("🚀 Starting Audio Processing Product - Simple Implementation 🚀")

    gemini_client = configure_gemini()
    if not gemini_client:
        return

    audio_file_path = select_audio_file()
    if not audio_file_path:
        return

    output_dir = select_output_directory()
    
    base_filename = Path(audio_file_path).stem
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. Upload audio file to Gemini
    gemini_audio_file = upload_file_to_gemini(gemini_client, audio_file_path)
    if not gemini_audio_file:
        print("🛑 Halting process due to file upload failure.")
        return

    results = {} # To store results of each step

    # --- Agent Transcriber ---
    print("\n--- Agent: Transcriber ---")
    transcription_prompt = (
        "You are an expert transcriber. Your task is to provide a highly accurate and verbatim "
        "transcript of the entire audio provided. Please ensure all spoken words, including "
        "filler words (e.g., 'um', 'uh'), are captured. If multiple speakers are discernible, "
        "try to label them (e.g., Speaker 1:, Speaker 2:). Focus on accuracy and completeness."
        "\n\nHere is the audio:"
    )
    transcription = call_gemini_api(gemini_client, [transcription_prompt, gemini_audio_file])
    results['transcription'] = transcription
    print("\n📝 Transcription Result:")
    print(transcription)
    transcription_filepath = Path(output_dir) / f"{base_filename}_transcription_{timestamp}.txt"
    save_to_file(transcription, transcription_filepath)

    if "Error" in transcription:
        print("🛑 Halting process due to transcription error.")
        return

    # --- Agent Summarizer ---
    print("\n\n--- Agent: Summarizer ---")
    summarizer_prompt = (
        "You are an expert summarizer. Based on the following meeting transcript, please generate a "
        "concise summary of 1-2 paragraphs. The summary should capture the main topics discussed, "
        "key decisions made (if any), and the overall purpose or outcome of the conversation. "
        "Aim for clarity and brevity while retaining essential information."
        f"\n\nTranscript:\n```\n{transcription}\n```"
        "\n\nYour 1-2 paragraph summary:"
    )
    summary = call_gemini_api(gemini_client, [summarizer_prompt]) # No audio file needed here, just text
    results['summary'] = summary
    print("\n📄 Summary Result:")
    print(summary)
    summary_filepath = Path(output_dir) / f"{base_filename}_summary_{timestamp}.txt"
    save_to_file(summary, summary_filepath)

    # --- Agent Pointer ---
    print("\n\n--- Agent: Pointer (Key Points & Sub-points) ---")
    pointer_prompt = (
        "You are an expert at extracting structured information. From the provided meeting transcript, "
        "identify and list the key discussion points. Organize these into a hierarchical list of main points "
        "and relevant sub-points. This should be more detailed than a general summary and reflect the "
        "structure and flow of the conversation. Use bullet points or numbered lists for clarity."
        f"\n\nTranscript:\n```\n{transcription}\n```"
        "\n\nKey Points and Sub-points:"
    )
    pointers = call_gemini_api(gemini_client, [pointer_prompt])
    results['pointers'] = pointers
    print("\n📌 Pointers Result:")
    print(pointers)
    pointers_filepath = Path(output_dir) / f"{base_filename}_pointers_{timestamp}.txt"
    save_to_file(pointers, pointers_filepath)

    # --- Agent To-Do List ---
    print("\n\n--- Agent: To-Do List Creator ---")
    todolist_prompt = (
        "You are an expert at identifying actionable items. Analyze the following meeting transcript "
        "and extract any tasks, action items, or to-do items mentioned. For each item, "
        "list it clearly. If responsibility is assigned to a specific person or group, note that. "
        "If a deadline is mentioned, include it. If no action items are found, please state "
        "'No action items identified'."
        f"\n\nTranscript:\n```\n{transcription}\n```"
        "\n\nTo-Do List / Action Items:"
    )
    todolist = call_gemini_api(gemini_client, [todolist_prompt])
    results['todolist'] = todolist
    print("\n✅ To-Do List Result:")
    print(todolist)
    todolist_filepath = Path(output_dir) / f"{base_filename}_todolist_{timestamp}.txt"
    save_to_file(todolist, todolist_filepath)

    # --- Agent Pembuat Dokumen (Markdown Creator) ---
    print("\n\n--- Agent: Document Creator (Markdown) ---")
    markdown_content = f"""# Meeting Report: {Path(audio_file_path).name}
Date Processed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📜 Full Transcription

{results.get('transcription', 'Transcription not available.')}

## 📄 Executive Summary (1-2 Paragraphs)

{results.get('summary', 'Summary not available.')}

## 📌 Key Points & Pointers

{results.get('pointers', 'Pointers not available.')}

## ✅ Action Items / To-Do List

{results.get('todolist', 'To-Do list not available.')}
"""
    print("📝 Generated Markdown Content (preview):")
    print(markdown_content[:500] + "\n..." if len(markdown_content) > 500 else markdown_content)
    
    md_filename = f"{base_filename}_full_report_{timestamp}.md"
    md_filepath = Path(output_dir) / md_filename
    save_to_file(markdown_content, md_filepath)

    # --- Export to Word Document ---
    docx_filename = f"{base_filename}_full_report_{timestamp}.docx"
    docx_filepath = Path(output_dir) / docx_filename
    convert_md_to_docx(md_filepath, docx_filepath)
    
    print(f"\n\n🎉🎉🎉 Processing Complete! 🎉🎉🎉")
    print(f"All outputs have been saved in the directory: {Path(output_dir).resolve()}")
    print("Individual step outputs (TXT):")
    print(f"  - Transcription: {transcription_filepath.resolve()}")
    print(f"  - Summary:       {summary_filepath.resolve()}")
    print(f"  - Pointers:      {pointers_filepath.resolve()}")
    print(f"  - To-Do List:    {todolist_filepath.resolve()}")
    print("Combined report outputs:")
    print(f"  - Markdown:      {md_filepath.resolve()}")
    print(f"  - Word Document: {docx_filepath.resolve() if Path(docx_filepath).exists() else 'Word conversion failed or skipped.'}")

    # Clean up the uploaded file from Gemini (optional, but good practice)
    # This part of the API might change, or might not be strictly necessary
    # as files might have an auto-expiration. For now, let's assume we don't need explicit deletion
    # or the SDK handles it. If you find files accumulating, you might need to use client.files.delete(name=gemini_audio_file.name)
    # print(f"\n--- Step: Deleting temporary file '{gemini_audio_file.name}' from Gemini ---")
    # try:
    # genai.delete_file(name=gemini_audio_file.name) # This is the new way
    # print(f"✅ Temporary file '{gemini_audio_file.name}' deleted from Gemini.")
    # except Exception as e:
    # print(f"⚠️ Warning: Could not delete temporary file from Gemini: {e}")


if __name__ == "__main__":
    main()
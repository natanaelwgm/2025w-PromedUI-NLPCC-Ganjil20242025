# 🎙️ Meeting Transcriber & Analyzer

An intelligent audio processing tool that transcribes meeting recordings and generates comprehensive reports using Google's Gemini AI. Transform your audio files into structured documents with transcriptions, summaries, key points, and action items.

## ✨ Features

- **🎵 Multi-format Audio Support**: M4A, MP3, WAV, AAC, FLAC, OGG, AIFF, MP4
- **🤖 AI-Powered Analysis**: Uses Google Gemini 2.5 Flash for intelligent processing
- **📝 Complete Transcription**: Verbatim transcripts with speaker identification
- **📊 Smart Summarization**: Concise 1-2 paragraph meeting summaries
- **🎯 Key Points Extraction**: Hierarchical bullet points of main topics
- **✅ Action Items Detection**: Automatic extraction of tasks and deadlines
- **📄 Multiple Export Formats**: Markdown (.md) and Word (.docx) documents
- **🖥️ User-Friendly Interface**: Easy file selection with GUI dialogs
- **⚡ Batch Processing**: Process entire meetings in one go

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API Key (Gemini API access)
- Pandoc (for Word document conversion)

### Installation

1. **Clone or Download** this repository
2. **Navigate** to the class6 directory:
   ```bash
   cd class6
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Pandoc** (for Word document export):
   - **macOS**: `brew install pandoc`
   - **Windows**: Download from [pandoc.org](https://pandoc.org/installing.html)
   - **Linux**: `sudo apt-get install pandoc` or `sudo dnf install pandoc`

### Setup

1. **Get a Google Gemini API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Copy the key

2. **Create environment file**:
   ```bash
   # Create .env file in the class6 directory
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```
   
   Or manually create a `.env` file with:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### Usage

1. **Run the application**:
   ```bash
   python meeting_transcriber.py
   ```

2. **Follow the prompts**:
   - Select your audio file when the dialog opens
   - Choose an output directory for results
   - Wait for processing to complete

3. **View your results**:
   - Individual text files for each analysis step
   - Combined Markdown report
   - Word document (if Pandoc is installed)

## 📁 Output Files

The tool generates several files with timestamps:

```
your_audio_file_transcription_20240521_143052.txt
your_audio_file_summary_20240521_143052.txt
your_audio_file_pointers_20240521_143052.txt
your_audio_file_todolist_20240521_143052.txt
your_audio_file_full_report_20240521_143052.md
your_audio_file_full_report_20240521_143052.docx
```

## 🎯 Supported Audio Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| MP3    | .mp3      | MPEG Audio Layer 3 |
| M4A    | .m4a      | MPEG-4 Audio |
| MP4    | .mp4      | MPEG-4 (audio track) |
| WAV    | .wav      | Waveform Audio |
| AAC    | .aac      | Advanced Audio Coding |
| FLAC   | .flac     | Free Lossless Audio Codec |
| OGG    | .ogg      | Ogg Vorbis |
| AIFF   | .aiff     | Audio Interchange File Format |

## ⚙️ Configuration

### Model Settings
The tool uses `gemini-2.5-flash-preview-05-20` by default. You can modify this in the script:

```python
MODEL_NAME = "gemini-2.5-flash-preview-05-20"
```

### File Size Limits
- **Maximum file size**: 20MB for inline upload
- **Maximum audio length**: 9.5 hours per request
- **Token usage**: ~32 tokens per second of audio

## 🛠️ Troubleshooting

### Common Issues

**1. "GOOGLE_API_KEY not found" Error**
```bash
# Solution: Create .env file with your API key
echo "GOOGLE_API_KEY=your_key_here" > .env
```

**2. "Pandoc not found" Error**
```bash
# macOS
brew install pandoc

# Windows - Download from pandoc.org
# Linux (Ubuntu/Debian)
sudo apt-get install pandoc
```

**3. File Dialog Not Appearing**
- Make sure you're running in a GUI environment
- On remote servers, use X11 forwarding or run locally

**4. Upload Errors**
- Check your internet connection
- Verify API key is valid
- Ensure file size is under 20MB

**5. Audio Format Not Supported**
- Convert your audio to a supported format using tools like FFmpeg:
```bash
ffmpeg -i input.wav output.mp3
```

### Debug Mode

For detailed error information, check the console output. The tool provides step-by-step progress indicators:

```
🚀 Starting Audio Processing Product - Simple Implementation 🚀
--- Step: Configuring Gemini Client ---
✅ Gemini client configured successfully.
--- Step: Selecting Input Audio File ---
✅ Audio file selected: /path/to/your/audio.m4a
```

## 📋 Dependencies

The tool requires these Python packages (automatically installed with `pip install -r requirements.txt`):

- `google-genai` - Google Gemini API client
- `python-dotenv` - Environment variable management
- `tkinter` - GUI file dialogs (usually included with Python)
- `pypandoc` - Markdown to Word conversion
- `pathlib` - Path handling (included with Python 3.4+)

## 🔒 Privacy & Security

- **API Keys**: Store securely in `.env` files (never commit to version control)
- **Audio Files**: Temporarily uploaded to Google's servers for processing
- **Data Retention**: Check Google's data retention policies for Gemini API
- **Local Storage**: All outputs are saved locally on your machine

## 📈 Performance Tips

1. **File Size**: Keep audio files under 20MB for best performance
2. **Format**: MP3 and M4A typically process faster than uncompressed formats
3. **Internet**: Ensure stable internet connection for upload/processing
4. **Hardware**: Processing time depends on file length, not local hardware

## 🎨 Customization

### Modify Prompts
You can customize the AI prompts in the script to change output style:

```python
# Example: More formal summarization
summarizer_prompt = (
    "Generate a formal executive summary in business language..."
)
```

### Change Output Format
Modify the Markdown template to match your organization's format:

```python
markdown_content = f"""# Custom Meeting Report
Organization: Your Company Name
Meeting Type: {meeting_type}
...
"""
```

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

## 📄 License

This project is open source. Check the main repository for license details.

## 🆘 Support

If you encounter issues:

1. Check this README's troubleshooting section
2. Verify your setup follows the installation steps
3. Check the console output for specific error messages
4. Ensure your API key has proper permissions

---

**Happy Transcribing!** 🎉

*Transform your meetings into actionable insights with AI-powered analysis.* 
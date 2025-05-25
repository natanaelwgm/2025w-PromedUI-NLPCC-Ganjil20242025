---
layout: default
title: Class 5 & 6 - Combined Assignment
---

# Class 5 & 6 Combined Assignment: Programmatic LLM Applications

Welcome to your combined assignment for Week 5 and Week 6! This assignment is designed to give you hands-on experience with leveraging Large Language Models (LLMs) programmatically for various tasks. You will demonstrate your ability to interact with LLM APIs like OpenAI and Gemini to build simple applications and process data.

**This assignment counts as TWO separate grades: one for Week 5 and one for Week 6.** For example, if you score 85 out of 100 on this combined assignment, you will receive a grade of 85 for Week 5 and a grade of 85 for Week 6.

**API Keys:**
*   You are expected to use the **OpenAI API key** provided in the WhatsApp group for OpenAI models.
*   If you wish to use **Google Gemini API**, please ask the lecturers for guidance on obtaining/using a key.
*   Remember to handle your API keys securely (e.g., using Colab Secrets, environment variables). **Do NOT hardcode keys directly in your notebook.** Refer to `class4-assignment.md` for best practices.

---

## Core Objectives

*   Demonstrate programmatic interaction with LLM APIs (OpenAI, Gemini).
*   Build a basic chat application using an LLM.
*   Apply LLM capabilities to process and derive insights from tabular data.
*   Optionally, explore and implement advanced LLM features like multimodality, agentic behavior, retrieval, or tool use.

---

## Core Tasks (Total 100 points for Week 5 & Week 6 each)

You are required to complete the following two tasks. All work should be done in one single Python notebook (`.ipynb`) and submitted to your GitHub repository.

### Task 1: Simple LLM Chat Application (Vanilla Chat) (35 points)

**Objective:** Create a basic command-line or simple interactive chat application that uses an LLM to respond to user inputs.

**Requirements:**
1.  **Programmatic LLM Interaction:**
    *   Write Python code to send user input to an LLM API (e.g., OpenAI's `gpt-3.5-turbo`, `gpt-4o`, or a Gemini model).
    *   Receive and display the LLM's response.
2.  **User Interface:**
    *   The application should allow a user to type in a message.
    *   It should then display the LLM's generated response.
    *   This can be a simple loop in a command-line interface.
3.  **Functionality:**
    *   Your chat application can be single-turn (processes one message at a time without memory of previous messages) or multi-turn (maintains a conversation history to provide context for subsequent responses). Multi-turn is encouraged for a richer interaction.
    *   Refer to `nlpcc_2025_week5_livecoding.ipynb` for examples of single-turn and multi-turn chat.

**Deliverables:**
*   A Python notebook (`.ipynb` file, e.g., `week5_6_task1_chat.ipynb`) containing:
    *   Your Python code for the chat application.
    *   Clear comments explaining your code.
    *   A brief markdown section describing how to run your chat application and any notable features or choices you made (e.g., which model used, if it's multi-turn).
    *   Example interactions (screenshots or text logs) showing your chat application working.

---

### Task 2: LLM-Powered Tabular Data Processing (65 points)

**Objective:** Apply an LLM to programmatically process multiple rows of data from a tabular source (e.g., Excel, CSV), similar to the "asking the same question to N rows" concept shown in `nlpcc_2025_week5_livecoding.ipynb`.

**Requirements:**
1.  **Dataset Selection:**
    *   Choose a tabular dataset. You can:
        *   Find a suitable dataset on [Kaggle](https://www.kaggle.com/datasets) (e.g., product reviews, news headlines, movie synopses, customer support tickets).
        *   Create your own synthetic dataset (e.g., a list of fictional product descriptions, social media posts).
    *   The dataset should have at least one text column that you will process with the LLM, and potentially other columns you can use to formulate your prompts.
2.  **Data Loading & Iteration:**
    *   Programmatically load your chosen dataset (e.g., using `pandas`).
    *   Iterate through the rows of your dataset (or a significant sample of at least 10-20 rows if the dataset is very large).
3.  **LLM Prompting per Row:**
    *   For each selected row:
        *   Formulate a specific question or prompt for the LLM. This prompt should ideally incorporate data from one or more columns of the current row.
        *   Send this prompt to an LLM API.
        *   **Example Tasks:**
            *   Summarize a text column (e.g., summarize product reviews).
            *   Perform sentiment analysis on a text column.
            *   Categorize items based on their descriptions.
            *   Extract specific information (e.g., key features from product descriptions).
            *   Generate a short creative text based on row data (e.g., a tweet, a tagline).
            *   Translate text from one language to another.
4.  **Response Handling:**
    *   Receive the LLM's response for each row.
    *   Store these responses, for example, in a new column in your DataFrame or a separate list.
    *   Present the original data and the LLM-generated responses clearly.

**Deliverables:**
*   A Python notebook (`.ipynb` file, e.g., `week5_6_task2_tabular.ipynb`) containing:
    *   Your Python code for loading data, iterating, prompting the LLM, and handling responses.
    *   Clear comments explaining your code.
    *   Information about your chosen dataset (e.g., link to Kaggle, or description if synthetic) and why you chose it.
    *   The specific task you asked the LLM to perform on each row and the structure of your prompts.
    *   A display (e.g., pandas DataFrame output) showing some of the original rows alongside their corresponding LLM-generated results.

---

## Bonus Task: Advanced LLM Feature Integration (Up to +50% on your total score for this combined assignment)

**Objective:** Enhance **either Task 1 or Task 2** by integrating at least one advanced LLM capability. This is your chance to explore the cutting edge!

**Choose ONE (+1) of the following advanced features to implement:**

1.  **Multimodal Interaction:**
    *   **For Task 1 (Chat):**
        *   Allow the user to input an image along with their text query, and have the LLM process both (e.g., "What is in this image?").
        *   Have the LLM generate an image as part of its response (e.g., using DALL-E via API if accessible, or describing an image if direct generation is complex).
        *   Integrate voice input (text-to-speech for input) and/or voice output (speech-to-text for LLM response).
    *   **For Task 2 (Tabular Data):**
        *   If your tabular data includes links to images (e.g., product images), send the image (or image URL) along with text data from the row to a multimodal LLM for processing (e.g., "Describe this product based on its image and description text.").

2.  **Agentic Behavior / Tool Use / Function Calling:**
    *   **For Task 1 (Chat):**
        *   Develop a chatbot that can use one or more simple "tools" (functions you define). For example, a tool to:
            *   Get the current date/time.
            *   Perform a basic calculation.
            *   Look up information in a small, predefined local dataset.
        *   The LLM should decide when to call a tool based on the user's query, and then use the tool's output to formulate its final response. (Refer to OpenAI's Function Calling or Gemini's Tool Use documentation).
    *   **For Task 2 (Tabular Data):**
        *   When processing a row, the LLM could call a function to:
            *   Fetch additional related information from an external source (e.g., a simple API, another local file) before generating its main response.
            *   Validate or reformat its own generated output against certain criteria using a defined function.

3.  **Retrieval Augmented Generation (RAG):**
    *   **For Task 1 (Chat):**
        *   Create a chatbot that can answer questions based on a specific document or a small collection of documents you provide.
        *   This involves:
            *   Storing your document(s) in a way that can be searched (e.g., simple text file, or basic vector embeddings if you're ambitious).
            *   When the user asks a question, retrieve relevant snippets from your document(s).
            *   Provide these snippets as context to the LLM along with the user's question to generate an answer.
    *   **For Task 2 (Tabular Data):**
        *   For each row being processed, retrieve relevant information from an external knowledge base (e.g., a text file containing domain-specific information, or a more advanced vector store).
        *   Use this retrieved information as additional context for the LLM when generating its response for that row, leading to more informed or detailed outputs.

**Requirements for the Bonus Task:**
*   Clearly state which advanced feature you chose and why.
*   Explain how you integrated it into your chosen Core Task (Task 1 or Task 2).
*   Provide code and a demonstration of the advanced feature in action.
*   Discuss any challenges faced and how you addressed them.

**Deliverables for the Bonus Task:**
*   Update the relevant notebook (from Task 1 or Task 2) to include the bonus implementation.
*   Ensure there's a dedicated markdown section in the notebook clearly explaining and demonstrating the bonus feature.

---

## Technical Requirements

*   **Language & Environment:** All code must be in Python, preferably within Google Colab notebooks (`.ipynb`).
*   **LLM APIs:** Use the OpenAI API (with the class-provided key) or Google's Gemini API.
*   **API Key Security:** Demonstrate secure API key management (e.g., Colab secrets, environment variables). **Do not hardcode API keys in your code cells.**
*   **Code Quality:** Write clear, well-commented, and organized code.
*   **Documentation:** Use markdown cells in your notebooks to explain your approach, steps, and findings.

---

## Submission Guidelines

1.  **Repository:** Push all your `.ipynb` notebook(s) for this combined assignment to your personal `nlpcc-ui-2025` GitHub repository.
    *   Suggested naming:
        *   `week5_6_task1_chat.ipynb`
        *   `week5_6_task2_tabular.ipynb`
        *   (If you do the bonus, integrate it into one of these files and make sure it's clearly marked).
2.  **Deadline:** **Friday, June 27th, 2025, at 23:55 PM Jakarta Time (WIB).**
3.  **Notification Email:**
    *   Send an email to **both** `natanael.waraney@ui.ac.id` and `natanaelmassie2009@gmail.com`.
    *   Subject line: `[NLPCC-UI 2025] Week 5-6 Assignment - Your Name - Student Number`.
    *   The email body **must** contain a direct link to your `nlpcc-ui-2025` GitHub repository. If possible, also link directly to the specific notebook(s) for this assignment within your repository.
    *   If you are aiming for the public sharing bonus, include a direct link to your public post in the same email.
4.  **Important:** Submissions will only be graded if the notification email is received by the deadline and the work is accessible in your GitHub repository.

---

## Grading Rubric

This combined assignment is worth a total of 100 base points, which will be recorded as your grade for **both Week 5 and Week 6**. The Bonus Task can add up to 50 additional points.

| Criteria                                  | Max Score | Excellent (Full Points)                                                                                                                                                       | Good (Partial Points)                                                                                                                                                       | Needs Improvement (Low/No Points)                                                                                                |
| :---------------------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Task 1: Simple LLM Chat (35 pts)**      |           |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |
| 1.1 Programmatic API Interaction          | 15        | Correctly and efficiently uses LLM API (OpenAI/Gemini) for chat. Handles API calls robustly. Model choice is appropriate and well-justified.                                  | Mostly correct API usage, minor inefficiencies or error handling gaps. Model choice acceptable.                                                                               | Significant errors in API usage, frequent failures, or inappropriate model choice. Little to no API interaction.                 |
| 1.2 User Input/Output Handling            | 10        | Clear and intuitive user interaction. LLM responses are well-formatted and displayed. Multi-turn history (if implemented) is managed effectively and enhances conversation.       | User interaction is functional but could be clearer. Response display is adequate. Basic multi-turn (if attempted) has minor issues or doesn't significantly add value.       | User interaction is confusing or buggy. Responses poorly displayed. Single-turn only or flawed/non-functional multi-turn.        |
| 1.3 Code Clarity & Doc (Task 1)           | 10        | Code is exceptionally clear, well-commented, and organized. Notebook includes excellent markdown explanations, clear demonstration of functionality, and thoughtful choices.     | Code is mostly clear and functional. Documentation and notebook organization are good. Demonstration is adequate.                                                             | Code is unclear, poorly organized, or lacks comments. Notebook documentation or demonstration is minimal/missing.                |
| **Task 2: LLM for Tabular Data (60 pts)** |           |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |
| 2.1 Dataset & Loading                     | 10        | Excellent choice/creation of a relevant tabular dataset. Data is loaded correctly and efficiently. Clear and insightful justification for dataset choice.                       | Suitable dataset chosen/created and loaded. Justification is adequate. Minor issues in loading or data handling.                                                              | Dataset is inappropriate, poorly chosen/created, or loading fails. Justification weak/missing.                                   |
| 2.2 Programmatic Iteration & Prompting    | 25        | Efficiently iterates through rows. Prompts are creatively and effectively designed, skillfully using row data to ask meaningful and complex questions/tasks of the LLM.         | Iteration works. Prompts are functional and use row data, but could be more refined, creative, or complex.                                                                  | Inefficient or incorrect iteration. Prompts are poorly formulated, don't use row data well, are trivial, or applied inconsistently. |
| 2.3 LLM Response Integration & Presentation | 15        | LLM responses are correctly parsed/handled and meaningfully integrated (e.g., new DataFrame column). Results are clearly presented, insightful, and well-analyzed.              | LLM responses are handled and stored. Presentation of results is adequate but could be clearer or more insightful. Basic analysis of results.                               | LLM responses are poorly handled, lost, or not integrated. Results are unclear, not presented, or not analyzed.                  |
| 2.4 Code Clarity & Doc (Task 2)           | 10        | Code is exceptionally clear, well-commented, and organized. Notebook includes excellent markdown explanations, clear presentation of results, and discussion of choices.        | Code is mostly clear and functional. Documentation and notebook organization are good. Results are presented.                                                               | Code is unclear, poorly organized, or lacks comments. Notebook documentation or presentation of results is minimal/missing.      |
| **Overall Requirements**                  |           |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |
| 3. API Key Security                       | 5         | API key is managed securely using Colab Secrets or equivalent environment variable method. No hardcoding. Clear explanation of method and its importance.                       | API key is managed (not hardcoded), but method might be less ideal (e.g. input prompt if not Colab) or explanation is brief.                                        | API key is hardcoded in a cell, or no attempt at secure management. No/poor explanation.                                          |
| **Total Base Score**                      | **100**   |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |
| **Bonus: Advanced LLM Feature (+50 pts)** |           |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |
| B.1 Choice & Relevance of Feature         | 10        | Excellent choice of an advanced feature highly relevant to the chosen core task, demonstrating a clear understanding of its potential. Clear justification for the choice.     | Good choice of feature, reasonably relevant. Justification is adequate.                                                                                                     | Feature choice is poor, irrelevant, not clearly justified, or not an advanced feature as described.                                |
| B.2 Implementation Correctness            | 20        | Advanced feature is implemented correctly and effectively, showcasing strong understanding of the underlying API/SDK capabilities. Robust error handling and efficient design. | Feature is mostly implemented correctly, but may have minor bugs or inefficiencies. Good understanding shown. Basic error handling.                                     | Feature implementation is significantly flawed, buggy, incomplete, or does not work. Misunderstanding of capabilities.           |
| B.3 Demonstration of Functionality        | 10        | Clear and compelling demonstration of the advanced feature in action. Shows tangible improvement or new, significant capability for the core task.                            | Feature is demonstrated, but impact or improvement might not be fully clear or significant. Functionality is present.                                                       | Demonstration is unclear, fails, or the feature adds little to no discernible value or functionality.                            |
| B.4 Explanation & Integration Clarity     | 10        | Exceptionally clear explanation of the bonus feature, its integration into the core task, and any challenges faced. Notebook section is well-organized and insightful.         | Good explanation and integration details. Challenges discussed. Notebook section is clear.                                                                                  | Explanation is poor, integration is unclear, or challenges not addressed. Notebook section is messy or difficult to follow.      |
| **Max Possible Score (with Bonus)**       | **150**   |                                                                                                                                                                               |                                                                                                                                                                             |                                                                                                                                  |

*The final score is also subject to the 1.5x public sharing multiplier if applicable, as detailed in `scoring-rubric.md`.*

---

## Encouragement & Resources

*   **Experiment!** This is your chance to play with powerful AI tools. Don't be afraid to try creative prompts or tackle interesting datasets.
*   **Use Gemini!** We encourage you to explore Google's Gemini models if you're interested. Ask the lecturers if you need assistance with API access.
*   **Refer to Class Materials:**
    *   `nlpcc_2025_week5_livecoding.ipynb`: Contains examples relevant to both Task 1 (chat) and Task 2 (iterative prompting for tabular data, structured output).
    *   `nlpcc_2025_week6_livecoding.ipynb`: May contain examples or discussions relevant to the Bonus Task (multimodality, agents, tool use).
    *   Review the concepts from `class5-outline.md` (LLMs, generative AI, API interaction) and `class6-outline.md` (Chatbots, Multi-Modal, Agentic AI, Tool Use).
*   **Ask Questions:** If you're stuck or need clarification, please don't hesitate to ask the lecturers or your TAs.
*   **Ethical Considerations:** As you work with LLMs, briefly consider the ethical implications of your application (e.g., potential biases in generated content, responsible use of AI). While not a formal grading component, it's good practice.

Good luck, and we look forward to seeing your innovative LLM applications!
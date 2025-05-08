---
layout: default
title: Class 3 - Assignment
---

# Class 3 Assignment: Text Classification Challenge & AI Collaboration

Building on our introduction to Text Classification, this assignment challenges you to apply these concepts to a dataset of your choice, train multiple models, and leverage AI tools for data generation and analysis.

This assignment is designed for you to be creative and dive deep into the practical aspects of text classification. The core tasks are defined, but we strongly encourage you to explore unique datasets, experiment with various models, and make extensive use of AI assistants, all within a Google Colab environment.

---

## Task: End-to-End Text Classification Project

Your mission is to find a suitable text dataset, train classification models, generate new test data using an LLM, evaluate your models, and present your findings. **All work should be completed in a Google Colab notebook, which will then be saved to your GitHub repository, similar to the workflow in Week 1 and Week 2.**

Step 1.  **Find Your Text Classification Dataset on Kaggle:**
    * Go to [Kaggle](https://www.kaggle.com/).
    * Search for text classification datasets. You can use search terms like "news classification," "book genre classification," "sentiment analysis dataset," "text categorization," etc.
    * After searching, filter the results by selecting "Datasets."
    * **Crucially, choose a dataset that is primarily text-based** (not images, audio, or purely numerical data) and makes sense for a classification task (i.e., it has clear categories or labels you can predict).
    * **Examples to get you started (feel free to find your own!):**
        * **News Classification:** [AG News Classification Dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
        * **Review/Sentiment Analysis:** [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
        * **Book Genre Classification:** [Best Books 10K - Multi-Genre Data](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)
    * Download the dataset and include a brief justification in your notebook for why you chose it. If it's not a well-known public dataset, please provide a link or instructions on how to access it.

> **Why is exploring Kaggle important?**
> Kaggle is more than just a repository of datasets; it's a vibrant community and learning platform for data science and machine learning. By exploring Kaggle, you:
> *   **Discover Diverse Datasets:** You get exposed to a vast array of real-world and competition datasets, which helps you understand the variety of problems data science can solve.
> *   **Learn from Others:** You can see how other data scientists and practitioners approach similar problems by studying public notebooks (often called "Kernels"). This is a great way to learn new techniques, coding styles, and best practices.
> *   **Understand Data Quality:** You'll encounter datasets of varying quality, which teaches you the importance of data cleaning, preprocessing, and critical evaluation.
> *   **Stay Updated:** Kaggle hosts competitions on cutting-edge problems, helping you stay abreast of the latest trends and techniques in AI and ML.
> *   **Build Your Portfolio:** Successfully working with Kaggle datasets and participating in the community can be a valuable addition to your data science portfolio.

Step 2.  **Train Classification Models:**
    * Using Python and libraries like Scikit-learn within your Colab notebook, train **at least two different classification models** on your chosen dataset.
    * You can use models discussed in class, such as **Naive Bayes** and **Logistic Regression**.
    * **Higher scores (see rubric) will be awarded for thoughtfully implementing and comparing more than two distinct models or for experimenting with more advanced techniques** (e.g., Support Vector Machines, simple Neural Networks, different text vectorization methods like TF-IDF beyond basic CountVectorizer).
    * Document your model training process, including any preprocessing steps (tokenization, normalization, vectorization), hyperparameter choices (if any), and why you chose your models.

Step 3.  **AI-Powered Test Data Generation:**
    * Use a Large Language Model (LLM) like **Google Gemini** or **ChatGPT** to generate **100 new, unique text samples** relevant to the classification task of your chosen dataset.
    * For each generated sample, instruct the LLM to also provide the **correct label** according to the classes in your dataset.
        * *Example:* If your dataset is about book genres, ask the LLM to "Generate 100 short book snippets (2-3 sentences each) and label each with one of the following genres: \[list your dataset's genres]."
    * Carefully review the LLM-generated data for quality and relevance. You may need to refine your prompts to get good results.
    * **Crucially, you MUST provide clear documentation of your interaction with the AI for this specific task.** This includes your prompts, the AI's responses, and any iterative refinement process. This can be in the form of screenshots of your chat history, a shared link to the conversation (if the platform supports it, e.g., ChatGPT's share link feature), or a detailed log in your Colab notebook.
    * Store these 100 generated samples and their labels as your new test set.

> **The Rise of Synthetic Data in AI**
> You've just used an LLM to generate synthetic data, a practice that's becoming increasingly crucial in the AI landscape!
> *   **What is it?** Synthetic data is artificially generated information rather than data collected from real-world events.
> *   **Why is it important?**
>     *   **Augmenting Datasets:** It can help create larger and more diverse datasets, especially when real-world data is scarce, expensive, or has privacy concerns. This is vital for training robust models.
>     *   **Addressing Imbalances:** If your dataset has too few examples of a particular class, synthetic data can help balance it out, leading to fairer and more accurate models.
>     *   **Training New Models:** Interestingly, many cutting-edge AI models, including some LLMs themselves, are trained on massive amounts of data, a portion of which can be synthetically generated to cover a wider range of scenarios or to pre-train models before they are fine-tuned on real-world data.
>     *   **Simulating Rare Events:** It's useful for creating data for scenarios that are rare or dangerous to collect in the real world.
> While powerful, it's also important to be mindful of the quality and potential biases in LLM-generated data, as you've been asked to reflect on in the optional exploration tasks!

Step 4.  **Model Prediction and Evaluation:**
    * Use each of your trained models to predict the labels for the 100 AI-generated text samples.
    * Calculate the **accuracy** (percentage of correctly predicted labels) for each model on this new test set.
    * Present the accuracies in a clear format (e.g., a table).
    * **Plot the accuracies** of your models for a visual comparison (e.g., a bar chart).

Step 5.  **Creativity and Exploration (Encouraged!):**
    * **Be creative!** The more unique your dataset choice and the more insightful your modeling approach, the better.
    * Explore different text preprocessing techniques, feature engineering, or model tuning.
    * Think about the nuances of your chosen dataset and how they might affect model performance.

Step 6.  **Extensive Use of AI Tools (Highly Encouraged!):**
    * Use AI tools (Gemini, ChatGPT, etc.) extensively throughout this assignment:
        * Brainstorming dataset ideas or search terms for Kaggle.
        * Understanding classification algorithms or Scikit-learn functions.
        * Generating Python code snippets for training, evaluation, or plotting.
        * Debugging your code.
        * Drafting explanations or interpretations of your results for your notebook.
        * As mandated, for generating the new test dataset.
    * Documenting your prompts and how AI assisted you is **mandatory for the AI-Powered Test Data Generation step (see point 3 above)**. For other uses of AI in this assignment, documenting your interaction (e.g., prompts used, how AI helped) in your notebook is good practice and welcome, though not mandatory for grading.

Step 7.  **Document in a Google Colab Notebook:**
    * Perform all your work in a single **Google Colab notebook** (`.ipynb` file).
    * Use markdown cells for clear explanations of each step: dataset selection, preprocessing, model training, AI data generation (including prompts **and AI interaction logs/history for this part**), evaluation, and your conclusions.
    * Include all code cells, ensuring their outputs (tables, plots, accuracy scores) are visible in the submitted notebook. (Remember to "Save" your Colab notebook to ensure outputs are stored before downloading or pushing to GitHub).
    * Structure your notebook logically so it tells the story of your project.

Step 8.  **Save and Add to Your GitHub Repo:**
    * Save your completed Google Colab notebook as an `.ipynb` file.
    * Place this `.ipynb` file inside your existing `nlpcc-ui-2025` GitHub repository.
    * Add, commit, and push your notebook to GitHub. Ensure the version on GitHub is the one with all your work and visible outputs.

**Goal:** This assignment aims to give you hands-on experience with the entire text classification pipeline, from data acquisition to model evaluation, while emphasizing creative problem-solving and the strategic use of AI tools as collaborators, all within the Google Colab environment.

---

## Optional: Breadth of Exploration (Up to +20 Extra Points)

To earn extra credit and demonstrate a deeper engagement with the material, expand your project by exploring one or more of the following areas:

* **Additional Models & Techniques:** Implement and compare more than the two required models. Explore different vectorization techniques (e.g., TF-IDF, word embeddings if you're adventurous), or delve into hyperparameter tuning for your models.
* **In-depth Error Analysis:** Manually inspect some of the misclassified samples from your AI-generated test set. Why do you think your models made mistakes on them? Are there patterns in the errors? What could be done to improve performance on these types of samples?
* **Comparison with Original Test Set:** If your Kaggle dataset has a predefined test set, also evaluate your models on it and compare its performance against the AI-generated test set. Discuss any differences and potential reasons.
* **Beyond Accuracy:** Calculate and discuss other evaluation metrics like precision, recall, F1-score (especially if your dataset is imbalanced). A confusion matrix for each model can also be very insightful.
* **Qualitative Analysis of LLM Output:** Briefly discuss the quality, diversity, and potential biases of the text data generated by the LLM (drawing from your documented interactions). How reliable was it? What were the limitations?
* **Reflection on AI Collaboration:** Write a short reflection on your experience using AI tools for this project (beyond just the data generation). What worked well? What were the challenges? How did it change your workflow or understanding?

**Important Clarification:** You only need to implement **one meaningful exploration task** from the list above to be eligible for these bonus points, though more comprehensive exploration is welcome. Clearly label this section in your notebook.

---

## Idea Consultation (Optional but Encouraged!)

If you're stuck on choosing a dataset, selecting models, or prompting an LLM effectively, you are welcome to discuss your ideas with the instructor.

* This is part of the learning process.
* Reach out via email or other designated channels.
* **Consultation Deadline:** Please aim to have these discussions **before Monday, May 12th, 2025, 23:59 WIB**.

---

## Deadline and Submission

* **Deadline:** **Wednesday, May 14th, 2025, at 23:55 PM Jakarta Time (WIB).** (Adjusted due to Waisak national holiday on Monday)
* **Submission Method:** You **must** notify the instructors via email by the deadline.
* **Email Contents:**
    * Send an email to **both** `natanael.waraney@ui.ac.id` and `natanaelmassie2009@gmail.com`.
    * The subject line should be: `[NLPCC-UI 2025] Class 3 Assignment - Your Name - Student Number`.
    * The email body **must** contain a direct link to your `nlpcc-ui-2025` GitHub repository (specifically linking to the Colab notebook `.ipynb` file within the repository is helpful, but linking the repo is mandatory).
    * If you are aiming for the public sharing bonus, also include a direct link to your public post (LinkedIn, blog, etc.) in the same email.
* **Important:** Submissions are graded based on the work pushed to GitHub *and* the notification email being received by the deadline.

---

## Optional: Public Sharing (Bonus Opportunity)

As outlined in the `scoring-rubric.md`, you can earn a **1.5x multiplier** on your final assignment score by sharing your work publicly.

* **How to Share:** Post about your text classification project on platforms like LinkedIn, a personal blog, Medium, GitHub (beyond just the private repo for submission), etc.
* **What Counts:** Create a public post discussing your project. You could explain your dataset, the models you used, your findings on model accuracy, your experience with AI-generated data, or what you learned. **Simply having the public GitHub repo with your code is not sufficient for the bonus; active sharing is key.**
* **Polishing:** Use tools like Gemini to help draft or refine your public post!
* **Notify:** Include the **direct link to your public post** in your submission email.

---

## Evaluation Rubric (How to Get 100% before bonuses)

| Criteria                      | Max Score | Excellent (Full Points)                                                                                                                               | Good (Partial Points)                                                                                                   | Needs Improvement (Low/No Points)                                                                     |
| :---------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **1. Dataset & Preparation** | 20        | Excellent choice of text classification dataset from Kaggle, well-justified. Thorough preprocessing and clear preparation for modeling.             | Suitable dataset chosen, but justification or preprocessing could be clearer/more detailed. Some minor issues present.    | Dataset inappropriate or poorly chosen. Minimal or flawed preprocessing.                              |
| **2. Model Training** | 20        | **Successfully implements and thoughtfully compares more than two distinct classification models (or two models with significant exploration of variations/tuning).** Clear explanation of model choices, training process, and rationale for choices. | At least two distinct models correctly implemented and trained. Explanations are adequate but may lack depth or full clarity on choices. | Fewer than two models, or significant errors in model implementation/training. Poor explanations.     |
| **3. AI Test Data Generation**| 20        | Successfully generated 100 relevant test samples with labels using an LLM. Prompts included, data quality is good, and **AI interaction history for generation is clearly documented.** | Generated 100 samples, but relevance/quality might vary, or prompts/AI interaction documentation is partially incomplete. Some issues with labels. | Failed to generate appropriate test data, data is irrelevant/low quality, or process/AI interaction not documented. |
| **4. Evaluation & Plotting** | 20        | Accurate calculation and clear presentation of model accuracies on AI-generated data. Insightful plotting of results and thoughtful comparison.                             | Accuracies calculated, but presentation, plotting, or comparison could be improved. Minor errors in calculation or interpretation. | Inaccurate or missing evaluation. Plots are unclear, misleading, or absent.                         |
| **5. Notebook & Code Quality**| 10        | Google Colab Notebook is exceptionally well-organized, code is clean, efficient, and well-commented. All outputs are visible and easy to understand.             | Google Colab Notebook is generally well-organized, code is functional. Some areas could be clearer or better documented.        | Notebook is disorganized (or not a Colab notebook as instructed), code is messy or has significant errors. Outputs missing or unclear.      |
| **6. Creativity & AI Use (General)** | 10        | Demonstrates significant creativity in dataset/model choices or analysis. Shows thoughtful and extensive use of AI tools beyond the mandatory data generation part. | Some creativity shown. AI tools used appropriately, but general integration could be deeper or more innovative.                | Little to no creativity. Minimal or ineffective general use of AI tools.                                      |
| **7. Breadth of Exploration** | **+20** | *(Optional Bonus)* Project demonstrates significant breadth by deeply exploring **multiple suggested areas** (e.g., several additional models, detailed error analysis, multiple advanced metrics). Findings are well-explained and add substantial value. | *(Optional Bonus)* Project explores **at least one suggested area** meaningfully. Presentation/explanation is clear.    | No significant breadth of exploration attempted, or exploration is superficial.                                                                       |

**Total:** | **100 (+20)** | The base score is out of 100. Meeting criteria 1-6 thoroughly leads to 100. Excellent Breadth of Exploration (Criteria 7) can add up to 20 bonus points, for a maximum of 120 (before the 1.5x public sharing multiplier). |                                                                                                         |                                                                                                       |

---

Good luck with your text classification projects! Embrace the challenge, be creative, and don't hesitate to lean on AI as your powerful assistant. Remember to conduct your work in Google Colab and submit the `.ipynb` file to your GitHub.
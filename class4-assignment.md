---
layout: default
title: Class 4 - Assignment
---

# Class 4 Assignment: Synthetic Data, Embeddings, and Semantic Analysis

Welcome to the Week 4 assignment! Building on our exploration of semantic representations and embeddings, this assignment will have you dive into the practical application of these powerful NLP techniques. You'll start by creating your own diverse datasets using generative AI, then transform this data into meaningful vector representations (embeddings), and finally, perform insightful analyses on these embeddings.

This assignment is designed to be both challenging and creative. You'll get to choose the topics for your synthetic data, experiment with different embedding models, and select an analysis method that interests you. Pay close attention to the best practices for API key management, as this is a critical skill.

---

## Core Objectives

* **Master Synthetic Data Generation:** Learn to use LLMs (like Gemini via API or AI Studio) to create structured, labeled datasets for various NLP tasks.
* **Understand Text Embeddings:** Gain hands-on experience generating text embeddings using different models/APIs.
* **Apply Embedding Analysis:** Implement at least one common embedding analysis technique (e.g., semantic search, clustering).
* **Develop Best Practices:** Securely manage API keys in your development environment (Google Colab).
* **Document and Present:** Clearly document your process, code, and findings in a well-structured Google Colab notebook and share it via GitHub.

---

## Tasks

This assignment is structured into several key tasks. All work should be completed within a **Google Colab notebook** (`.ipynb`), which will then be saved to your existing `nlpcc-ui-2025` GitHub repository. Ensure your notebook includes markdown cells for explanations and that all code cell outputs are visible.

### Task 1: Synthetic Dataset Creation

Reflecting the process shown in our live coding session (`nlpcc25_livecoding_week4.ipynb`), your first task is to create a synthetic dataset using a Large Language Model (LLM). We encourage using the Gemini API or Google AI Studio, but you are free to use other LLMs as well.

1.  **Choose Your Domain & Context:**
    * Decide on a general theme or domain for your synthetic data. This could be anything that interests you: customer reviews for a fictional product category, short news summaries, tweets on specific topics, mini book chapters, song lyrics, fictional character backstories, etc.
2.  **Define Distinct Topics/Labels:**
    * Within your chosen domain, define **at least five (5) distinct topics or labels**. These will be the categories for your synthetic text.
    * *Example from live coding:* We generated customer reviews for "beauty makeup" and also explored data about "basketball" and "murder" as distinct topics.
3.  **Generate Synthetic Data:**
    * For each of your defined topics/labels, use an LLM to generate a collection of text samples.
    * Aim for a reasonable number of samples per topic (e.g., 20-50 samples per topic, leading to a total of 100-250+ samples). The more data, the better your embedding analysis might be, but focus on quality and distinctiveness.
    * Ensure the generated text is relevant to the label.
    * **Document your prompts:** In your notebook, include the prompts you used to generate the data for each topic.
4.  **Structure Your Dataset:**
    * Organize your generated data, perhaps into a Pandas DataFrame, with columns for the `text` and its corresponding `label`.

### Task 2: Text Embedding Generation

Once you have your synthetic dataset, the next step is to convert your text data into numerical embedding vectors.

1.  **Choose an Embedding Model:**
    * Select an embedding model to use. You can choose from:
        * **API-based models (mandatory):**
            * OpenAI API (use what's shown in class; refer to [openai_embedding_ref.pdf](./openai_embedding_ref.pdf) for details on OpenAI's embedding documentation)
        * **Open-source models (Bonus Opportunity):** Explore using pre-trained models from libraries like Sentence Transformers, or even classical methods like TF-IDF if you want to compare. However, the API based one is mandatory and must be done first.
2.  **Generate Embeddings:**
    * For each text sample in your synthetic dataset, generate its embedding vector using your chosen model.
    * Store these embeddings. You might store them directly in your DataFrame alongside the text and labels, or in a separate structure like a NumPy array.
    * Remember to handle API calls efficiently if you're generating embeddings for many texts (e.g., batching if the API supports it).

### Task 3: Embedding Analysis

With your text data now represented as embeddings, perform **at least one** of the following analyses. The live coding session (`nlpcc25_livecoding_week4.ipynb`) demonstrated some of these techniques (e.g., smart search, clustering). Refer also to OpenAI's embedding documentation (details in [openai_embedding_ref.pdf](./openai_embedding_ref.pdf)) or the Gemini API tutorials linked in `class4-outline.md` for more ideas.

1.  **Choose ONE Analysis (minimum):**
    * **A. Semantic Search (Smart Search):**
        * Implement a system where a user can input a query (a sentence or a few keywords).
        * Your system should find and rank the most semantically similar text samples from your synthetic dataset using cosine similarity with the embeddings.
        * Demonstrate its usage with a few example queries.
    * **B. Clustering:**
        * Apply a clustering algorithm (e.g., K-Means, Agglomerative Clustering) to your embeddings.
        * Analyze the resulting clusters. Do the clusters correspond well to your original synthetic labels?
        * Visualize the clusters if possible (e.g., using t-SNE or PCA for dimensionality reduction first, then plotting).
    * **C. Text Classification (using Embeddings):**
        * Train a simple classifier (e.g., Logistic Regression, SVM, k-NN) using the embeddings as features and your synthetic labels as the target.
        * Evaluate its performance on a held-out portion of your synthetic data.
    * **D. Other Creative Analysis:** If you have another idea for analyzing or using your embeddings (e.g., anomaly detection, diversity measurement), feel free to propose and implement it. Clearly explain your method and findings.
2.  **Implement and Document:**
    * Clearly explain the chosen analysis method in your notebook.
    * Show the Python code for your implementation.
    * Present and discuss the results of your analysis. What insights did you gain?

### Task 4: API Key Management

A crucial aspect of working with cloud APIs is securely managing your API keys.

1.  **Secure Setup:**
    * In your Google Colab notebook, demonstrate the **correct and secure way to handle API keys** (e.g., for Gemini API or OpenAI API).
    * **The preferred method is using Colab Secrets.**
    * **Do NOT hardcode your API key directly in a code cell.**
2.  **Documentation:**
    * Briefly explain in a markdown cell *why* the method you chose (hopefully Colab Secrets) is secure and why hardcoding is bad.

---

## Deliverables and Submission

1.  **Google Colab Notebook:**
    * A single `.ipynb` file containing all your work:
        * Synthetic data generation process (including prompts).
        * Code for embedding generation.
        * Implementation of your chosen embedding analysis (code, results, discussion).
        * Demonstration of secure API key handling.
        * Clear explanations in markdown cells throughout the notebook.
        * **Ensure all code cell outputs are visible** in the final notebook.
2.  **GitHub Repository:**
    * Push your completed `.ipynb` notebook to your `nlpcc-ui-2025` GitHub repository.

* **Deadline:** **Friday, May 23rd, 2025, at 23:55 PM Jakarta Time (WIB).**
* **Submission Method:** You **must** notify the instructors via email by the deadline.
* **Email Contents:**
    * Send an email to **both** `natanael.waraney@ui.ac.id` and `natanaelmassie2009@gmail.com`.
    * The subject line should be: `[NLPCC-UI 2025] Class 4 Assignment - Your Name - Student Number`.
    * The email body **must** contain a direct link to your `nlpcc-ui-2025` GitHub repository (specifically linking to the Colab notebook `.ipynb` file within the repository is helpful, but linking the repo is mandatory).
    * If you are aiming for the public sharing bonus, also include a direct link to your public post (LinkedIn, blog, etc.) in the same email.
* **Important:** Submissions are graded based on the work pushed to GitHub *and* the notification email being received by the deadline.

---

## Bonus Opportunities

Enhance your project and score by exploring these optional extensions:

1.  **Multiple Embedding Analyses (+ Bonus Points):**
    * Implement **more than one** type of analysis from Task 3 (e.g., do both semantic search AND clustering).
    * Clearly present the results and any comparative insights for each analysis.
2.  **Diverse Embedding Techniques (+ Bonus Points):**
    * Use **more than one type of embedding model/method**. For instance:
        * Compare results from a Gemini API embedding model vs. an OpenAI API model.
        * Compare an API-based embedding (e.g., Gemini) with a classical model like TF-IDF or an open-source sentence transformer model.
    * If you do this, provide a comparative discussion:
        * How do the results of your chosen analysis (e.g., clustering quality, search relevance) differ between embedding types?
        * Which embedding type seemed to perform better for your specific synthetic data and task? Why might that be?
        * This is a significant opportunity to showcase deeper understanding.

---

## Optional: Public Sharing (1.5x Multiplier)

As outlined in the `scoring-rubric.md`, you can earn a **1.5x multiplier** on your final assignment score by sharing your work publicly.

* **How to Share:** Post about your project on platforms like LinkedIn, a personal blog, Medium, GitHub (e.g., a well-documented public version of your project), etc.
* **What Counts:** Create a public post discussing your project. You could explain:
    * Your synthetic dataset and why you chose those topics.
    * The embedding models you used and your experiences.
    * Your most interesting finding from the embedding analysis.
    * Challenges faced and how you overcame them.
* **Simply having the public GitHub repo for submission is NOT sufficient for the bonus; active sharing and explanation are key.**
* **Polishing:** Use tools like Gemini to help draft or refine your public post!
* **Notify:** Include the **direct link to your public post** in your submission email.

---

## Evaluation Rubric

Your assignment will be evaluated based on the following criteria. Aim for "Excellent" in each category!

| Criteria                         | Max Score | Excellent (Full Points)                                                                                                                                                              | Good (Partial Points)                                                                                                                                          | Needs Improvement (Low/No Points)                                                                                                |
| :------------------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **1. Synthetic Data Creation** | 25        | Dataset is creative, with **at least 5 clearly distinct and well-justified topics/labels**. Sufficient volume of high-quality, relevant samples per topic. Prompts well-documented. | Dataset has 3-4 distinct topics, or topics are somewhat overlapping. Sample quality/volume is adequate. Prompts documented.                                     | Fewer than 3 topics, topics are unclear/irrelevant, or data quality is poor. Minimal/no prompt documentation.                  |
| **2. Embedding Generation** | 20        | Embeddings correctly generated for all synthetic data using a chosen model. Process is clearly explained. Code is efficient and correct.                                         | Embeddings generated for most data, but minor errors or inefficiencies in code/process. Explanation is adequate.                                               | Significant issues in embedding generation (e.g., wrong model usage, many samples missed). Process poorly explained or incorrect. |
| **3. Embedding Analysis** | 30        | **At least one analysis method** is implemented correctly, demonstrating clear understanding. Results are well-presented, insightful, and thoroughly discussed.                     | Chosen analysis method is mostly correct, but implementation may have minor flaws or results are not fully explored/discussed. Presentation could be clearer. | Analysis method is poorly chosen, incorrectly implemented, or results are missing/misinterpreted. Little to no discussion.        |
| **4. API Key Management** | 10        | API Key is managed securely using **Colab Secrets**. Clear explanation of why this method is secure and why hardcoding is insecure.                                              | API Key is managed, but not via Colab Secrets (e.g., environment variable if shown correctly, but Colab Secrets preferred). Some explanation provided.          | API Key is hardcoded in a cell, or no attempt at secure management. No/poor explanation.                                          |
| **5. Notebook & Code Quality** | 15        | Notebook is exceptionally well-organized, with clear markdown explanations. Code is clean, well-commented, and efficient. All outputs are visible and easy to understand.             | Notebook is generally organized, code is functional. Some areas could be clearer or better documented. Most outputs visible.                               | Notebook is disorganized, code is messy/has errors, or key outputs are missing/unclear.                                         |
| **BONUS: Multiple Analyses** | Up to +10 | Implements **one or more additional distinct analysis methods** effectively, with clear results and comparisons.                                                                   | Attempts an additional analysis, but implementation or discussion is basic.                                                                                    | N/A                                                                                                                              |
| **BONUS: Diverse Embeddings** | Up to +15 | Uses **more than one type of embedding model/method** (e.g., API vs API, or API vs TF-IDF/OSS) AND provides a thoughtful **comparative analysis** of their performance/results. | Uses more than one embedding type, but comparative analysis is superficial or missing.                                                                         | N/A                                                                                                                              |

**Base Score Total: 100 points.** Bonus points can increase your score further. The final score is subject to the 1.5x public sharing multiplier if applicable.

---

Good luck with this assignment! This is a great opportunity to showcase your understanding of modern NLP techniques and build a cool project. Don't hesitate to refer to the class materials, API documentation, and the live coding examples.
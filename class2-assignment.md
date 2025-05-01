---
layout: default
title: Class 2 - Assignment
---

# Class 2 Assignment: Regex Explorations in Text Data

Following up on our dive into Regular Expressions (Regex), this assignment focuses on applying these powerful pattern-matching tools to real text data. You'll practice crafting regex patterns, exploring datasets, and refining your searches.

This assignment is designed for exploration. The minimum requirements get you started, but the real goal is to experiment, be creative, and see what interesting patterns you can uncover!

---

## Task: Explore Text Data with Regex

Your task is to use Python (specifically the `re` library) within a notebook environment (like Google Colab) to explore one or more text datasets using regular expressions.

1.  **Choose Your Dataset(s):**
    *   Select at least one text dataset to work with. You can use **any** of the datasets provided below (all available in the same folder link) or find your own interesting text data (news articles, literary works, social media data, code, etc. – make sure you have the rights to use it!).
    *   **Provided Datasets Folder:** [https://1drv.ms/f/s!AhVxHmatz-M7jeoLgggqXVaJ9fbifA?e=oZRCZQ](https://1drv.ms/f/s!AhVxHmatz-M7jeoLgggqXVaJ9fbifA?e=oZRCZQ)
    *   **Available Datasets in the folder:**
        *   **COVID-19 Indonesian Tweets (May-July 2020):** Contains original (`covid-sentiment.csv`) and translated English (`TRANSLATED-covid-sentiment.csv`) tweets related to COVID and the government.
        *   **Indonesian Email Spam:** Contains ~2600 emails labeled as spam or ham (`email_spam_indo.csv`), translated from an English dataset.
        *   **Indonesia Election News 2024 (Jan-Dec 2023):** Contains ~19.8k news articles (`news_data.csv`) from detik.com covering the 2024 Indonesian election period.
        *   **TED Talks (up to Sep 2017):** Contains metadata (`ted_main.csv`) and full English transcripts (`transcripts.csv`) for ~2500 TED talks.
    *   Download the specific data file(s) you want to use from the OneDrive folder and load the chosen data file into your notebook. (tip: upload to your own Google Drive and connect to Google Colab as shown in our live coding session in Week 2! But again this is optional)
    *   **Using Your Own Data:** The datasets above are curated options, but you are strongly encouraged to use your own text dataset if you find one more relevant or interesting to your goals! Just make sure to include a brief justification in your notebook explaining your choice and provide access to the data if it's not publicly available.

2.  **Define 5 Creative Search Goals:**
    *   Come up with **five distinct goals** for patterns you want to find in the text. Be creative! Think beyond simple keyword searches. Examples:
        *   Finding all email addresses.
        *   Identifying phone numbers in various formats.
        *   Extracting dates mentioned in the text.
        *   Finding specific grammatical structures (e.g., sentences ending with a question mark).
        *   Locating mentions of monetary values (e.g., Rp 10,000;  £20.50).
        *   Searching for specific names or titles with variations (like the "Jokowi" example).
        *   Finding lines that contain repeated words.
        *   Identifying specific HTML tags (if using web data).
        *   *Your own fun or absurd ideas!*

3.  **Demonstrate Regex Depth for Each Goal:**
    *   For **each** of your five goals, demonstrate how you can refine your regex search. Show at least 2-3 variations of your regex pattern for that single goal, explaining the progression.
    *   **Example Progression (Goal: Finding "Jokowi"):**
        1.  `r"Jokowi"` (Simple, case-sensitive)
        2.  `r"[Jj]okowi"` (Case-insensitive first letter)
        3.  `r"[Jj][Oo][Kk][Oo][Ww][Ii]"` (Fully case-insensitive)
        4.  `r"([Jj]okowi|[Jj]oko [Ww]idodo)"` (Includes alternative name)
    *   Explain *why* you are refining the pattern (e.g., "to catch variations in capitalization," "to include the full name," "to handle different formatting").
    *   Show the *results* of applying each regex pattern (e.g., print the matches found, or count them).
    *   You MUST use the Python `re` library for all pattern matching (e.g., `re.findall()`, `re.search()`, `re.match()`, etc.).

4.  **Document in a Notebook:**
    *   Perform all your work in a Python notebook (`.ipynb`).
    *   Use markdown cells to clearly state each of your 5 search goals.
    *   For each goal, include code cells showing your different regex patterns, the code to apply them (`re.findall`, `re.search`, etc.), and the output/results.
    *   Add explanations in markdown cells about your regex choices and refinements.
    *   **Important:** Ensure your final submitted notebook (`.ipynb` file on GitHub) has all the code cell outputs saved and visible. The instructor should be able to see your results without needing to re-run the entire notebook. Check the live coding notebook from Week 2 for an example of how results should be presented.

5.  **Save and Add to Your GitHub Repo:**
    *   Save your notebook (e.g., `class2_regex_exploration.ipynb`).
    *   Place this `.ipynb` file inside your **existing** `nlpcc-ui-2025` repository directory on your local machine.
    *   Add the notebook file to Git staging (`git add your_notebook_name.ipynb`).
    *   Commit the new file (`git commit -m "Add Class 2 regex assignment notebook"`).
    *   Push this commit to GitHub (`git push origin main` or your default branch).
    *   Or basically follow our live coding example! 

**Goal:** This task aims to solidify your understanding of regex syntax and its practical application in text analysis. We want to see your thought process in refining patterns and your creativity in defining search goals.

---

## Optional: Downstream Analysis (Up to +20 Extra Points)

Want to take your exploration further and earn extra credit? Go beyond just *finding* patterns with regex and *use* those findings for some simple downstream analysis. This is highly encouraged and will contribute significantly to your score (potentially exceeding 100 points before the public sharing bonus!).

**The Idea:** Use the information you extracted using your regex patterns as input for another layer of analysis within your notebook. 

**Examples (inspired by our live coding & beyond):**

*   **Simple Named Entity Recognition (NER):** Use regex to identify potential names (e.g., capitalized words after titles like 'Mr.', 'Presiden') or locations (e.g., words following 'di', 'ke'). List the unique entities found.
*   **Co-occurrence Analysis:** Find documents (tweets, articles, emails) where multiple entities (e.g., different politicians' names found via regex) appear together. You could visualize this as a simple network graph showing who is mentioned with whom.
*   **Frequency Analysis:** Track how often certain patterns (e.g., specific keywords, monetary values, date formats) appear across different documents or over time (if timestamps are available). Create simple bar charts or tables.
*   **Basic Topic Frequency:** Use regex to find keywords related to certain topics (e.g., 'vaksin', 'bantuan', 'ekonomi' in the COVID data). Count how often these topic keywords appear.
*   **Targeted Sentiment Snippets:** Find sentences containing specific patterns (e.g., mentions of a particular policy or person) and analyze the sentiment expressed in just those sentences (you could use a simple pre-built sentiment library or even just manually label a few as positive/negative/neutral).

**Formal Terms (for your further research):** The techniques above relate to concepts like *Named Entity Recognition (NER)*, *Co-occurrence Networks / Association Analysis*, *Frequency Distribution*, *Keyword Extraction*, and *Targeted Sentiment Analysis*.

**How to present:** Clearly explain your downstream analysis goal, show the code used to perform the analysis on your regex results, and present the findings clearly (tables, charts, summaries).

---

## Use of AI Tools (Encouraged!)

Remember the tools we discussed in Class 2, like **Google Gemini AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/))? You are highly encouraged to use these AI tools to help you with this assignment!

*   **Brainstorming Search Goals:** Ask AI for ideas on interesting patterns to look for in your chosen dataset.
*   **Generating Regex Patterns:** Use AI to help you draft initial regex patterns or suggest refinements.
*   **Debugging Code:** If your Python code or regex isn't working, ask AI for help debugging.
*   **Explaining Concepts:** If you're unsure about a regex concept, ask AI for an explanation.
*   **Improving Explanations:** Use AI to help you write clearer explanations in your notebook.

Using AI as a collaborative tool is a key skill in modern development. Documenting how you used AI (e.g., prompts you used, how AI helped) in your notebook is welcome, though not mandatory.

---

## Deadline and Submission

*   **Deadline:** Tuesday, May 6th, 2025, at 23:55 PM Jakarta Time (WIB). 
*   **Submission Method:** You **must** notify the instructors via email by the deadline.
*   **Email Contents:**
    *   Send an email to **both** `natanael.waraney@ui.ac.id` and `natanaelmassie2009@gmail.com`.
    *   The subject line should be: `[NLPCC-UI 2025] Class 2 Assignment - Your Name - Student Number`.
    *   The email body **must** contain a direct link to your `nlpcc-ui-2025` GitHub repository (specifically linking to the notebook is helpful but linking the repo is mandatory).
    *   If you are aiming for the public sharing bonus, also include a direct link to your public post (LinkedIn, blog, etc.) in the same email.
*   **Important:** Submissions are graded based on the work pushed to GitHub *and* the notification email being received by the deadline.

---

## Optional: Public Sharing (Bonus Opportunity)

As outlined in the `scoring-rubric.md` and similar to the first assignment, you can earn bonus points by sharing your work publicly.

*   **The Bonus:** Successfully sharing your work publicly (and notifying the instructors via the submission email) will apply a **1.5x multiplier** to your final assignment score (e.g., a score of 80 becomes 120!).
*   **How to Share:** Post about your regex exploration on platforms like LinkedIn, a personal blog, Medium, etc.
*   **What Counts:** Create a public post discussing your assignment. You could explain one of your interesting search goals, share a tricky regex pattern you figured out, or reflect on what you learned about text patterns. **Simply having the public GitHub repo is not enough for the bonus.**
*   **Polishing:** Use tools like Gemini to help draft or refine your post!
*   **Notify:** Include the **direct link to your public post** in your submission email.

---

## Evaluation Rubric (How to Get 100%)

Your assignment will be evaluated based on the following rubric. Aim for the "Excellent" column in each category!

| Criteria                           | Max Score | Excellent (Full Points)                                                                                                           | Good (Partial Points)                                                                                                   | Needs Improvement (Low/No Points)                                                                 |
| :--------------------------------- | :-------- | :-------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | 
| **1. Completion**                  | 10        | All 5 distinct search goals are defined and addressed in the notebook.                                                              | 3-4 search goals are addressed, or some are very superficially handled.                                                  | Fewer than 3 search goals addressed, or goals are not distinct.                                     |
| **2. Regex Depth/Refinement**      | 20        | Each of the 5 goals clearly shows 2-3+ meaningful regex refinements with strong explanations for the progression.                 | Most goals show refinement, but some lack depth (e.g., only 1-2 patterns) or explanations are weak/missing.           | Little to no refinement shown for most goals; patterns are basic or explanations are absent.        |
| **3. Creativity & Insight**        | 20        | Goals demonstrate thoughtful, non-trivial exploration of the dataset; shows genuine effort to find interesting patterns.            | Goals are mostly standard/obvious (e.g., finding simple keywords) with limited exploration beyond basic examples.     | Goals are trivial, nonsensical, or copied directly from examples without adaptation.              |
| **4. Code Quality & Clarity**      | 20        | Python code (`re` library) is correct, efficient, well-commented where needed. Notebook is very well-organized.                 | Code mostly works but might be inefficient or unclear. Notebook organization is acceptable but could be improved.     | Code has significant errors, is very unclear, or doesn't use the `re` library appropriately. Notebook is messy. |
| **5. Results & Presentation**      | 20        | Results for *each* regex step are clearly shown and easy to interpret. Final notebook outputs are saved and visible.            | Most results are shown, but presentation might be unclear for some steps. Final outputs might require re-running. | Results are missing for many steps, poorly presented, or final notebook outputs are not saved.      |
| **6. Dataset Choice/Justification**| 10        | Uses one of the provided datasets (automatic points) **OR** uses a custom dataset with clear, concise justification provided. | *N/A*                                                                                                                   | Uses a custom dataset with weak/missing justification.                                            |
| **7. Downstream Analysis**         | **+20**   | *(Optional Bonus)* Meaningful downstream analysis performed using regex results. Well-explained and clearly presented.            | *(Optional Bonus)* Basic downstream analysis attempted, but may be simplistic or presentation unclear.                 | No downstream analysis attempted.                                                                 |

**Total:**                         | **100 (+20)** | The base score is out of 100. Meeting criteria 1-6 thoroughly leads to 100. Excellent Downstream Analysis (Criteria 7) can add up to 20 bonus points, for a maximum of 120 (before the 1.5x public sharing multiplier). |                                                                                                         |                                                                                                   |

---

Have fun exploring the world of text with Regex! Don't hesitate to experiment with complex patterns or unusual search goals. 
---
layout: default
title: Class 4 - Semantic Representations & Embeddings
---

# Class 4: Semantic Representations & Embeddings

This document outlines the topics for our fourth class meeting and provides recommended materials to review beforehand.

### Preview for Class 4 (e.g., Wednesday, May 15th, 2025)

This week, we transition from classical NLP techniques to the powerful world of **semantic representations** using **embeddings**. We'll explore how words, phrases, and documents can be represented as dense vectors that capture their meaning, enabling a wide range of advanced NLP applications.

**Main Topics:**

*   **What are Embeddings?**
    *   Moving beyond sparse representations (like bag-of-words, tf-idf).
    *   The concept of dense vector representations.
    *   The distributional hypothesis: words in similar contexts have similar meanings.
*   **Why Embeddings?**
    *   Capturing semantic similarity and relationships.
    *   Powering downstream tasks like search, classification, clustering, and more.
*   **Generating Embeddings:**
    *   Introduction to pre-trained embedding models (e.g., from Gemini API, OpenAI API).
    *   How to obtain embeddings using API calls (Python examples).
    *   Understanding embedding dimensionality.
*   **Using Embeddings:**
    *   Calculating semantic similarity using cosine similarity.
    *   Conceptual overview of applications: semantic search, text classification, clustering.
*   **Task-Specific Embeddings:**
    *   Understanding `task_type` in Gemini API for optimized embeddings.
    *   The concept of tailoring embeddings for retrieval, classification, etc.
*   **Ethical Considerations:**
    *   Brief discussion on biases in embeddings (related to Jurafsky Ch 6.11).

We'll cover the conceptual underpinnings and work through practical examples of generating and using embeddings in class.

## Class 4 Materials & Recording

*   **Class 4 Slides:** [Link](./nlpcc-w4-v4.pdf)
*   **Full Recording:** [Link to OneDrive](https://1drv.ms/f/s!AhVxHmatz-M7jepCveewGL2nGFyFPQ?e=pbMusQ)
*   **Live Coding Examples (Python Notebook):** [Link](./nlpcc_2025_week4.ipynb)

## Pre-Class Reading List: Understanding and Using Embeddings

To prepare for our discussion on embeddings, please review the following materials. They cover the theoretical background and practical API usage.

---

### 1. Core Concepts: Jurafsky & Martin - Chapter 6

This chapter provides a foundational understanding of vector semantics and embeddings.

*   **Reading:** Jurafsky & Martin, "Speech and Language Processing" (3rd Edition), **Chapter 6: Vector Semantics and Embeddings**.
    *   Focus on understanding:
        *   Lexical Semantics (Section 6.1)
        *   Vector Semantics (Section 6.2)
        *   Words as vectors, term-document vs. term-term matrices (Section 6.3)
        *   Cosine for measuring similarity (Section 6.4)
        *   TF-IDF and PPMI (Sections 6.5, 6.6 - good to know as background for sparse vectors)
        *   **Word2vec (Section 6.8 - very important for dense embeddings)**
        *   Semantic properties of embeddings (Section 6.10)
        *   **Bias in Embeddings (Section 6.11 - crucial for ethical understanding)**
    *   **Link to Textbook PDF:** [https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)

---

### 2. Practical Embeddings: Gemini API

Familiarize yourself with how to generate embeddings using Google's Gemini API.

*   **Reading:** Gemini API Documentation - Embeddings
    *   **Source:** Review the official Gemini API documentation on embeddings. The key information is summarized below.
    *   **Key Concepts to Understand:**
        *   What embeddings are (numerical representations, vectors capturing meaning).
        *   How to generate embeddings using the `embedContent` method.
        *   The concept of `task_type` for optimizing embeddings (e.g., `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`, `CLASSIFICATION`).
        *   Common use cases (semantic search, clustering, classification, vector databases).
        *   Available embedding models.

*   **Gemini API Embeddings Overview (from provided material):**

    The Gemini API supports several embedding models that generate embeddings for words, phrases, code, and sentences. The resulting embeddings can then be used for tasks such as semantic search, text classification, and clustering, among many others.

    **What are embeddings?**

    Embeddings are numerical representations of text (or other media formats) that capture relationships between inputs. Text embeddings work by converting text into arrays of floating point numbers, called *vectors*. These vectors are designed to capture the meaning of the text. The length of the embedding array is called the vector's *dimensionality*. A passage of text might be represented by a vector containing hundreds of dimensions.

    Embeddings capture semantic meaning and context, which results in text with similar meanings having "closer" embeddings. For example, the sentence "I took my dog to the vet" and "I took my cat to the vet" would have embeddings that are close to each other in the vector space.

    You can use embeddings to compare different texts and understand how they relate. For example, if the embeddings of the text "cat" and "dog" are close together you can infer that these words are similar in meaning, context, or both. This enables a variety of [common AI use cases](https://ai.google.dev/gemini-api/docs/embeddings#use-cases).

    **Generate embeddings**

    Use the `embedContent` method to generate text embeddings:

    *Python Example:*
    ```python
    from google import genai

    # Make sure to configure your API key securely, e.g., via environment variables or Colab secrets
    # client = genai.Client(api_key="YOUR_GEMINI_API_KEY") # Replace with secure key access

    # Example:
    # import os
    # GEMINI_API_KEY = os.getenv('GEMINI_API_KEY') # Or use Colab secrets
    # genai.configure(api_key=GEMINI_API_KEY)
    # model = genai.GenerativeModel('gemini-embedding-exp-03-07') # Or other embedding model
    # result = model.embed_content(content="What is the meaning of life?")
    # print(result['embedding'])

    # Corrected based on typical genai usage for embeddings:
    import google.generativeai as genai
    import os
    # genai.configure(api_key="YOUR_GEMINI_API_KEY") # Configure securely
    # model = 'models/embedding-001' # Or other embedding model like 'models/text-embedding-004'
    # result = genai.embed_content(model=model, content="What is the meaning of life?")
    # print(result['embedding'])
    ```
    *(Note: The provided Python snippet `client.models.embed_content` might be slightly different from the common `google.generativeai.embed_content` or `GenerativeModel(...).embed_content` usage. Refer to the latest official Gemini Python SDK documentation for the most current method.)*

    *Node.js Example:*
    ```javascript
    // import { GoogleGenerativeAI } from "@google/generative-ai"; // Common import
    // async function main() {
    //     const genAI = new GoogleGenerativeAI("YOUR_GEMINI_API_KEY"); // Secure key access
    //     const model = genAI.getGenerativeModel({ model: "embedding-001"}); // Or other model
    //     const result = await model.embedContent("What is the meaning of life?");
    //     const embedding = result.embedding;
    //     console.log(embedding.values);
    // }
    // main();
    ```

    *cURL Example:*
    ```bash
    # curl "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent?key=$GEMINI_API_KEY" \
    # -H 'Content-Type: application/json' \
    # -d '{"model": "models/embedding-001",
    #      "content": {
    #      "parts":[{
    #      "text": "What is the meaning of life?"}]}
    #     }'
    ```
    *(Note: Model names like `gemini-embedding-exp-03-07` might be experimental or specific versions. `embedding-001` or `text-embedding-004` are commonly cited. Always check current model availability.)*

    You can also generate embeddings for multiple chunks at once by passing them in as a list of strings.

    **Task types**

    When building Retrieval Augmented Generation (RAG) systems, a common design is to use text embeddings to perform a similarity search. In some cases this can lead to degraded quality, because questions and their answers are not semantically similar. For example, a question like "Why is the sky blue?" and its answer "The scattering of sunlight causes the blue color," have distinctly different meanings as statements, which means that a RAG system won't automatically recognize their relation.

    Task types enable you to generate optimized embeddings for specific tasks, saving you time and cost and improving performance.

    *Python Example with Task Type:*
    ```python
    # import google.generativeai as genai
    # import os
    # genai.configure(api_key="YOUR_GEMINI_API_KEY") # Configure securely
    # model_name = 'models/embedding-001' # Or 'models/text-embedding-004'
    # result = genai.embed_content(
    #     model=model_name,
    #     content="What is the meaning of life?",
    #     task_type="SEMANTIC_SIMILARITY" # or "RETRIEVAL_QUERY", "RETRIEVAL_DOCUMENT", etc.
    # )
    # print(result['embedding'])
    ```

    **Supported task types**

    | Task type             | Description                                                                                                                               |
    | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | `SEMANTIC_SIMILARITY` | Used to generate embeddings that are optimized to assess text similarity.                                                                 |
    | `CLASSIFICATION`      | Used to generate embeddings that are optimized to classify texts according to preset labels.                                              |
    | `CLUSTERING`          | Used to generate embeddings that are optimized to cluster texts based on their similarities.                                              |
    | `RETRIEVAL_DOCUMENT`, `RETRIEVAL_QUERY`, `QUESTION_ANSWERING`, and `FACT_VERIFICATION` | Used to generate embeddings that are optimized for document search or information retrieval.                                              |
    | `CODE_RETRIEVAL_QUERY`| Used to retrieve a code block based on a natural language query. Embeddings of the code blocks are computed using `RETRIEVAL_DOCUMENT`. |

    **Use cases**

    Text embeddings are used in a variety of common AI use cases, such as:
    -   Information retrieval: [Document search tutorial](https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/tutorials/document_search.ipynb)
    -   Clustering: [Embedding clustering tutorial](https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/tutorials/clustering_with_embeddings.ipynb)
    -   Vector database: [Vector database tutorial](https://github.com/google-gemini/cookbook/blob/main/examples/chromadb/Vectordb_with_chroma.ipynb)
    -   Classification: [Classification tutorial](https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/tutorials/text_classifier_embeddings.ipynb)

    **Embedding models (examples, check official docs for latest)**
    -   `embedding-001` (formerly `text-embedding-004`)
    -   `text-embedding-004` (check if this is still the name or if `embedding-001` replaced it)
    -   `gemini-embedding-exp-03-07` (experimental, specific version)

    **What's next**
    Check out the [embeddings quickstart notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb).

---

### 3. Practical Embeddings: OpenAI API

Understand how OpenAI's API provides embeddings and their common use cases.

*   **Reading:** OpenAI API Documentation - Embeddings
    *   **Source:** Review the official OpenAI API documentation on embeddings. The key information is summarized below.
    *   **Key Concepts to Understand:**
        *   How OpenAI defines embeddings and their purpose.
        *   Models available (e.g., `text-embedding-3-small`, `text-embedding-3-large`).
        *   How to get embeddings using the API.
        *   The `dimensions` parameter for controlling embedding size.
        *   Various use cases like search, clustering, recommendations, classification.

*   **OpenAI API Embeddings Overview (from provided material):**

    **What are embeddings?**

    OpenAI's text embeddings measure the relatedness of text strings. Embeddings are commonly used for:
    *   Search (where results are ranked by relevance to a query string)
    *   Clustering (where text strings are grouped by similarity)
    *   Recommendations (where items with related text strings are recommended)
    *   Anomaly detection (where outliers with little relatedness are identified)
    *   Diversity measurement (where similarity distributions are analyzed)
    *   Classification (where text strings are classified by their most similar label)

    An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

    **How to get embeddings**

    To get an embedding, send your text string to the embeddings API endpoint along with the embedding model name (e.g., `text-embedding-3-small`):

    *Python Example:*
    ```python
    from openai import OpenAI
    # client = OpenAI(api_key="YOUR_OPENAI_API_KEY") # Configure securely, e.g., from os.environ

    # response = client.embeddings.create(
    #     input="Your text string goes here",
    #     model="text-embedding-3-small" # or "text-embedding-3-large", "text-embedding-ada-002"
    # )
    # print(response.data[0].embedding)
    ```

    By default, the length of the embedding vector is 1536 for `text-embedding-3-small` or 3072 for `text-embedding-3-large`. To reduce the embedding's dimensions without losing its concept-representing properties, pass in the `dimensions` parameter.

    **Embedding models**

    OpenAI offers powerful third-generation embedding models (denoted by -3 in the model ID).
    | Model                   | ~ Pages per dollar | Performance on MTEB eval | Max input |
    | ----------------------- | ------------------ | ------------------------ | --------- |
    | `text-embedding-3-small`| 62,500             | 62.3%                    | 8192      |
    | `text-embedding-3-large`| 9,615              | 64.6%                    | 8192      |
    | `text-embedding-ada-002`| 12,500             | 61.0%                    | 8192      |

    **Use cases**
    The documentation details various use cases including:
    *   Obtaining embeddings for a dataset.
    *   Reducing embedding dimensions (using the `dimensions` parameter or manual normalization).
    *   Question answering using embeddings-based search.
    *   Text search and Code search using embeddings.
    *   Recommendations.
    *   Data visualization in 2D (using t-SNE).
    *   Embeddings as text feature encoders for ML algorithms (regression, classification).
    *   Zero-shot classification.
    *   Obtaining user and product embeddings for cold-start recommendations.
    *   Clustering.

    **FAQ Highlights:**
    *   **Token counting:** Use `tiktoken` library. For `-3` models, use `cl100k_base` encoding.
    *   **Nearest neighbor search:** Vector databases are recommended for speed.
    *   **Distance function:** Cosine similarity is recommended. OpenAI embeddings are normalized to length 1, so dot product is equivalent for ranking.

---

## Recommended Tools for Exploration

*   **NotebookLM ([https://notebooklm.google.com/](https://notebooklm.google.com/)):**
    *   Upload the Jurafsky chapter PDF or your notes on embeddings.
    *   Ask questions, get summaries, and use the bilingual (English & Bahasa Indonesia) audio overview feature to deepen your understanding.
*   **Google Gemini AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)):**
    *   Experiment with prompting Gemini for explanations of embedding concepts.
    *   Use it to help generate or debug Python code for working with embeddings.
*   **OpenAI Playground ([https://platform.openai.com/playground](https://platform.openai.com/playground)):**
    *   While primarily for chat models, you can use it to ask questions about OpenAI's embedding models or related concepts.

## Podcast Prep Materials

To help you prepare for our discussions on embeddings, listen to this podcast-style audio summary. It will focus on key concepts from Jurafsky Chapter 6 and the practical aspects of using embedding APIs.

*   **Podcast for Main Topics (Embeddings, Vector Semantics, APIs - based on Jurafsky Ch 6 & API Docs):**
    *   [Link to OneDrive](https://1drv.ms/f/s!AhVxHmatz-M7jepCveewGL2nGFyFPQ?e=pbMusQ)

*(Links will be provided via email before class)*

## Assignment for Class 4

*   **Class 4 Assignment:** [Class 4 - Assignment: Exploring Text Embeddings](./class4-assignment.md)
*   **Deadline:** Friday, May 23rd, 2025, at 23:55 PM Jakarta Time (WIB).

The assignment will involve hands-on practice with generating and using text embeddings. 
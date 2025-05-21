---
layout: default
title: Class 5 - Large Language Models & Generative AI
---

# Class 5: Large Language Models & Generative AI

This document outlines the topics for our fifth class meeting and provides recommended materials to review beforehand.

### Preview for Class 5 (e.g., Wednesday, May 21st, 2025)

This week, we transition from understanding text with embeddings to generating and interacting with text using **Large Language Models (LLMs)** and **Generative AI**. We'll explore how these models work, their applications, and demonstrate practical interactions.

**Main Topics:**

*   **Recap of Last Week & The Role of Embeddings:**
    *   Brief review of embeddings and semantic similarity.
    *   Embeddings provide "context," but for tailored, meaningful answers, we often need more.
*   **Enter Generative AI & LLMs:**
    *   How embeddings act as a behind-the-scenes process, guiding LLMs (e.g., helping an LLM know "where to look" for an answer to "how many planets?").
    *   The role of techniques like Reinforcement Learning from Human Feedback (RLHF) in "crafting good answers."
*   **The LLM Landscape: Key Products:**
    *   Overview of prominent models/platforms: ChatGPT (OpenAI), Gemini (Google), Claude (Anthropic), Grok (xAI), Mistral, etc.
*   **Understanding LLM Benchmarks:**
    *   How to interpret common benchmarks (e.g., ELO scores).
    *   Considering the ELO vs. cost frontier.
    *   Awareness of the variety of benchmarks available.
*   **Core Use Cases of LLMs & Generative AI:**
    *   Coding assistance.
    *   Media: Ideation, scriptwriting, content generation.
    *   Design: Front-end and back-end conceptualization.
    *   General Chat and conversational AI.
*   **Practical Showcases & Demonstrations:**
    *   Interacting with LLMs via web UIs.
    *   Single-turn chat via API (e.g., GPT-4o).
    *   Multi-turn chat with history via API (e.g., GPT-4o).
    *   Iterative prompting for batch tasks (e.g., summarizing multiple news articles).
    *   Achieving structured output (e.g., sentiment identification, information extraction, classification using LLMs).
*   **Ethical Considerations & Limitations (from Jurafsky Ch. 10.6).**

We'll cover the conceptual underpinnings, drawing from Jurafsky Ch. 10, and work through practical examples in class.

## Class 5 Materials & Recording

*   **Class 5 Slides:** [Link - *Placeholder, TBD*]
*   **Full Recording:** [Link - *Placeholder, will be updated after class*]
*   **Live Coding Examples (Python Notebook):** [Link - *Placeholder for Class 5 Live Coding Notebook*]

## Pre-Class Reading List: Understanding & Using LLMs

To prepare for our discussion on LLMs and their generative applications, please review the following materials. The presentation will cover these topics in more detail.

---

### 1. Core Reading: Jurafsky & Martin - Chapter 10

This chapter is central to this week's topics and provides a comprehensive overview of Large Language Models.

*   **Reading:** Jurafsky & Martin, "Speech and Language Processing" (3rd Edition), **Chapter 10: Large Language Models**.
    *   Familiarize yourself with:
        *   The concept of pretraining and how LLMs learn (Introduction, Section 10.3.1).
        *   How Transformers are used in LLMs for conditional generation (Section 10.1).
        *   Overview of text generation and sampling methods (Section 10.2).
        *   The idea of finetuning (Section 10.3.3).
        *   How LLMs are evaluated (Section 10.4 - e.g., perplexity).
        *   Potential Harms from Language Models (Section 10.6).
    *   **Link to Textbook PDF:** [https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf) (Refer to Chapter 10)

---

### 2. Review: Interacting with LLMs & APIs

Refresh your understanding of how to interact with LLMs and their APIs from previous sessions.

*   **Review Materials from `class1-outline.md`:**
    *   **Re-read:** The "AI Chat Interfaces: ChatGPT & Google Gemini" section for general interaction principles.
*   **API Documentation (for interaction patterns & getting started with text generation):**
    *   **Gemini API Documentation:** [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)
        *   Focus on quickstarts for your chosen language (e.g., Python) to see how `generateContent` calls are structured.
    *   **OpenAI API Documentation:** [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)
        *   You may need to create an account. Alternatively, refer to the OpenAI embedding documentation PDF provided in Week 4 materials (`in_progress/week4_openai_embedding_docs.md`) for examples of API interaction structure, which you can adapt for chat/completion endpoints.
    *   **Key takeaway:** Secure API key management and basic request/response flow. Specifics for text generation will be covered in class.

---

## Recommended Tools for Exploration

These tools will be invaluable for experimenting with LLMs and prompt engineering, as discussed in previous outlines.

*   **NotebookLM ([https://notebooklm.google.com/](https://notebooklm.google.com/)):**
    *   Upload Jurafsky Chapter 10 or other relevant articles.
    *   Use it to ask questions, get summaries, and utilize the audio overview feature.
*   **Google Gemini AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)):**
    *   An excellent place to experiment directly with Gemini models for various text generation tasks.
*   **OpenAI Playground ([https://platform.openai.com/playground](https://platform.openai.com/playground)):**
    *   If accessible, use this to experiment with OpenAI's GPT models.

## Assignment for Class 5

*   **Class 5 Assignment:** [Class 5 - Assignment: LLM & Generative AI Explorations - *Placeholder, TBD*](./class5-assignment.md)
*   **Deadline:** Tuesday, May 28th, 2025, at 23:55 PM Jakarta Time (WIB). (To be confirmed on assignment page).

Details for the Class 5 assignment will be announced soon. It will involve hands-on practice in using LLMs for various media production tasks, focusing on prompt engineering, API interaction, and output analysis, drawing heavily on the concepts from Jurafsky Chapter 10 and in-class demonstrations.
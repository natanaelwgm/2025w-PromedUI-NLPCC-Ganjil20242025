---
layout: default
title: Class 6 - Chatbots, Multi-Modal & Agentic Models
---

# Class 6: Advanced Frontier: Chatbots, Multi-Modal & Agentic Models

This document outlines the topics for our sixth and final core content class meeting and provides recommended materials to review beforehand. We'll be looking at the cutting edge of NLP and AI.

### Preview for Class 6 (e.g., Friday, May 23rd, 2025)

This week, we venture into the advanced frontiers of AI, exploring how systems can converse, understand multiple types of information, and act autonomously to solve complex tasks.

**Main Topics:**

* **Chatbots & Conversational AI Revisited:**
    * Leveraging LLMs for sophisticated dialogue management and persona creation.
    * Integrating external knowledge and tools into conversational agents.
* **Multi-Modal AI Deep Dive:**
    * Understanding models that fuse information from text, images, audio, and video (e.g., Gemini).
    * Techniques for joint representation and cross-modal generation.
    * Applications in media: generative art, video understanding, automated accessibility features.
* **Agentic AI: Building Autonomous Systems:**
    * Core principles: Planning, memory, tool use, and multi-agent collaboration.
    * Designing agentic pipelines for media workflows: from research and ideation to content assembly and distribution.
    * Overview of key frameworks: LangChain, DSPy, LlamaIndex, CrewAI.
* **Ethical Considerations & The Future:**
    * Responsibility in deploying advanced AI systems in media.
    * Addressing potential biases and societal impacts.
    * The evolving landscape and what's next.

We'll cover conceptual frameworks, key technologies, and discuss practical applications and future directions.

---
## Class 6 Materials & Recording

* **Class 6 Slides:** [https://1drv.ms/f/s!AhVxHmatz-M7jepO7RBE4GI7fovF4A?e=g6eXN8](https://1drv.ms/f/s!AhVxHmatz-M7jepO7RBE4GI7fovF4A?e=g6eXN8)
* **Full Recording:** [https://1drv.ms/f/s!AhVxHmatz-M7jepO7RBE4GI7fovF4A?e=g6eXN8](https://1drv.ms/f/s!AhVxHmatz-M7jepO7RBE4GI7fovF4A?e=g6eXN8)
* **Live Coding Examples (Python Notebook):** [./nlpcc_2025_week5_livecoding.ipynb](./nlpcc_2025_week5_livecoding.ipynb)

---
## Pre-Class Reading List: Diving into the Frontier 🚀

For this advanced session, focus on understanding the capabilities of current models and the frameworks used to build with them. Foundational LLM concepts (like those discussed in Jurafsky Ch. 10 for general LLM understanding) are assumed, but our focus shifts to practical application and newer paradigms.

**1. Key API Documentation (Capabilities & Use Cases):**

* **Google Gemini API (Multimodal & Advanced Capabilities):**
    * Review documentation on multimodal models (e.g., Gemini 1.5 Pro with text, image, audio, video understanding).
    * Explore examples of function calling and advanced prompting techniques.
    * **Link:** [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)
* **OpenAI API (Multimodal, Assistants API, Function Calling):**
    * Familiarize yourself with GPT-4 Vision capabilities.
    * Study the Assistants API for building stateful, tool-using agents.
    * Review function calling for enabling tool integration.
    * **Link:** [https://platform.openai.com/docs](https://platform.openai.com/docs) (Navigate to relevant sections like Assistants, Vision, Function calling)

**2. Agentic AI & LLM Application Frameworks (Get Started Guides):**

* **LangChain (Building applications with LLMs):**
    * Understand its core components: Models, Prompts, Chains, Agents, Memory, Indexes.
    * Focus on how it facilitates creating complex applications and agents.
    * **Docs - Get Started:** [https://python.langchain.com/v0.2/docs/get_started/](https://python.langchain.com/v0.2/docs/get_started/)
    * **Conceptual Guide:** [https://python.langchain.com/v0.2/docs/concepts/](https://python.langchain.com/v0.2/docs/concepts/)
* **DSPy (Programming with LLMs, not just prompting):**
    * Grasp its philosophy of abstracting away manual prompting by defining program signatures and using optimizers.
    * Understand how it aims for more systematic and optimizable LLM programs.
    * **GitHub (Readme is a good start):** [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
    * **Introductory Tutorial:** [https://dspy-docs.vercel.app/docs/introduction/getting-started](https://dspy-docs.vercel.app/docs/introduction/getting-started)
* **LlamaIndex (Data framework for LLM applications, RAG focused but has agentic parts):**
    * Focus on how it connects LLMs to external data, crucial for knowledgeable agents.
    * Understand its role in retrieval and augmenting generation.
    * **Docs - Getting Started:** [https://docs.llamaindex.ai/en/stable/getting_started/installation.html](https://docs.llamaindex.ai/en/stable/getting_started/installation.html)
    * **High-Level Concepts:** [https://docs.llamaindex.ai/en/stable/getting_started/concepts.html](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
* **CrewAI (Framework for orchestrating role-playing autonomous AI agents):**
    * Understand its approach to collaborative multi-agent systems.
    * How to define agents with roles, goals, and tools.
    * **Docs:** [https://docs.crewai.com/](https://docs.crewai.com/)
* **Microsoft AutoGen (Framework for multi-agent conversation applications):**
    * Explore its concepts of different types of agents that can chat to solve tasks.
    * **GitHub (Docs in repo):** [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)
    * **Documentation Website:** [https://microsoft.github.io/autogen/](https://microsoft.github.io/autogen/)

**3. Recommended Articles/Overviews (Recent Developments):**
* Search for recent (2024-2025) blog posts or whitepapers from major AI research labs (e.g., Google DeepMind, OpenAI, Meta AI, Anthropic) discussing breakthroughs or new features in multimodal understanding and agentic AI.
* Keywords for search: "State of Multimodal AI 2025," "AI Agents capabilities," "LLM tool use advancements."

---
## Recommended Tools for Exploration 🛠️

Continue leveraging these tools for deeper understanding and experimentation.

* **NotebookLM ([https://notebooklm.google.com/](https://notebooklm.google.com/)):**
    * Upload documentation PDFs, articles, or your notes on these advanced topics.
    * Use it to query, summarize, and compare concepts across different frameworks.
* **Google Gemini AI Studio ([https://aistudio.google.com/](https://aistudio.google.com/)):**
    * Experiment with Gemini 1.5 Pro's multimodal capabilities (text, image, audio, video inputs).
    * Test out function calling and advanced prompting for agent-like behaviors.
* **OpenAI Playground ([https://platform.openai.com/playground](https://platform.openai.com/playground)) (if accessible):**
    * Experiment with GPT-4 Vision, DALL-E for image generation, and the Assistants API or function calling.
* **Hugging Face Hub ([https://huggingface.co/models](https://huggingface.co/models)):**
    * Search for and explore available open-source multi-modal models or agent-related spaces/demos.

---
## Assignment for Class 6

* **Class 5 & 6 Combined Assignment:** [class56-assignment.md](class56-assignment.md)

This assignment is shared with Class 5 and covers both week's content. It involves building LLM applications including a chat system and tabular data processing, with bonus opportunities to explore advanced features like multimodal AI, agentic systems, or RAG that we discuss in this class. **Deadline:** Friday, June 27th, 2025, at 23:55 PM Jakarta Time (WIB).
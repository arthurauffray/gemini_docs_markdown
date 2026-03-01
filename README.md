# 🤖 Gemini API Docs Markdown

> **Mirroring the Gemini API documentation in clean, structured Markdown.**

An offline-first, LLM-optimized collection of the Gemini API documentation. Every capability, every model, and every guide — organized and ready for your next project.

---
#### Note: read [structure.md](/structure.md) to understand the full hierarchy and available categories.
----

## ✨ Features

- 🏎️ **Optimized for LLMs**: Perfectly formatted for RAG (Retrieval Augmented Generation) and AI context.
- 📂 **Structured Layout**: Mirrors the official [Gemini API Documentation](https://ai.google.dev/gemini-api/docs).
- 💻 **Multi-Language**: Comprehensive code snippets for `Python`, `JavaScript`, `Go`, `Java`, `C#`, `REST/curl`, and `Apps Script`.
- 🔍 **Searchable**: Grep your way through the entire Gemini ecosystem in milliseconds.
- 📄 **Clean Markdown**: Zero fluff, just the docs.

## 📁 Repository Structure

The documentation is organized across two main directories:

```text
docs/
├── get_started/            # Quickstart, API keys, Libraries, Pricing...
├── core_capabilities/      # Text, Image, Video, Audio, Function Calling, Thinking...
├── models/                 # Gemini 3, Embeddings, Imagen, Veo, Lyria, TTS...
├── tools_and_agents/       # Code Execution, Computer Use, Deep Research, Search...
├── live_api/               # Real-time streaming, Session management...
├── guides/                 # Caching, Prompt Engineering, Frameworks, Safety...
└── resources/              # Rate Limits, Billing, Troubleshooting, Release Notes...

api_reference/
├── gemini_api_reference.md # Complete API reference overview
├── api_versions.md         # API versioning
└── capabilities/           # Method-level API docs (generateContent, files, etc.)
```

## 🔧 Filter Docs by Language

Use the included `filter_docs.py` to create a copy of the docs filtered to only your language(s) of choice:

```bash
# Copy and filter to Python + REST only (default)
python filter_docs.py --source docs --destination filtered_docs

# Filter for JavaScript only
python filter_docs.py --source docs --destination filtered_docs -l javascript

# Filter in-place (modifies files directly)
python filter_docs.py docs -l python

# Filter a single file
python filter_docs.py docs/core_capabilities/text.md -l go
```

## 🚀 Getting Started

Simply clone the repo and start reading. If you're using this with an AI assistant, point it towards specific files for instant context:

```bash
# Example: Find all function calling examples
grep -rn "function_calling" docs/

# Example: Search for generateContent usage
grep -rn "generateContent" docs/
```

## 🛠️ Built for Developers

Whether you're building a new AI application, integrating Gemini capabilities, or debugging a complex multi-modal pipeline, having the docs at your fingertips (without the browser overhead) is a game changer.

- **Fast**: No loading states, just text.
- **Offline**: Works in the air, on a train, or in a bunker.
- **Accurate**: Sourced directly from the official documentation.

---

*Note: This repository is a community-maintained mirror and is not affiliated with Google.*

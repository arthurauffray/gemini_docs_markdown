# Gemini API Documentation Structure

This document describes the structure of the Gemini API documentation.

## Hierarchy

The documentation is organized into two top-level directories:

1. **`docs/`**: Guides, tutorials, and conceptual documentation
2. **`api_reference/`**: API reference documentation and method specifications

Within each, content is organized into:

1. **Category**: Top-level groups (e.g., `core_capabilities`, `models`, `tools_and_agents`, `guides`)
2. **Topic**: Folders or files within categories covering specific features
3. **Document**: Markdown files containing specific documentation

---

## docs/

### core_capabilities

- 📄 `documents.md`
- 📄 `function_calling.md`
- 📄 `long_context.md`
- 📄 `structured_outputs.md`
- 📄 `text.md`
- 📁 **image** (2 docs)
  - 📄 `image_generation.md`
  - 📄 `image_understanding.md`
- 📁 **speech_and_audio** (2 docs)
  - 📄 `audio_understanding.md`
  - 📄 `speech_generation.md`
- 📁 **thinking** (2 docs)
  - 📄 `thinking.md`
  - 📄 `thought_signatures.md`
- 📁 **video** (2 docs)
  - 📄 `video_generation.md`
  - 📄 `video_understanding.md`

### get_started

- 📄 `api_keys.md`
- 📄 `gemini_api_libraries.md`
- 📄 `interactions_api.md`
- 📄 `overview.md`
- 📄 `pricing.md`
- 📄 `quickstart.md`

### guides

- 📄 `batch_api.md`
- 📄 `coding_agent_skills.md`
- 📄 `context_caching.md`
- 📄 `media_resolution.md`
- 📄 `openai_compatibility.md`
- 📄 `prompt_engineering.md`
- 📄 `token_counting.md`
- 📁 **file_input** (2 docs)
  - 📄 `files_api.md`
  - 📄 `input_methods.md`
- 📁 **frameworks** (5 docs)
  - 📄 `crewai.md`
  - 📄 `langchain_and_langgraph.md`
  - 📄 `llamaindex.md`
  - 📄 `temporal.md`
  - 📄 `vercel_ai_sdk.md`
- 📁 **logs_and_dataset** (2 docs)
  - 📄 `data_logging_and_sharing.md`
  - 📄 `get_started_by_logs.md`
- 📁 **safety** (2 docs)
  - 📄 `safety_guidance.md`
  - 📄 `safety_settings.md`

### live_api

- 📄 `capabilities.md`
- 📄 `ephemeral_tokens.md`
- 📄 `get_started.md`
- 📄 `session_management.md`
- 📄 `tool_use.md`

### models

- 📄 `all_models.md`
- 📄 `embeddings.md`
- 📄 `gemini_3.md`
- 📄 `imagen.md`
- 📄 `lyria.md`
- 📄 `nano_banana.md`
- 📄 `robotics.md`
- 📄 `text_to_speech.md`
- 📄 `veo.md`

### resources

- 📄 `api_troubleshooting.md`
- 📄 `billing_info.md`
- 📄 `deprecations.md`
- 📄 `migrate_to_gen_ai_sdk.md`
- 📄 `partner_and_library_integrations.md`
- 📄 `rate_limits.md`
- 📄 `release_notes.md`
- 📁 **google_cloud_platform** (2 docs)
  - 📄 `oauth_authentication.md`
  - 📄 `vertexai_gemini_api.md`

### tools_and_agents

- 📄 `code_execution.md`
- 📄 `computer_use.md`
- 📄 `deep_research.md`
- 📄 `file_search.md`
- 📄 `google_maps.md`
- 📄 `google_search.md`
- 📄 `overview.md`
- 📄 `url_context.md`

## api_reference/

- 📄 `api_versions.md`
- 📄 `gemini_api_reference.md`
- 📄 `sdk_references_urls.md`
### capabilities

- 📄 `all_methods.md`
- 📄 `batch_api.md`
- 📄 `caching.md`
- 📄 `embeddings.md`
- 📄 `files.md`
- 📄 `generating_content.md`
- 📄 `interactions_api.md`
- 📄 `live_api.md`
- 📄 `live_music_api.md`
- 📄 `models.md`
- 📄 `tokens.md`
- 📁 **file_search** (2 docs)
  - 📄 `document.md`
  - 📄 `file_search_stores.md`

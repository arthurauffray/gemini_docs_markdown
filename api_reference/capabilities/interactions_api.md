The Gemini Interactions API is an experimental API that allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.
[View as markdown](https://ai.google.dev/static/api/interactions.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## Creating an interaction

post https://generativelanguage.googleapis.com/v1beta/interactions Creates a new interaction.
- [Request body](https://ai.google.dev/api/interactions-api#CreateInteraction.request_body)
- [Response](https://ai.google.dev/api/interactions-api#CreateInteraction.response)

### Request body

The request body contains data with the following structure:
model ModelOption (optional) The name of the \`Model\` used for generating the interaction.   
**Required if \`agent\` is not provided.**

Possible
values:

- `gemini-2.5-flash`

  Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.
- `gemini-2.5-flash-image`

  Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.
- `gemini-2.5-flash-lite`

  Our smallest and most cost effective model, built for at scale usage.
- `gemini-2.5-flash-lite-preview-09-2025`

  The latest model based on Gemini 2.5 Flash lite optimized for cost-efficiency, high throughput and high quality.
- `gemini-2.5-flash-native-audio-preview-12-2025`

  Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
- `gemini-2.5-flash-preview-09-2025`

  The latest model based on the 2.5 Flash model. 2.5 Flash Preview is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.
- `gemini-2.5-flash-preview-tts`

  Our 2.5 Flash text-to-speech model optimized for powerful, low-latency controllable speech generation.
- `gemini-2.5-pro`

  Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
- `gemini-2.5-pro-preview-tts`

  Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
- `gemini-3-flash-preview`

  Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.
- `gemini-3-pro-image-preview`

  State-of-the-art image generation and editing model.
- `gemini-3-pro-preview`

  Our most intelligent model with SOTA reasoning and multimodal understanding, and powerful agentic and vibe coding capabilities.
- `gemini-3.1-pro-preview`

  Our latest SOTA reasoning model with unprecedented depth and nuance, and powerful multimodal understanding and coding capabilities.
- `gemini-3.1-flash-image-preview`

  Pro-level visual intelligence with Flash-speed efficiency and reality-grounded generation capabilities.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.
agent AgentOption (optional) The name of the \`Agent\` used for generating the interaction.   
**Required if \`model\` is not provided.**

Possible
values:

- `deep-research-pro-preview-12-2025`

  Gemini Deep Research Agent

The agent to interact with.
input [Content](https://ai.google.dev/api/interactions-api#Resource:Content) or array ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ([Turn](https://ai.google.dev/api/interactions-api#Resource:Turn)) or string (required) The inputs for the interaction (common to both Model and Agent).
system_instruction string (optional) System instruction for the interaction.
tools array ([Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)) (optional) A list of tool declarations the model may call during interaction.
response_format object (optional) Enforces that the generated response is a JSON object that complies with
the JSON schema specified in this field.
response_mime_type string (optional) The mime type of the response. This is required if response_format is set.
stream boolean (optional) Input only. Whether the interaction will be streamed.
store boolean (optional) Input only. Whether to store the response and request for later retrieval.
background boolean (optional) Input only. Whether to run the model interaction in the background.
generation_config GenerationConfig (optional) **Model Configuration**   
Configuration parameters for the model interaction.   
*Alternative to \`agent_config\`. Only applicable when \`model\` is set.*
Configuration parameters for model interactions.

#### Fields

temperature number (optional) Controls the randomness of the output.
top_p number (optional) The maximum cumulative probability of tokens to consider when sampling.
seed integer (optional) Seed used in decoding for reproducibility.
stop_sequences array (string) (optional) A list of character sequences that will stop output interaction.
thinking_level ThinkingLevel (optional) The level of thought tokens that the model should generate.

Possible
values:

- `minimal`
- `low`
- `medium`
- `high`

<br />

thinking_summaries ThinkingSummaries (optional) Whether to include thought summaries in the response.

Possible
values:

- `auto`
- `none`

<br />

max_output_tokens integer (optional) The maximum number of tokens to include in the response.
speech_config SpeechConfig (optional) Configuration for speech interaction.
The configuration for speech interaction.

#### Fields

voice string (optional) The voice of the speaker.
language string (optional) The language of the speech.
speaker string (optional) The speaker's name, it should match the speaker name given in the prompt.
image_config ImageConfig (optional) Configuration for image interaction.
The configuration for image interaction.

#### Fields

aspect_ratio enum (string) (optional) No description provided.

Possible
values:

- `1:1`
- `2:3`
- `3:2`
- `3:4`
- `4:3`
- `4:5`
- `5:4`
- `9:16`
- `16:9`
- `21:9`
- `1:8`
- `8:1`
- `1:4`
- `4:1`
image_size enum (string) (optional) No description provided.

Possible
values:

- `1K`
- `2K`
- `4K`
- `512`
tool_choice [ToolChoiceConfig](https://ai.google.dev/api/interactions-api#Resource:ToolChoiceConfig) or [ToolChoiceType](https://ai.google.dev/api/interactions-api#Resource:ToolChoiceType) (optional) The tool choice for the interaction.
agent_config object (optional) **Agent Configuration**   
Configuration for the agent.   
*Alternative to \`generation_config\`. Only applicable when \`agent\` is set.*

#### Possible Types

Polymorphic discriminator: `type`
DynamicAgentConfig Configuration for dynamic agents.
type object (required) No description provided.

Always set to `"dynamic"`.
DeepResearchAgentConfig Configuration for the Deep Research agent.
thinking_summaries ThinkingSummaries (optional) Whether to include thought summaries in the response.

Possible
values:

- `auto`
- `none`

<br />

type object (required) No description provided.

Always set to `"deep-research"`.
previous_interaction_id string (optional) The ID of the previous interaction, if any.
response_modalities ResponseModality (optional) The requested modalities of the response (TEXT, IMAGE, AUDIO).

Possible
values:

- `text`
- `image`
- `audio`

<br />

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

### Simple Request

<iframe src="https:///frame/api/interactions-api_a78c3656a191fc61337f0eb9564b677efd89f781a218f2885093fb97e9bac186.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "created": "2025-11-26T12:25:15Z",
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3-flash-preview",
  "object": "interaction",
  "outputs": [
    {
      "text": "Hello! I'm functioning perfectly and ready to assist you.\n\nHow are you doing today?",
      "type": "text"
    }
  ],
  "role": "model",
  "status": "completed",
  "updated": "2025-11-26T12:25:15Z",
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 7
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 20,
    "total_thought_tokens": 22,
    "total_tokens": 49,
    "total_tool_use_tokens": 0
  }
}
```

### Multi-turn

<iframe src="https:///frame/api/interactions-api_80220461097181601c66abcc498cc87a3a1c90056c2cf4a2fdaa89810d40aec3.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3-flash-preview",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "The capital of France is Paris."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 50
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 50,
    "total_output_tokens": 10,
    "total_thought_tokens": 0,
    "total_tokens": 60,
    "total_tool_use_tokens": 0
  }
}
```

### Image Input

<iframe src="https:///frame/api/interactions-api_fe8a7d1313ac94f59379dba314adda00769c806d60c35f6449cfac89fc5627bb.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3-flash-preview",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "A white humanoid robot with glowing blue eyes stands holding a red skateboard."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 10
      },
      {
        "modality": "image",
        "tokens": 258
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 268,
    "total_output_tokens": 20,
    "total_thought_tokens": 0,
    "total_tokens": 288,
    "total_tool_use_tokens": 0
  }
}
```

### Function Calling

<iframe src="https:///frame/api/interactions-api_7c5b66c09677dc6c9bc1bb1c4a5cb295f6ff522f576aded8d79169a66c61260e.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3-flash-preview",
  "status": "requires_action",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "model",
  "outputs": [
    {
      "type": "function_call",
      "id": "gth23981",
      "name": "get_weather",
      "arguments": {
        "location": "Boston, MA"
      }
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 100
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 100,
    "total_output_tokens": 25,
    "total_thought_tokens": 0,
    "total_tokens": 125,
    "total_tool_use_tokens": 50
  }
}
```

### Deep Research

<iframe src="https:///frame/api/interactions-api_6b3d214c3111e035124abcd42839fd24cdbef9769a1e89da930817d5101c6e78.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "agent": "deep-research-pro-preview-12-2025",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:22:47Z",
  "updated": "2025-11-26T12:22:47Z",
  "role": "agent",
  "outputs": [
    {
      "type": "text",
      "text": "Here is a comprehensive research report on the current state of cancer research..."
    }
  ],
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 20
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 20,
    "total_output_tokens": 1000,
    "total_thought_tokens": 500,
    "total_tokens": 1520,
    "total_tool_use_tokens": 0
  }
}
```

## Retrieving an interaction

get https://generativelanguage.googleapis.com/v1beta/interactions/{id} Retrieves the full details of a single interaction based on its \`Interaction.id\`.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#getInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#getInteractionById.response)

### Path / Query Parameters

id string (required) The unique identifier of the interaction to retrieve.
stream boolean (optional) If set to true, the generated content will be streamed incrementally.

*Defaults to: `False`*
last_event_id string (optional) Optional. If set, resumes the interaction stream from the next chunk after the event marked by the event id. Can only be used if \`stream\` is true.
include_input boolean (optional) If set to true, includes the input in the response.

*Defaults to: `False`*
api_version string (optional) Which version of the API to use.

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

### Get Interaction

<iframe src="https:///frame/api/interactions-api_045bea5bcc7023a054bdc4f512005145a41a695219354b1d037457e436ecd2af.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "model": "gemini-3-flash-preview",
  "status": "completed",
  "object": "interaction",
  "created": "2025-11-26T12:25:15Z",
  "updated": "2025-11-26T12:25:15Z",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "I'm doing great, thank you for asking! How can I help you today?"
    }
  ]
}
```

## Deleting an interaction

delete https://generativelanguage.googleapis.com/v1beta/interactions/{id} Deletes the interaction by id.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#deleteInteraction.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#deleteInteraction.response)

### Path / Query Parameters

id string (required) The unique identifier of the interaction to delete.
api_version string (optional) Which version of the API to use.

### Response

If successful, the response is empty.

### Delete Interaction

<iframe src="https:///frame/api/interactions-api_74de8596698afe6a391224244bd26262f9c84aebed9f14c7d8039b8e539de205.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

## Canceling an interaction

post https://generativelanguage.googleapis.com/v1beta/interactions/{id}/cancel Cancels an interaction by id. This only applies to background interactions that are still running.
- [Path / Query parameters](https://ai.google.dev/api/interactions-api#cancelInteractionById.PATH_PARAMETERS)
- [Response](https://ai.google.dev/api/interactions-api#cancelInteractionById.response)

### Path / Query Parameters

id string (required) The unique identifier of the interaction to cancel.
api_version string (optional) Which version of the API to use.

### Response

Returns an [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) resource.

### Cancel Interaction

<iframe src="https:///frame/api/interactions-api_4c59af510bd084c8112b8430b6ae52e2c72a607f500a2122a28d6af02d60caec.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

#### Example Response

```json
{
  "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
  "agent": "deep-research-pro-preview-12-2025",
  "status": "cancelled",
  "object": "interaction",
  "created": "2025-11-26T12:25:15Z",
  "updated": "2025-11-26T12:25:15Z",
  "role": "agent"
}
```

## Resources

### Interaction

The Interaction resource.

#### Fields

model ModelOption (optional) The name of the \`Model\` used for generating the interaction.

Possible
values:

- `gemini-2.5-flash`

  Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.
- `gemini-2.5-flash-image`

  Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.
- `gemini-2.5-flash-lite`

  Our smallest and most cost effective model, built for at scale usage.
- `gemini-2.5-flash-lite-preview-09-2025`

  The latest model based on Gemini 2.5 Flash lite optimized for cost-efficiency, high throughput and high quality.
- `gemini-2.5-flash-native-audio-preview-12-2025`

  Our native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.
- `gemini-2.5-flash-preview-09-2025`

  The latest model based on the 2.5 Flash model. 2.5 Flash Preview is best for large scale processing, low-latency, high volume tasks that require thinking, and agentic use cases.
- `gemini-2.5-flash-preview-tts`

  Our 2.5 Flash text-to-speech model optimized for powerful, low-latency controllable speech generation.
- `gemini-2.5-pro`

  Our state-of-the-art multipurpose model, which excels at coding and complex reasoning tasks.
- `gemini-2.5-pro-preview-tts`

  Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.
- `gemini-3-flash-preview`

  Our most intelligent model built for speed, combining frontier intelligence with superior search and grounding.
- `gemini-3-pro-image-preview`

  State-of-the-art image generation and editing model.
- `gemini-3-pro-preview`

  Our most intelligent model with SOTA reasoning and multimodal understanding, and powerful agentic and vibe coding capabilities.
- `gemini-3.1-pro-preview`

  Our latest SOTA reasoning model with unprecedented depth and nuance, and powerful multimodal understanding and coding capabilities.
- `gemini-3.1-flash-image-preview`

  Pro-level visual intelligence with Flash-speed efficiency and reality-grounded generation capabilities.

The model that will complete your prompt.\\n\\nSee \[models\](https://ai.google.dev/gemini-api/docs/models) for additional details.
agent AgentOption (optional) The name of the \`Agent\` used for generating the interaction.

Possible
values:

- `deep-research-pro-preview-12-2025`

  Gemini Deep Research Agent

The agent to interact with.
id string (optional) Output only. A unique identifier for the interaction completion.
status enum (string) (optional) Output only. The status of the interaction.

Possible
values:

- `in_progress`
- `requires_action`
- `completed`
- `failed`
- `cancelled`
- `incomplete`
created string (optional) Output only. The time at which the response was created in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).
updated string (optional) Output only. The time at which the response was last updated in ISO 8601 format
(YYYY-MM-DDThh:mm:ssZ).
role string (optional) Output only. The role of the interaction.
outputs array ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) (optional) Output only. Responses from the model.
system_instruction string (optional) System instruction for the interaction.
tools array ([Tool](https://ai.google.dev/api/interactions-api#Resource:Tool)) (optional) A list of tool declarations the model may call during interaction.
usage Usage (optional) Output only. Statistics on the interaction request's token usage.
Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional) Number of tokens in the prompt (context).
input_tokens_by_modality ModalityTokens (optional) A breakdown of input token usage by modality.
The token count for a single response modality.

#### Fields

modality ResponseModality (optional) The modality associated with the token count.

Possible
values:

- `text`
- `image`
- `audio`

<br />

tokens integer (optional) Number of tokens for the modality.
total_cached_tokens integer (optional) Number of tokens in the cached part of the prompt (the cached content).
cached_tokens_by_modality ModalityTokens (optional) A breakdown of cached token usage by modality.
The token count for a single response modality.

#### Fields

modality ResponseModality (optional) The modality associated with the token count.

Possible
values:

- `text`
- `image`
- `audio`

<br />

tokens integer (optional) Number of tokens for the modality.
total_output_tokens integer (optional) Total number of tokens across all the generated responses.
output_tokens_by_modality ModalityTokens (optional) A breakdown of output token usage by modality.
The token count for a single response modality.

#### Fields

modality ResponseModality (optional) The modality associated with the token count.

Possible
values:

- `text`
- `image`
- `audio`

<br />

tokens integer (optional) Number of tokens for the modality.
total_tool_use_tokens integer (optional) Number of tokens present in tool-use prompt(s).
tool_use_tokens_by_modality ModalityTokens (optional) A breakdown of tool-use token usage by modality.
The token count for a single response modality.

#### Fields

modality ResponseModality (optional) The modality associated with the token count.

Possible
values:

- `text`
- `image`
- `audio`

<br />

tokens integer (optional) Number of tokens for the modality.
total_thought_tokens integer (optional) Number of tokens of thoughts for thinking models.
total_tokens integer (optional) Total token count for the interaction request (prompt + responses + other
internal tokens).
response_modalities ResponseModality (optional) The requested modalities of the response (TEXT, IMAGE, AUDIO).

Possible
values:

- `text`
- `image`
- `audio`

<br />

response_format object (optional) Enforces that the generated response is a JSON object that complies with
the JSON schema specified in this field.
response_mime_type string (optional) The mime type of the response. This is required if response_format is set.
previous_interaction_id string (optional) The ID of the previous interaction, if any.
input [Content](https://ai.google.dev/api/interactions-api#Resource:Content) or array ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or array ([Turn](https://ai.google.dev/api/interactions-api#Resource:Turn)) or string (optional) The inputs for the interaction.
agent_config object (optional) Configuration for the agent.

#### Possible Types

Polymorphic discriminator: `type`
DynamicAgentConfig Configuration for dynamic agents.
type object (required) No description provided.

Always set to `"dynamic"`.
DeepResearchAgentConfig Configuration for the Deep Research agent.
thinking_summaries ThinkingSummaries (optional) Whether to include thought summaries in the response.

Possible
values:

- `auto`
- `none`

<br />

type object (required) No description provided.

Always set to `"deep-research"`.

### Examples

### Example

```bash
{
  "created": "2025-12-04T15:01:45Z",
  "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
  "model": "gemini-3-flash-preview",
  "object": "interaction",
  "outputs": [
    {
      "text": "Hello! I'm doing well, functioning as expected. Thank you for asking! How are you doing today?",
      "type": "text"
    }
  ],
  "role": "model",
  "status": "completed",
  "updated": "2025-12-04T15:01:45Z",
  "usage": {
    "input_tokens_by_modality": [
      {
        "modality": "text",
        "tokens": 7
      }
    ],
    "total_cached_tokens": 0,
    "total_input_tokens": 7,
    "total_output_tokens": 23,
    "total_thought_tokens": 49,
    "total_tokens": 79,
    "total_tool_use_tokens": 0
  }
}
```

## Data Models

### Content

The content of the response.

### Possible Types

Polymorphic discriminator: `type`
TextContent A text content block.
text string (required) The text content.
annotations Annotation (optional) Citation information for model-generated content.
Citation information for model-generated content.

#### Fields

start_index integer (optional) Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.
end_index integer (optional) End of the attributed segment, exclusive.
source string (optional) Source attributed for a portion of the text. Could be a URL, title, or
other identifier.
type object (required) No description provided.

Always set to `"text"`.
ImageContent An image content block.
data string (optional) The image content.
uri string (optional) The URI of the image.
mime_type enum (string) (optional) The mime type of the image.

Possible
values:

- `image/png`
- `image/jpeg`
- `image/webp`
- `image/heic`
- `image/heif`
resolution MediaResolution (optional) The resolution of the media.

Possible
values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

type object (required) No description provided.

Always set to `"image"`.
AudioContent An audio content block.
data string (optional) The audio content.
uri string (optional) The URI of the audio.
mime_type enum (string) (optional) The mime type of the audio.

Possible
values:

- `audio/wav`
- `audio/mp3`
- `audio/aiff`
- `audio/aac`
- `audio/ogg`
- `audio/flac`
type object (required) No description provided.

Always set to `"audio"`.
DocumentContent A document content block.
data string (optional) The document content.
uri string (optional) The URI of the document.
mime_type enum (string) (optional) The mime type of the document.

Possible
values:

- `application/pdf`
type object (required) No description provided.

Always set to `"document"`.
VideoContent A video content block.
data string (optional) The video content.
uri string (optional) The URI of the video.
mime_type enum (string) (optional) The mime type of the video.

Possible
values:

- `video/mp4`
- `video/mpeg`
- `video/mpg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/webm`
- `video/wmv`
- `video/3gpp`
resolution MediaResolution (optional) The resolution of the media.

Possible
values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

type object (required) No description provided.

Always set to `"video"`.
ThoughtContent A thought content block.
signature string (optional) Signature to match the backend source to be part of the generation.
summary ThoughtSummary (optional) A summary of the thought.
A summary of the thought.
type object (required) No description provided.

Always set to `"thought"`.
FunctionCallContent A function tool call content block.
name string (required) The name of the tool to call.
arguments object (required) The arguments to pass to the function.
type object (required) No description provided.

Always set to `"function_call"`.
id string (required) A unique ID for this specific tool call.
FunctionResultContent A function tool result content block.
name string (optional) The name of the tool that was called.
is_error boolean (optional) Whether the tool call resulted in an error.
type object (required) No description provided.

Always set to `"function_result"`.
result object or string (required) The result of the tool call.
call_id string (required) ID to match the ID from the function call block.
CodeExecutionCallContent Code execution content.
arguments CodeExecutionCallArguments (required) The arguments to pass to the code execution.
The arguments to pass to the code execution.

#### Fields

language enum (string) (optional) Programming language of the \`code\`.

Possible
values:

- `python`
code string (optional) The code to be executed.
type object (required) No description provided.

Always set to `"code_execution_call"`.
id string (required) A unique ID for this specific tool call.
CodeExecutionResultContent Code execution result content.
result string (required) The output of the code execution.
is_error boolean (optional) Whether the code execution resulted in an error.
signature string (optional) A signature hash for backend validation.
type object (required) No description provided.

Always set to `"code_execution_result"`.
call_id string (required) ID to match the ID from the code execution call block.
UrlContextCallContent URL context content.
arguments UrlContextCallArguments (required) The arguments to pass to the URL context.
The arguments to pass to the URL context.

#### Fields

urls array (string) (optional) The URLs to fetch.
type object (required) No description provided.

Always set to `"url_context_call"`.
id string (required) A unique ID for this specific tool call.
UrlContextResultContent URL context result content.
signature string (optional) The signature of the URL context result.
result UrlContextResult (required) The results of the URL context.
The result of the URL context.

#### Fields

url string (optional) The URL that was fetched.
status enum (string) (optional) The status of the URL retrieval.

Possible
values:

- `success`
- `error`
- `paywall`
- `unsafe`
is_error boolean (optional) Whether the URL context resulted in an error.
type object (required) No description provided.

Always set to `"url_context_result"`.
call_id string (required) ID to match the ID from the url context call block.
GoogleSearchCallContent Google Search content.
arguments GoogleSearchCallArguments (required) The arguments to pass to Google Search.
The arguments to pass to Google Search.

#### Fields

queries array (string) (optional) Web search queries for the following-up web search.
search_type enum (string) (optional) The type of search grounding enabled.

Possible
values:

- `web_search`
- `image_search`
type object (required) No description provided.

Always set to `"google_search_call"`.
id string (required) A unique ID for this specific tool call.
GoogleSearchResultContent Google Search result content.
signature string (optional) The signature of the Google Search result.
result GoogleSearchResult (required) The results of the Google Search.
The result of the Google Search.

#### Fields

url string (optional) URI reference of the search result.
title string (optional) Title of the search result.
rendered_content string (optional) Web content snippet that can be embedded in a web page or an app webview.
is_error boolean (optional) Whether the Google Search resulted in an error.
type object (required) No description provided.

Always set to `"google_search_result"`.
call_id string (required) ID to match the ID from the google search call block.
McpServerToolCallContent MCPServer tool call content.
name string (required) The name of the tool which was called.
server_name string (required) The name of the used MCP server.
arguments object (required) The JSON object of arguments for the function.
type object (required) No description provided.

Always set to `"mcp_server_tool_call"`.
id string (required) A unique ID for this specific tool call.
McpServerToolResultContent MCPServer tool result content.
name string (optional) Name of the tool which is called for this specific tool call.
server_name string (optional) The name of the used MCP server.
type object (required) No description provided.

Always set to `"mcp_server_tool_result"`.
result object or string (required) The result of the tool call.
call_id string (required) ID to match the ID from the MCP server tool call block.
FileSearchCallContent File Search content.
type object (required) No description provided.

Always set to `"file_search_call"`.
id string (required) A unique ID for this specific tool call.
FileSearchResultContent File Search result content.
result FileSearchResult (optional) The results of the File Search.
The result of the File Search.

#### Fields

title string (optional) The title of the search result.
text string (optional) The text of the search result.
file_search_store string (optional) The name of the file search store.
type object (required) No description provided.

Always set to `"file_search_result"`.
call_id string (required) ID to match the ID from the file search call block.

### Examples

### Text

```json
{
  "type": "text",
  "text": "Hello, how are you?"
}
```

### Image

```json
{
  "type": "image",
  "data": "BASE64_ENCODED_IMAGE",
  "mime_type": "image/png"
}
```

### Audio

```json
{
  "type": "audio",
  "data": "BASE64_ENCODED_AUDIO",
  "mime_type": "audio/wav"
}
```

### Document

```json
{
  "type": "document",
  "data": "BASE64_ENCODED_DOCUMENT",
  "mime_type": "application/pdf"
}
```

### Video

```json
{
  "type": "video",
  "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
}
```

### Thought

```json
{
  "type": "thought",
  "summary": [
    {
      "type": "text",
      "text": "The user is asking about the weather. I should use the get_weather tool."
    }
  ],
  "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0+19xcLsGG46bd8wjkF/6RNlRUdvHrXyjsHkG0BZFcuO/bPOyA6Xh5jANNgx82wPHjGExN8A4ZQn56FlMwyZoqFVQz0QyY1lfibFJ2zU3J87uw26OewzcuVX0KEcs+GIsZa3EA6WwqhbsOd3wtZB3Ua2Qf98VAWZTS5y/tWpql7jnU3/CU7pouxQr/Bwft3hwnJNesQ9/dDJTuaQ8Zprh9VRWf1aFFjpIueOjBRrlT3oW6/y/eRl/Gt9BQXCYTqg/38vHFUU4Wo/d9dUpvfCe/a3o97t2Jgxp34oFKcsVb4S5WJrykIkw+14DzVnTpCpbQNFckqvFLuqnJCkL0EQFtunBXI03FJpPu3T1XU6id8S7ojoJQZSauGUCgmaLqUGdMrd08oo81ecoJSLs51Re9N/lISGmjWFPGpqJLoGq6uo4FHz58hmeyXCgHG742BHz2P3MiH1CXHUT2J8mF6zLhf3SR9Qb3lkrobAh"
}
```

### Function Call

```json
{
  "type": "function_call",
  "name": "get_weather",
  "id": "gth23981",
  "arguments": {
    "location": "Boston, MA"
  }
}
```

### Function Result

```json
{
  "type": "function_result",
  "name": "get_weather",
  "call_id": "gth23981",
  "result": [
    {
      "type": "text",
      "text": "{\"weather\":\"sunny\"}"
    }
  ]
}
```

### Code Execution Call

```json
{
  "type": "code_execution_call",
  "id": "call_123456",
  "arguments": {
    "language": "python",
    "code": "print('hello world')"
  }
}
```

### Code Execution Result

```json
{
  "type": "code_execution_result",
  "call_id": "call_123456",
  "result": "hello world"
}
```

### Url Context Call

```json
{
  "type": "url_context_call",
  "id": "call_123456",
  "arguments": {
    "urls": [
      "https://www.example.com"
    ]
  }
}
```

### Url Context Result

```json
{
  "type": "url_context_result",
  "call_id": "call_123456",
  "result": [
    {
      "url": "https://www.example.com",
      "status": "SUCCESS"
    }
  ]
}
```

### Google Search Call

```json
{
  "type": "google_search_call",
  "id": "call_123456",
  "arguments": {
    "queries": [
      "weather in Boston"
    ]
  }
}
```

### Google Search Result

```json
{
  "type": "google_search_result",
  "call_id": "call_123456",
  "result": [
    {
      "url": "https://www.google.com/search?q=weather+in+Boston",
      "title": "Weather in Boston"
    }
  ]
}
```

### Mcp Server Tool Call

```json
{
  "type": "mcp_server_tool_call",
  "id": "call_123456",
  "name": "get_forecast",
  "server_name": "weather_server",
  "arguments": {
    "city": "London"
  }
}
```

### Mcp Server Tool Result

```json
{
  "type": "mcp_server_tool_result",
  "name": "get_forecast",
  "server_name": "weather_server",
  "call_id": "call_123456",
  "result": "sunny"
}
```

### File Search Call

```json
{
  "type": "file_search_call",
  "id": "call_123456"
}
```

### File Search Result

```json
{
  "type": "file_search_result",
  "call_id": "call_123456",
  "result": [
    {
      "text": "search result chunk",
      "file_search_store": "file_search_store"
    }
  ]
}
```

### Tool

<br />

### Possible Types

Polymorphic discriminator: `type`
Function A tool that can be used by the model.
name string (optional) The name of the function.
description string (optional) A description of the function.
parameters object (optional) The JSON Schema for the function's parameters.
type string (required) No description provided.

Always set to `"function"`.
GoogleSearch A tool that can be used by the model to search Google.
search_types array (enum (string)) (optional) The types of search grounding to enable.

Possible
values:

- `web_search`
- `image_search`
type string (required) No description provided.

Always set to `"google_search"`.
CodeExecution A tool that can be used by the model to execute code.
type string (required) No description provided.

Always set to `"code_execution"`.
UrlContext A tool that can be used by the model to fetch URL context.
type string (required) No description provided.

Always set to `"url_context"`.
ComputerUse A tool that can be used by the model to interact with the computer.
environment enum (string) (optional) The environment being operated.

Possible
values:

- `browser`
excludedPredefinedFunctions array (string) (optional) The list of predefined functions that are excluded from the model call.
type string (required) No description provided.

Always set to `"computer_use"`.
McpServer A MCPServer is a server that can be called by the model to perform actions.
name string (optional) The name of the MCPServer.
url string (optional) The full URL for the MCPServer endpoint.
Example: "https://api.example.com/mcp"
headers object (optional) Optional: Fields for authentication headers, timeouts, etc., if needed.
allowed_tools AllowedTools (optional) The allowed tools.
The configuration for allowed tools.

#### Fields

mode ToolChoiceType (optional) The mode of the tool choice.

Possible
values:

- `auto`
- `any`
- `none`
- `validated`

<br />

tools array (string) (optional) The names of the allowed tools.
type string (required) No description provided.

Always set to `"mcp_server"`.
FileSearch A tool that can be used by the model to search files.
file_search_store_names array (string) (optional) The file search store names to search.
top_k integer (optional) The number of semantic retrieval chunks to retrieve.
metadata_filter string (optional) Metadata filter to apply to the semantic retrieval documents and chunks.
type string (required) No description provided.

Always set to `"file_search"`.

### Examples

### Function

<iframe src="https:///frame/api/interactions-api_4a5dbf9d620c02ac91fab9a81c18bbf757b789ac1aacdbdd1344543526285116.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### GoogleSearch

<iframe src="https:///frame/api/interactions-api_f8479aebdefc679bc0aa879da69b36359eeeecc8fa0aa2ade58c197fff9b0c4f.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### CodeExecution

<iframe src="https:///frame/api/interactions-api_158cbd536bcb164757d0d89985a1c5e88412987a9c90e39ccbb2d56bef005f02.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### UrlContext

<iframe src="https:///frame/api/interactions-api_c0dfd9bd68ce4844e89374cfb79942ea89e41b3ff4ef23313559319d0ad25db1.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### ComputerUse

<iframe src="https:///frame/api/interactions-api_b44384e3558525bfc57333193c99e2d38675e9a63c4a68f6dae6b8f3fd0bafde.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### McpServer

<iframe src="https:///frame/api/interactions-api_458a224ebb45f79cb7c7419d5075f46e288873a007f8e82b3227e8d4d0271f7d.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### FileSearch

<iframe src="https:///frame/api/interactions-api_bd9a26cfd12cf81a76c60572e19b2f395c33d0d45d640ee92106e6f73a63f36a.frame" class="framebox inherit-locale " allow="clipboard-write https://" allowfullscreen is-upgraded></iframe>

### Turn

<br />

#### Fields

role string (optional) The originator of this turn. Must be user for input or model for
model output.
content array ([Content](https://ai.google.dev/api/interactions-api#Resource:Content)) or string (optional) The content of the turn.

### Examples

### User Turn

```bash
{
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": "user turn"
    }
  ]
}
```

### Model Turn

```bash
{
  "role": "model",
  "content": [
    {
      "type": "text",
      "text": "model turn"
    }
  ]
}
```

### InteractionSseEvent

<br />

### Possible Types

Polymorphic discriminator: `event_type`
InteractionStartEvent <br />

interaction [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) (required) No description provided.
event_type enum (string) (required) No description provided.

Possible
values:

- `interaction.start`
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
InteractionCompleteEvent <br />

interaction [Interaction](https://ai.google.dev/api/interactions-api#Resource:Interaction) (required) The completed interaction with empty outputs to reduce the payload size.
Use the preceding ContentDelta events for the actual output.
event_type enum (string) (required) No description provided.

Possible
values:

- `interaction.complete`
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
InteractionStatusUpdate <br />

interaction_id string (required) No description provided.
status enum (string) (required) No description provided.

Possible
values:

- `in_progress`
- `requires_action`
- `completed`
- `failed`
- `cancelled`
- `incomplete`
event_type string (required) No description provided.

Always set to `"interaction.status_update"`.
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
ContentStart <br />

index integer (required) No description provided.
content [Content](https://ai.google.dev/api/interactions-api#Resource:Content) (required) No description provided.
event_type string (required) No description provided.

Always set to `"content.start"`.
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
ContentDelta <br />

index integer (required) No description provided.
event_type string (required) No description provided.

Always set to `"content.delta"`.
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
delta object (required) No description provided.

#### Possible Types

Polymorphic discriminator: `type`
TextDelta <br />

text string (required) No description provided.
annotations Annotation (optional) Citation information for model-generated content.
Citation information for model-generated content.

#### Fields

start_index integer (optional) Start of segment of the response that is attributed to this source.

Index indicates the start of the segment, measured in bytes.
end_index integer (optional) End of the attributed segment, exclusive.
source string (optional) Source attributed for a portion of the text. Could be a URL, title, or
other identifier.
type object (required) No description provided.

Always set to `"text"`.
ImageDelta <br />

data string (optional) No description provided.
uri string (optional) No description provided.
mime_type enum (string) (optional) No description provided.

Possible
values:

- `image/png`
- `image/jpeg`
- `image/webp`
- `image/heic`
- `image/heif`
resolution MediaResolution (optional) The resolution of the media.

Possible
values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

type object (required) No description provided.

Always set to `"image"`.
AudioDelta <br />

data string (optional) No description provided.
uri string (optional) No description provided.
mime_type enum (string) (optional) No description provided.

Possible
values:

- `audio/wav`
- `audio/mp3`
- `audio/aiff`
- `audio/aac`
- `audio/ogg`
- `audio/flac`
type object (required) No description provided.

Always set to `"audio"`.
DocumentDelta <br />

data string (optional) No description provided.
uri string (optional) No description provided.
mime_type enum (string) (optional) No description provided.

Possible
values:

- `application/pdf`
type object (required) No description provided.

Always set to `"document"`.
VideoDelta <br />

data string (optional) No description provided.
uri string (optional) No description provided.
mime_type enum (string) (optional) No description provided.

Possible
values:

- `video/mp4`
- `video/mpeg`
- `video/mpg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/webm`
- `video/wmv`
- `video/3gpp`
resolution MediaResolution (optional) The resolution of the media.

Possible
values:

- `low`
- `medium`
- `high`
- `ultra_high`

<br />

type object (required) No description provided.

Always set to `"video"`.
ThoughtSummaryDelta <br />

type object (required) No description provided.

Always set to `"thought_summary"`.
content [ImageContent](https://ai.google.dev/api/interactions-api#Resource:ImageContent) or [TextContent](https://ai.google.dev/api/interactions-api#Resource:TextContent) (optional) No description provided.
ThoughtSignatureDelta <br />

signature string (optional) Signature to match the backend source to be part of the generation.
type object (required) No description provided.

Always set to `"thought_signature"`.
FunctionCallDelta <br />

name string (required) No description provided.
arguments object (required) No description provided.
type object (required) No description provided.

Always set to `"function_call"`.
id string (required) A unique ID for this specific tool call.
FunctionResultDelta <br />

name string (optional) No description provided.
is_error boolean (optional) No description provided.
type object (required) No description provided.

Always set to `"function_result"`.
result object or string (required) Tool call result delta.
call_id string (required) ID to match the ID from the function call block.
CodeExecutionCallDelta <br />

arguments CodeExecutionCallArguments (required) No description provided.
The arguments to pass to the code execution.

#### Fields

language enum (string) (optional) Programming language of the \`code\`.

Possible
values:

- `python`
code string (optional) The code to be executed.
type object (required) No description provided.

Always set to `"code_execution_call"`.
id string (required) A unique ID for this specific tool call.
CodeExecutionResultDelta <br />

result string (required) No description provided.
is_error boolean (optional) No description provided.
signature string (optional) No description provided.
type object (required) No description provided.

Always set to `"code_execution_result"`.
call_id string (required) ID to match the ID from the function call block.
UrlContextCallDelta <br />

arguments UrlContextCallArguments (required) No description provided.
The arguments to pass to the URL context.

#### Fields

urls array (string) (optional) The URLs to fetch.
type object (required) No description provided.

Always set to `"url_context_call"`.
id string (required) A unique ID for this specific tool call.
UrlContextResultDelta <br />

signature string (optional) No description provided.
result UrlContextResult (required) No description provided.
The result of the URL context.

#### Fields

url string (optional) The URL that was fetched.
status enum (string) (optional) The status of the URL retrieval.

Possible
values:

- `success`
- `error`
- `paywall`
- `unsafe`
is_error boolean (optional) No description provided.
type object (required) No description provided.

Always set to `"url_context_result"`.
call_id string (required) ID to match the ID from the function call block.
GoogleSearchCallDelta <br />

arguments GoogleSearchCallArguments (required) No description provided.
The arguments to pass to Google Search.

#### Fields

queries array (string) (optional) Web search queries for the following-up web search.
type object (required) No description provided.

Always set to `"google_search_call"`.
id string (required) A unique ID for this specific tool call.
GoogleSearchResultDelta <br />

signature string (optional) No description provided.
result GoogleSearchResult (required) No description provided.
The result of the Google Search.

#### Fields

url string (optional) URI reference of the search result.
title string (optional) Title of the search result.
rendered_content string (optional) Web content snippet that can be embedded in a web page or an app webview.
is_error boolean (optional) No description provided.
type object (required) No description provided.

Always set to `"google_search_result"`.
call_id string (required) ID to match the ID from the function call block.
McpServerToolCallDelta <br />

name string (required) No description provided.
server_name string (required) No description provided.
arguments object (required) No description provided.
type object (required) No description provided.

Always set to `"mcp_server_tool_call"`.
id string (required) A unique ID for this specific tool call.
McpServerToolResultDelta <br />

name string (optional) No description provided.
server_name string (optional) No description provided.
type object (required) No description provided.

Always set to `"mcp_server_tool_result"`.
result object or string (required) Tool call result delta.
call_id string (required) ID to match the ID from the function call block.
FileSearchCallDelta <br />

type object (required) No description provided.

Always set to `"file_search_call"`.
id string (required) A unique ID for this specific tool call.
FileSearchResultDelta <br />

result FileSearchResult (optional) No description provided.
The result of the File Search.

#### Fields

title string (optional) The title of the search result.
text string (optional) The text of the search result.
file_search_store string (optional) The name of the file search store.
type object (required) No description provided.

Always set to `"file_search_result"`.
ContentStop <br />

index integer (required) No description provided.
event_type string (required) No description provided.

Always set to `"content.stop"`.
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.
ErrorEvent <br />

error Error (optional) No description provided.
Error message from an interaction.

#### Fields

code string (optional) A URI that identifies the error type.
message string (optional) A human-readable error message.
event_type string (required) No description provided.

Always set to `"error"`.
event_id string (optional) The event_id token to be used to resume the interaction stream, from this event.

### Examples

### Interaction Start

```json
{
  "event_type": "interaction.start",
  "interaction": {
    "id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
    "model": "gemini-3-flash-preview",
    "object": "interaction",
    "status": "in_progress"
  }
}
```

### Interaction Complete

```json
{
  "event_type": "interaction.complete",
  "interaction": {
    "created": "2025-12-09T18:45:40Z",
    "id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
    "model": "gemini-3-flash-preview",
    "object": "interaction",
    "role": "model",
    "status": "completed",
    "updated": "2025-12-09T18:45:40Z",
    "usage": {
      "input_tokens_by_modality": [
        {
          "modality": "text",
          "tokens": 11
        }
      ],
      "total_cached_tokens": 0,
      "total_input_tokens": 11,
      "total_output_tokens": 364,
      "total_thought_tokens": 1120,
      "total_tokens": 1495,
      "total_tool_use_tokens": 0
    }
  }
}
```

### Interaction Status Update

```json
{
  "event_type": "interaction.status_update",
  "interaction_id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
  "status": "in_progress"
}
```

### Content Start

```json
{
  "event_type": "content.start",
  "content": {
    "type": "text"
  },
  "index": 1
}
```

### Content Delta

```json
{
  "event_type": "content.delta",
  "delta": {
    "type": "text",
    "text": "Elara\u2019s life was a symphony of quiet moments. A librarian, she found solace in the hushed aisles, the scent of aged paper, and the predictable rhythm of her days. Her small apartment, meticulously ordered, reflected this internal calm, save"
  },
  "index": 1
}
```

### Content Stop

```json
{
  "event_type": "content.stop",
  "index": 1
}
```

### Error Event

```json
{
  "event_type": "error",
  "error": {
    "message": "Failed to get completed interaction: Result not found.",
    "code": "not_found"
  }
}
```
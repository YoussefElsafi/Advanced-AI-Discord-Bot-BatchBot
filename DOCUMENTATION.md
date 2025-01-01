# Batchbot Documentation

This document provides a comprehensive overview of Batchbot, a Discord bot powered by Google Gemini and designed for interactive conversations, information retrieval, and various utility functions.

## Setup and Configuration

1. **Install Required Libraries:**

   pip install -r requirements.txt

2. **Obtain API Keys:**
   - **Discord Bot Token:** Create a Discord application and bot on the Discord Developer Portal and obtain the bot token.
   - **Google Gemini API Key:** Acquire an API key for Google Gemini.
   - **Hugging Face API Key (Optional):** Obtain an API key from Hugging Face to enable image generation features.

3. **Configure `config.py`:**
   - Replace `YOUR_DISCORD_BOT_TOKEN`, `YOUR_GEMINI_API_KEY`, and `YOUR_HUGGING_FACE_API_KEY` with your obtained API keys.
   - Customize `NAME` and `server_name` as desired.
   - Select the Default Gemini model using the `gemini_model` variable with the options:
   
   **(Flash: Gemini 1.5 Flash | 2.0-Flash: Gemini 2.0 Flash (Experimental) | Pro: Gemini 1.5 Pro | Flash-8B: Gemini 1.5 Flash 8B | Flash-002: Gemini 1.5 Flash 002 | Pro-002: Gemini 1.5 Pro 002 | Flash-Latest: Gemini 1.5 Flash Latest | Pro-Latest: Gemini 1.5 Pro Latest | Exp-1114: Gemini Experimental 1114 | Exp-1121: Gemini Experimental 1121 | Exp-1206: Gemini Experimental 1206)**.
   
   *Tip: (You can change the model while the bot is running using the `/model` command but it will not change the Default model)*
   - (Optional) Configure `Image_Generator_Model` to use a different image generation model from Hugging Face.

## Configuration Settings

The `system/config.py` file contains all configurable parameters for the AI bot. These settings allow for fine-grained control over the bot's functionality, performance, and safety features.

<details>
<summary><strong>Detailed Configuration Options (Click to Expand)</strong></summary>

- **`gemini_model`**: Specifies the default Gemini model used by the bot. Different models offer varying capabilities and performance characteristics. Model selection can also be performed at runtime using the `/model` command.
   <details>
   <summary><strong>Supported Models (Click to Expand)</strong></summary>
   
   ### Gemini Flash Models
   - **`Flash`:** Gemini 1.5 Flash.
   - **`Flash-Latest`:** Gemini 1.5 Flash Latest.
   - **`Flash-8B`:** Gemini 1.5 Flash 8B.

   ### Gemini Pro Models
   - **`Pro`:** Gemini 1.5 Pro.
   - **`Pro-Latest`:** Gemini 1.5 Pro Latest.
   - **`Pro-002`:** Gemini 1.5 Pro 002.

   ### Google LearnLM (Accessible via `/model` command)
   - **`LeanLM`:** LearnLM 1.5 Pro Experimental.
   
   ### Experimental Models
   - **`Exp-1114`:** Gemini Experimental 1114.
   - **`Exp-1121`:** Gemini Experimental 1121.
   - **`Exp-1206`:** Gemini Experimental 1206.
   </details>

- **`model_temperature`** `(Default: 1)`: Controls the randomness and creativity of the model's responses. Higher values (up to 2) increase creativity but may lead to less coherent outputs. Lower values result in more predictable and factual responses.

- **`limit_history`** `(Default: True)`: Enables a limited conversation history to maintain optimal performance and stability.

- **`history_limit`** `(Default: 100)`: Defines the maximum number of conversation turns stored in the history when `limit_history` is enabled.

- **`show_time`** `(Default: False)`: When enabled, the bot incorporates timestamps and response time information into its interactions. This may impact performance.

- **`history_channel_toggle`** `(Default: True)`: Restricts conversation history to a per-channel basis. This enhances performance and improves contextual awareness within individual channels.

- **`embed_colors`** `(Default: 0x00ff00)`: Specifies the hexadecimal color code used for message embeds.

- **`show_tokens_at_startup`** `(Default: False)`: Displays API keys and token information on the console during startup. It is recommended to keep this disabled for security purposes.

- **`safe_search`** `(Default: True)`: Enforces safe search filtering for web queries, promoting a safer user experience.

- **`ffmpeg_executable_path`**:  Provides the file path to the `ffmpeg` executable, which is required for voice-related functionalities.

- **`tts`** `(Default: True)`: Enables text-to-speech functionality in voice channels, allowing the bot to vocalize its responses.

- **`vc_voice`** `(Default: 1)`: Sets the default voice for voice channel interactions. The default value of `1` corresponds to `en-US-BrianNeural`. Voice selection can be adjusted using the `/vc voice [voice_number]` command.

- **`sync_voice_with_text`** `(Default: True)`: Synchronizes text and voice output in voice channels. This may introduce latency depending on network conditions.

- **`HISTORY_FILE`** `(Default: 'system/data/data.json')`: Defines the file path for storing conversation history data.

- **`preview_code_output`** `(Default: True)`: Enables the Gemini feature that predicts the output of code snippets.

- **`safegen`** `(Default: True)`: Activates content filtering for image generation, preventing the creation of inappropriate or harmful images.

- **`create_mod_channel`** `(Default: False)`: Automatically creates a moderation channel when inappropriate content is detected. Requires `safegen` to be enabled.

- **`mod_channel_name`** `(Default: '🔧・mod')`: Specifies the name of the automatically generated moderation channel.

- **`additional_details`** `(Default: False)`: Includes supplementary information about images, media, and files in the bot's responses, similar to previous versions (v1.0.0, v1.5.0, v2.0, v2.1). This may impact response times.
-  **`discord_heartbeat_timeout`** `(Default: 60)`: Adjusts the Discord heartbeat timeout in seconds. Increase this value if the bot experiences frequent disconnections due to timeouts.
- **`show_tokens`** `(Default: False)`:  Displays input and output token counts. Primarily used for debugging.
-  **`add_watermark_to_generated_image`** `(Default: False)`: Applies a watermark to generated images. The watermark image is located at `system/assets/watermark.png`.
- **`show_safety_settings_on_startup`** `(Default: False)`:  Displays the configured safety settings when the bot starts.
- **`cool_personality`** `(Default: False)`: Modifies the bot's conversational style to adopt a "cooler" persona.
    <details>
   <summary>Personality Options (Click to Expand)</summary>
        
   - **`False`:** Disables the alternate personality.
   - **`True`:** Enables a basic level of the alternate personality.
   - **`Super`:**  Applies a more pronounced version of the alternate personality.
   - **`Ultimate`:**  Enables the most prominent version of the alternate personality.
   </details>
- **`Image_Generator_Model`** `(Default: "stabilityai/stable-diffusion-xl-base-1.0")`: Specifies the model used for image generation. Changing this setting may require reinviting the bot.
- **`DEFAULT_MUSIC_MODEL`** `(Default: "facebook/musicgen-small")`:  Determines the model used for music generation. Bot re-invitation might be necessary after modification.
- **`Object_Detection_Model`** `(Default: "facebook/detr-resnet-50")`: Sets the model used for object detection tasks.
- **`Dangerous`, `Harassment`, `Hate_Speech`, `Sexually_Explicit`, `Dangerous_Content`**: These parameters control the safety filtering thresholds for different categories of harmful content.
   <details>
   <summary>Safety Level Options (Click to Expand)</summary>

   - **`Default`:**  Uses the default safety filtering settings.
   - **`None`:** Disables safety filtering for the specified category.
   - **`Low`:**  Filters only high-risk content.
   - **`Moderate`:** Filters medium and high-risk content.
   - **`High`:**  Filters low, medium, and high-risk content.
   </details>
</details>

<details>
<summary><strong>Experimental Settings (Click to Expand)</strong></summary>

- **`vc_AI`** `(Default: False)`: Enables experimental voice assistant features, allowing the bot to process and respond to voice input in voice channels. This feature is currently under development.
-  **`show_invite_link_on_startup`** `(Default: False)`: Displays the bot's invitation link upon startup.
- **`smart_recognition`** `(Default: False)`:  An experimental feature that attempts to improve the bot's ability to distinguish between different users in a conversation.
-  **`fix_repeating_prompts`** `(Default: True)`: Implements measures to mitigate issues with repetitive or broken responses. This is an experimental feature.
</details>

## Usage

### Basic Commands

- `/ai [Prompt]`: Initiate a conversation with Batchbot using the provided prompt.
- `/search [Query]`: Perform a web search using Google Search API and provide a summarized response. **(Requires Google Custom Search API & Project Search Engine ID)**
- `/search*yt [Query]`: Perform a YouTube search using Google Search API and provide a summarized response. **(Requires Google Custom Search API & Project Search Engine ID)**
- `/img [Prompt]`: Generate an image based on the provided prompt. **(Requires Hugging Face API key)**
- `/music [Prompt]`: Generate Music based on the provided prompt. **(Requires Hugging Face API key)**

### Additional Commands

- `/aitoggle [on/off]`: Enable or disable automatic AI responses.
- `/say [Message] [channel_name(optional)]`: Make the bot say the specified message.
- `/reset`: Clear the bot's memory of past conversations.
- `/profile [Member]`: Display information about the specified member (or yourself if no member is specified).
- `/serverinfo`: Display information about the current server.
- `/joke`: Tell a random joke.
- `/search_save [Query]`: Perform a web search and save the results.
- `/search_img [Query] [Number of Images]`: Search for images and display the specified number.

## Image Generation

Batchbot can generate images using various models from Hugging Face. You can select the desired model using the `/img` command with the `model` option. For example:

- `/img [Prompt] model: Stable Diffusion XL Base 1.0`

## Voice Chat (Experimental)

- `/vc join [Channel Name]`: Join the specified voice channel.
- `/vc leave`: Leave the current voice channel.
- `/vc voice [voice_number]`: Change Bot's Voice.
- `/vc replay`: Replay what the bot said.
- `/vc status`: Check if the bot is in a voice channel or not.

## Reporting Issues and Providing Feedback

Note: That the `/report` and `/feedback` does not send us the report or the feedback, It only gets stored in `system/data/feedback.txt` & `system/data/reports.txt`.

- `/report [Report]`: Report bugs or issues with the bot.
- `/feedback [Feedback]`: Provide feedback or suggestions for improvement.

## Additional Notes

- Batchbot's behavior and responses are influenced by the configured Gemini model's training data & the configured system instructions, You can edit the system instructions in `system/instructions`.
- The bot's memory is persistent and will be retained across sessions.
- Be mindful of the information you share with the bot, as it may be used at google for model improvement purposes.

This documentation provides a general overview of Batchbot's features and functionality. For more detailed information, refer to the bot's source code and the Google Gemini documentation.

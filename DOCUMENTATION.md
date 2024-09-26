# BatchBot Documentation: Your Comprehensive Guide

This document provides an in-depth guide to BatchBot, a powerful Discord bot driven by Google Gemini and enhanced with Hugging Face models. BatchBot is designed for interactive conversations, efficient information retrieval, creative content generation, and a range of utility functions.  This documentation covers everything from setup and configuration to detailed command usage, limitations, and troubleshooting.

---

## I. Setting Up BatchBot: A Step-by-Step Guide

### 1. Installing the Necessary Libraries: Preparing the Foundation

Before you can unleash BatchBot's potential, you need to install the required Python libraries. These libraries provide the essential tools for interacting with Discord, Google Gemini, Hugging Face, and other services.  Open your terminal or command prompt and execute the following command:

```bash
pip install -r requirements.txt
```

**Explanation of Key Libraries:**

* **`discord.py`:**  The core library for interacting with the Discord API. It allows BatchBot to send and receive messages, manage channels, and interact with users.
* **`google-generativeai`:**  Provides access to Google's Gemini API, the brain behind BatchBot's advanced AI capabilities.
* **`requests`:**  A versatile library for making HTTP requests, used for communicating with various web services.
* **`Pillow (PIL)`:**  A powerful image processing library, essential for handling and manipulating images.
* **`colorama`:**  Adds color to your terminal output, making logs and debugging information more readable.
* **`asyncio`:**  Enables asynchronous programming, crucial for handling multiple tasks concurrently.
* **`logging`:**  Provides tools for logging events and debugging information, helpful for troubleshooting and monitoring BatchBot's activity.
* **`duckduckgo-search`:**  A library for interacting with the DuckDuckGo search engine, used for web and YouTube searches.
* **`httpx`:** A modern HTTP client, providing a more efficient and user-friendly way to make HTTP requests.
* **`docx`, `markdown`, `openpyxl`, `python-pptx`:** These libraries enable BatchBot to process various file formats, including Word documents (docx), Markdown files, Excel spreadsheets (xlsx), and PowerPoint presentations (pptx).
* **`youtube-transcript-api`:**  Allows BatchBot to retrieve transcripts from YouTube videos.
* **`fitz`:** A library for working with PDF files. (Alternative to PyPDF2 for improved compatibility)
* **`edge-tts`:**  Microsoft Edge Text-to-Speech library, used for the voice chat features.


### 2. Obtaining Your API Keys: Unlocking BatchBot's Power

BatchBot relies on several API keys to access external services. You'll need to obtain these keys before running the bot.

* **Discord Bot Token:**
    1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    2. Create a new application.
    3. Add a bot to your application.
    4. Copy the bot token. **Keep this token secret and secure!**

* **Google Gemini API Key:**
    1. Navigate to the [Google AI Studio](https://aistudio.google.com/app/apikey) and obtain your Gemini API key. **Keep this key secret and secure!**

* **Hugging Face API Key (Optional, but Recommended):**
    1. Visit [Hugging Face](https://huggingface.co/settings/tokens) and create an API key. This enables image generation and object detection features.  **Keep this key secret and secure!**


### 3. Configuring `config.py`: Tailoring BatchBot to Your Needs

The `system/config.py` file is the control center for BatchBot's settings. Here you'll input your API keys, customize the bot's name, select AI models, and adjust various other parameters.

```python
# config.py

# Essential Keys (KEEP THESE SECRET!)
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Your Discord bot token
API_KEY = "YOUR_GEMINI_API_KEY"  # Your Google Gemini API key
HUGGING_FACE_API = "YOUR_HUGGING_FACE_API_KEY" # Your Hugging Face API key

# Bot Identity
NAME = "BatchBot"  # Bot's name (can be customized)
server_name = "YOUR_SERVER_NAME" # Your Discord server's name

# AI Settings
ai_toggle = True  # Automatic AI responses (True/False)
pro = False       # Gemini model (True: Pro, "True+": Pro Advanced, False: Flash)
limit_history = False  # Limit conversation history (True/False)
history_limit = 100    # Maximum history length (if limit_history is True)
fix_repeating_prompts = True # Helps prevent repeating responses (True/False)
safe_search = 'On' # Safe search for web searches (On/Off)


# Model Settings
Image_Generator_Model = "stabilityai/stable-diffusion-xl-base-1.0"  # Default image generation model
DEFAULT_MUSIC_MODEL = "facebook/musicgen-small"  # Default music generation model
Object_Detection_Model = "facebook/detr-resnet-50" # Object detection model
custom_model = False  # Use a custom Gemini model (True/False)
custom_model_name = "gemini-1.5-flash" # Custom model name (if custom_model is True)
custom_model_tokens = 1048576 # Custom model max tokens (if custom_model is True)

# ... (other settings - see detailed explanations below)
```

**Detailed Configuration Options:**

* **`Image_Generator_Model`:** The Hugging Face model used for image generation.  You can explore other models on the Hugging Face website.
* **`DEFAULT_MUSIC_MODEL`:** The Hugging Face model used for music generation.  Explore options on Hugging Face.
* **`Object_Detection_Model`:** The Hugging Face model used for object detection in images.
* **`custom_model`:**  Set to `True` if you want to use a custom Gemini model.  You'll need to specify the `custom_model_name` and `custom_model_tokens`.
* **`show_time`:** Includes timestamps in the conversation history (`True/False`).
* **`history_channel_toggle`:** Enables per-channel conversation history (`True/False`).
* **`embed_colors`:**  Customizes embed colors (hexadecimal color code, e.g., `0x00ff00`).
* **`show_tokens_at_startup`:** Displays API keys on startup for verification (`True/False`).
* **`ffmpeg_path`:** Path to your `ffmpeg.exe` (required for TTS). Example: `r"C:\path\to\your\ffmpeg.exe"`. *On Replit, this is usually handled automatically.*
* **`tts_toggle`:** Enables TTS on startup (`True/False`).
* **`vc_voice`:**  Default TTS voice index (1-20 - see `VOICES` list in `config.py`).
* **`sync_voice_with_text`:** Synchronizes TTS with text output (`True/False`).
* **`HISTORY_FILE`:**  Path to the conversation history file.
* **`auto_start_tts`:**  Automatically starts TTS on joining a voice channel (`True/False`).

### 4. Running BatchBot: Bringing Your AI Companion to Life

Once you've installed the libraries and configured the settings, you're ready to run BatchBot! Open your terminal in the project directory and execute:

```bash
python main.py
```

If everything is set up correctly, BatchBot will connect to Discord and be ready to interact with your server.


---

## II. Interacting with BatchBot: Command Usage and Examples

### 1. Basic Commands:  Everyday Interactions

* **`/ai [Prompt]`:**  The heart of BatchBot! This command initiates a conversation.  BatchBot will use its AI powers to respond to your prompt, providing information, generating creative text formats, and engaging in dynamic conversations.
    * **Example:** `/ai What's the weather like in London today?`

* **`/search [Query]`:** Perform a web search using DuckDuckGo. BatchBot will summarize the most relevant results, saving you time and effort.
    * **Example:** `/search best laptops for programming`

* **`/search*yt [Query]`:** Search YouTube using DuckDuckGo, getting summaries and top video suggestions.
    * **Example:** `/search*yt funny cat videos`

* **`/img [Prompt]`:** Unleash your creativity! Generate images based on your text prompts using Hugging Face's Stable Diffusion or other selected models.
    * **Example:**  `/img a majestic dragon flying over a fantasy castle`
    * **Advanced Example (with Model Selection):** `/img a cute cat wearing a hat model: stabilityai/stable-diffusion-2-1`

### 2.  AI Toggle:  Seamless Conversations

* **`/aitoggle [on/off]`:**  Enable or disable automatic AI responses. With `aitoggle on`, BatchBot will respond to all your messages in the channel without needing the `/ai` prefix, creating a more natural conversational flow.


### 3. Memory Management:  Remembering What Matters

* **`/memory`:** Displays BatchBot's saved core memory, showing the information it has stored from past conversations and commands.

* **`//#m3m0ry9(c0r3// [Memory]`:**  This special command saves important information to BatchBot's core memory.  Use this for personal details, facts you want BatchBot to remember, or key insights from discussions.  This information will be added to the `system/data/core-memory.json` file.
    * **Example:** `//#m3m0ry9(c0r3// My birthday is on July 15th.`


### 4.  Utility Commands:  Helpful Tools for Your Server

* **`/timer [Seconds]`:** Sets a timer for the specified number of seconds.  BatchBot will send a message when the timer is up.
    * **Example:** `/timer 60` (sets a 1-minute timer)

* **`/say [Message]`:** Makes BatchBot repeat the specified message in the chat. This is useful for announcements or for having the bot say something specific.
    * **Example:** `/say Hello everyone! Welcome to the server!`
    * **Example (Specify Channel):** `/say Hello #general!  This message is for the general channel!`  (The bot will send "Hello This message is for the general channel!" to the #general channel). You can also use channel ID or mention the channel like <#channelId>.

* **`/profile [Member]`:** Displays information about a specified Discord member. If no member is provided, it displays information about the user who used the command.
    * **Example:** `/profile @User123`

* **`/serverinfo`:** Shows details about your Discord server, such as member count, creation date, and channels.

* **`/joke`:**  Need a laugh? BatchBot will tell you a random joke.

### 5.  Search Power-Ups:  Mastering Information Retrieval

* **`/search_save [Query]`:**  Performs a web search using DuckDuckGo and saves the results. This is great for storing research or information you want to access later.
* **`/search_view`:**  View your saved searches.
* **`/search_list`:**  Lists the queries of all your saved searches.
* **`/search_remove [Query or Number]`:**  Removes a saved search either by its query (the search term) or its number in the list.
* **`/search_show [Query]`:**  Performs a web search and shows the raw results without summarization.
* **`/search_img [Query] [Number of Images]`:** Searches for images related to your query and displays the specified number of images.


### 6.  File Analysis:  Unlocking the Content of Your Documents

BatchBot can analyze various file types, including PDFs, DOCX, XLSX, PPTX, and more. Simply upload the file to the Discord channel, and BatchBot will provide insights, summaries, or answer questions about its content. (This feature works automatically when `ai_toggle` is enabled).

### 7.  YouTube Analysis:  Summarizing and Transcribing Videos

Paste a YouTube URL into the chat, and BatchBot will automatically provide a summary and transcript of the video.  (Requires `ai_toggle` to be enabled).


### 8.  Voice Chat Commands (v2.1):  Bringing Conversations to Life

* **`/vc join [Channel Name]`:** Joins the specified voice channel. BatchBot will now join your voice chats and be ready to speak using TTS. 
* **`/vc leave`:** Makes BatchBot leave the current voice channel.
* **`/vc status`:** Shows which voice channel BatchBot is currently connected to.
* **`/vc tts [on/off / message]`:**  Toggles TTS on or off in the voice channel.  You can also use `/vc tts [message]` to have BatchBot speak a specific message in the voice channel.
* **`/vc voice [voice_number]`:** Changes BatchBot's TTS voice.  See the `VOICES` list in `config.py` for available voice numbers (1-20).
* **`/vc replay`:** Replays the last TTS message that BatchBot spoke.

### 9. Advanced Usage:  Fine-tuning BatchBot's Behavior

* **`/add [Instruction]`:** Adds a specific instruction to BatchBot's knowledge base. This can be used to fine-tune its responses or add specific information.
* **`/serv [Instruction]`:** Simulates the server giving instructions to BatchBot, adding them to the conversation history and potentially influencing its responses.
* **`/system [System Message]`:**  Adds a system message to the conversation history.  This can be used to set the context or provide background information for BatchBot. 
* **`/force`:** Forces BatchBot to respond, even if it's unsure or hesitant. Use this with caution, as it might produce unexpected results.
* **`/reset`:** Clears BatchBot's memory, resetting the conversation history and core memory. Use this to start fresh or if BatchBot's responses become irrelevant or erratic.
* `/name [new_name]`: Changes the user's name that the bot will use when mentioning the user.

---

## III.  Troubleshooting and Limitations

### 1. Known Issues

* **Voice chat (Under Development):** The voice chat features are still under development and may have some limitations.
* **Resource Limitations:**  High server load or complex requests can sometimes cause delays or errors. Consider hosting on Replit or a similar service for improved performance.

### 2.  Model Limitations

* **AI Model Biases:** AI models, including Gemini, are trained on vast amounts of data and may reflect biases present in that data.  BatchBot's responses might sometimes contain inaccurate, biased, or offensive content.
* **Imperfect Understanding:**  AI models don't always perfectly understand user intent, and responses might be irrelevant or nonsensical at times.  Rephrasing your prompts can often improve results.
* **Hallucinations:**  AI models can sometimes generate fabricated information or "hallucinate."  Always double-check information provided by BatchBot, especially for critical tasks.


### 3.  Reporting Issues and Providing Feedback

* **`/report [Report]`:**  Use this command to report bugs, errors, or other issues you encounter with BatchBot.  Please provide as much detail as possible to help us reproduce and fix the problem.
* **`/feedback [Feedback]`:**  Share your thoughts, suggestions, and ideas for improving BatchBot! Your feedback is invaluable in helping us develop a better bot.

---

## IV. Additional Resources and Support

* **Email:**  [batchbothelp@gmail.com](mailto:batchbothelp@gmail.com)
* **GitHub Repository:**  [https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot](https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot)  Report issues, contribute to the project, and stay updated on the latest developments.

---

This documentation provides a comprehensive overview of BatchBot's features and capabilities. We are continuously working to improve BatchBot and expand its functionality. Your feedback and contributions are always welcome!

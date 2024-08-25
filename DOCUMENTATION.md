# Batchbot Documentation

This document provides a comprehensive overview of Batchbot, a Discord bot powered by Google Gemini and designed for interactive conversations, information retrieval, and various utility functions.

## Setup and Configuration

1. **Install Required Libraries:**

   pip install discord.py google-generativeai requests Pillow colorama asyncio logging duckduckgo-search httpx docx markdown openpyxl python-pptx youtube-transcript-api fitz

2. **Obtain API Keys:**
   - **Discord Bot Token:** Create a Discord application and bot on the Discord Developer Portal and obtain the bot token.
   - **Google Gemini API Key:** Acquire an API key for Google Gemini.
   - **Hugging Face API Key (Optional):** Obtain an API key from Hugging Face to enable image generation features.

3. **Configure `config.py`:**
   - Replace `YOUR_DISCORD_BOT_TOKEN`, `YOUR_GEMINI_API_KEY`, and `YOUR_HUGGING_FACE_API_KEY` with your obtained API keys.
   - Customize `NAME` and `server_name` as desired.
   - Set `ai_toggle` to `True` to enable automatic AI responses by default.
   - Select the desired Gemini model using the `pro` variable (`True` for Gemini Pro, `True+` for Gemini Pro Advanced, `False` for Gemini Flash).
   - (Optional) Configure `Image_Generator_Model` to use a different image generation model from Hugging Face.

## Usage

### Basic Commands

- `/ai [Prompt]`: Initiate a conversation with Batchbot using the provided prompt.
- `/search [Query]`: Perform a web search using DuckDuckGo and provide a summarized response.
- `/search*yt [Query]`: Perform a YouTube search using DuckDuckGo and provide a summarized response.
- `/img [Prompt]`: Generate an image based on the provided prompt (requires Hugging Face API key).

### Additional Commands

- `/aitoggle [on/off]`: Enable or disable automatic AI responses.
- `/memory`: Display the saved core memory.
- `/timer [Seconds]`: Set a timer for the specified number of seconds.
- `/say [Message]`: Make the bot say the specified message.
- `/add [Instruction]`: Add an instruction to the bot's knowledge.
- `/serv [Instruction]`: Act as a server and add an instruction to the bot's memory.
- `/system [System Message]`: Add a system message to the conversation history.
- `/force`: Force the bot to respond to commands, even if it's hesitant.
- `/reset`: Clear the bot's memory of past conversations.
- `/profile [Member]`: Display information about the specified member (or yourself if no member is specified).
- `/serverinfo`: Display information about the current server.
- `/joke`: Tell a random joke.
- `/search*save [Query]`: Perform a web search and save the results.
- `/search*view`: View saved searches.
- `/search*list`: List the queries of saved searches.
- `/search*remove [Query or Number]`: Remove a saved search by query or number.
- `/search*show [Query]`: Perform a web search and display the raw results.
- `/search*img [Query] [Number of Images]`: Search for images and display the specified number.

## Core Memory

Batchbot uses core memory to store important information and context from past conversations. You can use the following command to interact with the core memory:

- `//#m3m0ry9(c0r3// [Memory]`: Save the specified memory to the core memory.

## Image Generation

Batchbot can generate images using various models from Hugging Face. You can select the desired model using the `/img` command with the `model` option. For example:

- `/img [Prompt] model: stabilityai/stable-diffusion-xl-base-1.0`

## Voice Chat (Under Development)

- `/vc join [Channel Name]`: Join the specified voice channel.
- `/vc leave`: Leave the current voice channel.

## Reporting Issues and Providing Feedback

- `/report [Report]`: Report bugs or issues with the bot.
- `/feedback [Feedback]`: Provide feedback or suggestions for improvement.

## Additional Notes

- Batchbot's behavior and responses are influenced by the configured Gemini model and its training data.
- The bot's memory is persistent and will be retained across sessions.
- Be mindful of the information you share with the bot, as it may be stored in its memory.

This documentation provides a general overview of Batchbot's features and functionality. For more detailed information, refer to the bot's source code and the Google Gemini documentation.

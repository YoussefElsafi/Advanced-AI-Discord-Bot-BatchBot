# BatchBot: The AI-Powered Discord Bot (Free & Open Source)

## Introduction

BatchBot is a cutting-edge Discord bot powered by advanced AI models, designed to bring a wide array of features to your server—completely free of charge. Whether you want to engage in natural conversations, analyze or generate images, summarize web searches, or explore various other capabilities, BatchBot has you covered.

## Features

BatchBot offers a rich set of features powered by state-of-the-art AI models:

- **AI Chat:** 
  - Engage in dynamic conversations with BatchBot using Google Gemini AI models (Gemini 1.5 Pro, Gemini 1.5 Pro Advanced, Gemini 1.5 Flash). It understands context, provides insightful answers, generates creative content, and can even engage in role-playing scenarios.

- **Image Processing:**
  - Upload images, and BatchBot will use powerful vision models to generate detailed descriptions. It can identify objects, scenes, and emotions within the images.

- **Video Processing:**
  - Upload videos, and BatchBot will use powerful vision models to generate detailed descriptions. It can identify objects, scenes, and emotions within the video.

- **Image Generation:**
  - Create stunning and personalized images using Hugging Face's Stable Diffusion. You can generate anything from imaginative scenes to funny memes based on your text prompts.

- **YouTube Analysis:**
  - Get summaries and transcripts from YouTube videos. BatchBot can analyze video URLs, extract content, and provide concise summaries.

- **File Analysis:**
  - Analyze and extract information from a variety of file types including PDFs, DOCX, Markdown, Python code, JavaScript, and more. BatchBot can also provide summaries and insights from these files.

- **Web Search and Summarization:**
  - Utilize DuckDuckGo's API for web searches. BatchBot provides summaries of the most relevant search results, making it easy to find the information you need.

- **Memory:**
  - BatchBot can remember important information shared during conversations or stored via commands. This feature enables personalized interactions and a better understanding of your preferences.

- **Custom User Names:**
  - Set a custom name for yourself in interactions with BatchBot, enhancing personalization and user experience.

- **And More!**
  - BatchBot continues to evolve with new features and improvements, providing even more value to your server.

## Getting Started

To get BatchBot up and running on your Discord server, follow these steps:

1. **Prerequisites:**
   - A Discord server.
   - Python 3.9+ installed.
   - A Discord Bot account: [Discord Applications](https://discord.com/developers/applications) 
   - An API Key from Google Generative AI (Gemini): [Gemini API Key](https://aistudio.google.com/app/apikey)
   - An API Key from Hugging Face: [Hugging Face API Key](https://huggingface.co/settings/tokens)
   - No need for an API Key from DuckDuckGo

2. **Install Dependencies:**
   - Clone the repository:
     ```bash
     git clone https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot.git
     cd Advanced-AI-Discord-Bot-BatchBot
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure Settings:**
   - In `system/config.py` file with the following content and replace the placeholders with your actual API keys and tokens:
     ```python
     TOKEN = "YOUR_DISCORD_BOT_TOKEN"
     API_KEY = "YOUR_GOOGLE_GENERATIVE_AI_API_KEY"
     HUGGING_FACE_API = "YOUR_HUGGING_FACE_API_KEY"
     # Add other configuration settings as needed
     ```

4. **Run the Bot:**
   - Start the bot using the following command:
     ```bash
     python main.py
     ```

## Usage

Interact with BatchBot using the following commands:

- `/ai [prompt]`: Starts a conversation with BatchBot. Use this command for any text-based prompt.
- `/img [prompt]`: Generates an image based on your text prompt using Stable Diffusion.
- `/search [query]`: Searches the web using DuckDuckGo and provides a summary of the results.
- `/search*yt [query]`: Searches YouTube for the query and provides a summary of the results.
- `/search*save [query]`: Saves web search results for later retrieval.
- `/search*view`: Displays your saved web searches.
- `/joke`: Tells a random joke.
- `/memory`: Displays the saved core memory.
- `//help`: Displays the avaliable commands.

## Core Functionality

BatchBot's core functionality includes:

- **AI-Powered Chat:** Uses Google's Gemini AI models to understand context, provide insightful answers, generate creative content, and engage in role-playing.
- **Image Analysis:** Analyzes images for object recognition, scene description, and emotion detection.
- **Video Analysis:** Provides accurate analysis of video content and transcripts.
- **Image Generation:** Generates images based on text prompts using models like Stable Diffusion.
- **YouTube Analysis:** Extracts and summarizes video transcripts.
- **File Analysis:** Processes various file types and provides information and summaries.
- **Web Search and Summarization:** Searches the web and summarizes search results using DuckDuckGo.
- **Memory:** Remembers information shared during conversations and stored using commands.

## Commands

Here are additional commands you can use:

- `/search*list`: Lists your saved search queries.
- `/search*show [query]`: Searches the web and displays results.
- `/timer [seconds]`: Sets a timer for the specified number of seconds.
- `/say [message]`: Echoes the given message.
- `/aitoggle [on/off]`: Enables or disables automatic AI responses.
- `/name [new name]`: Sets a custom name for yourself within BatchBot.
- `/reset`: Clears BatchBot's memory of past conversations.
- `/profile [member]`: Shows information about a user.
- `/serverinfo`: Shows information about the current server.
- `/add [instruction]`: Adds an instruction to BatchBot's memory.
- `/system [system]`: Adds a system instruction to BatchBot's memory.
- `/force`: Forces BatchBot to prioritize answering your commands.
- `/vc join [channel name]`: (Under development) Joins a specified voice channel.
- `/vc leave`: (Under development) Leaves the current voice channel.

## Additional Features

- **Customizable Instructions:** Influence BatchBot's behavior and personality using the `/add` command or in system/instructions.py.
- **File Uploads:** Upload files (images, videos, documents) for analysis.

## Key Advantages

- **Free to Use:** BatchBot is completely free with no paid tiers or limitations.
- **Open Source:** The code is publicly available on GitHub for contributions and collaboration.
- **Powerful AI:** Utilizes advanced AI models for a wide range of functionalities.
- **Customizable:** Tailor BatchBot's behavior with instructions and commands.

## Considerations

- **Free Tier Limitations:** Usage limits may apply for underlying APIs.
- **Development Stage:** Some features may be in progress or subject to change.

## Contributing

Contributions are welcome! Here's how you can help:

- Fork the repository.
- Create a branch for your changes.
- Make your changes and commit them.
- Push your changes to your fork.
- Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is provided "as is" without warranty of any kind. Use at your own risk.

## Acknowledgements

- Google Generative AI (Gemini)
- Hugging Face Stable Diffusion
- DuckDuckGo
- The Discord API

## Author

Youssef Elsafi

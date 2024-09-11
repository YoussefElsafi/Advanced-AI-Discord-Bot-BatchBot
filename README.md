# 🌌 BatchBot: The AI-Powered Discord Bot (Free & Open Source) 🚀

<div style="border-bottom: 2px solid #00ffff; margin-bottom: 20px;"></div>

## Introduction

**BatchBot** is a cutting-edge Discord bot powered by advanced AI models, designed to bring a wide array of features to your server—completely free of charge. It combines neon-styled visuals with state-of-the-art AI functionalities to give your server a futuristic touch. Engage in natural conversations, analyze or generate images, summarize web searches, and explore various other capabilities with a high-tech vibe.

<div style="border-bottom: 2px solid #00ffff; margin-bottom: 20px;"></div>

## Videos

> ### **Tutorial Video:**  
> [![Watch the Tutorial](https://img.shields.io/badge/Watch%20Tutorial-%F0%9F%93%BA-red)](https://youtu.be/ow-Cw8OLTdI)

> ### **Update Video for v1.5.0:**  
> [![Update Video (v1.5.0)](https://img.shields.io/badge/Update%20Video%20(v1.5.0)-%F0%9F%93%BA-red)](https://youtu.be/ow-Cw8OLTdI)

> ### **Update Video for v2.0.0:**  
> Not available yet.

## 🌟 Features

BatchBot offers a rich set of features powered by state-of-the-art AI models:

### 🤖 AI Chat
Engage in dynamic conversations with BatchBot using Google Gemini AI models (Gemini 1.5 Pro, Gemini 1.5 Pro Advanced, Gemini 1.5 Flash). It understands context, provides insightful answers, generates creative content, and can even engage in role-playing scenarios.

### 🖼️ Image Processing
Upload images, and BatchBot will use powerful vision models to generate detailed descriptions. It can identify objects, scenes, and emotions within the images.

- **Identify Objects Example:**
  - **Prompt:** detect the objects in this image
  - ![bugatti_object_image object](https://github.com/user-attachments/assets/c88bb44f-266b-4a59-aad0-34d59f025502)

### 🎥 Video Processing
Upload videos, and BatchBot will use powerful vision models to generate detailed descriptions. It can identify objects, scenes, and emotions within the video.

### 🎨 Image Generation
Create stunning and personalized images using Hugging Face's Stable Diffusion. Generate anything from imaginative scenes to funny memes based on your text prompts. BatchBot v2.0.0 now offers an expanded selection of image generation models, giving you more control and creative possibilities:

- **Expanded Model Choices:** Choose from a variety of models, including:
    - `stabilityai/stable-diffusion-xl-base-1.0` (Default)
    - `stabilityai/stable-diffusion-3-medium-diffusers`
    - `ehristoforu/dalle-3-xl-v2`
    - `black-forest-labs/FLUX.1-schnell`
    - `dataautogpt3/FLUX-anime2`
    - **`Yntec/Chip_n_DallE (New)`:**  Chip & DallE, known for its unique style
    - **`black-forest-labs/FLUX.1-dev (New)`:** Latest development version of Flux.1
    - **`Shakker-Labs/FLUX.1-dev-LoRA-Garbage-Bag-Art (New)`:** Specializes in a "Garbage Bag Art" style
    - **`Shakker-Labs/FLUX.1-dev-LoRA-playful-metropolis (New)`:** Creates images with a "Playful Metropolis" aesthetic
    - **`Shakker-Labs/FLUX.1-dev-LoRA-add-details (New)`:**  Adds intricate details to images

- **Image Example:**
    - **Prompt:** Realistic bugatti sports car driving on a highway with Lamborghini sports cars driving on the road.
    - **Model:** [Flux.1 DEV LoRA Add Details](https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-add-details) by [Shakker Labs](https://huggingface.co/Shakker-Labs)
    - ![bugatti_generated_image](https://github.com/user-attachments/assets/b94c5eec-a543-46ac-8c9f-62488e66d677) 

### 🎶 Music Generation
Unleash your inner composer with the `/music` command! BatchBot now leverages powerful AI models from Hugging Face to generate unique musical compositions based on your prompts. Choose your sound from:
  - `facebook/musicgen-small` (Default)
  - `facebook/musicgen-stereo-small`

### 📺 YouTube Analysis
Get summaries and transcripts from YouTube videos. BatchBot can analyze video URLs, extract content, and provide concise summaries. 

- **More Accurate YouTube Results in v2.0.0:** BatchBot now uses the DuckDuckGo Search API for YouTube searches, providing more precise and relevant video suggestions. 

### 📂 File Analysis
Analyze and extract information from a variety of file types including PDFs, DOCX, Markdown, Python code, JavaScript, and more. BatchBot can also provide summaries and insights from these files.

- **Advanced File Handling in v2.0.0:**  BatchBot's file handling has been significantly enhanced. It can now effectively analyze DOCX, XLSX, PPTX, and MCMETA files, expanding its ability to understand and interact with various document types. 

### 🌐 Web Search and Summarization
Utilize DuckDuckGo's API for web searches. BatchBot provides summaries of the most relevant search results, making it easy to find the information you need.

### 🧠 Memory
BatchBot can remember important information shared during conversations or stored via commands. This feature enables personalized interactions and a better understanding of your preferences. 

- **New Dedicated Command in v2.0.0:** You can now use the `/memory_save` command to explicitly save messages or information that you want BatchBot to remember.

### 🔤 Custom User Names
Set a custom name for yourself in interactions with BatchBot, enhancing personalization and user experience.

### 🚀 And More!
BatchBot continues to evolve with new features and improvements, providing even more value to your server.

<div style="border-bottom: 2px solid #00ffff; margin-bottom: 20px;"></div>

## 📈 Why Use Replit for Hosting?

For the best performance and fastest response times, we recommend hosting BatchBot on [Replit](https://replit.com). Replit offers an efficient, user-friendly environment that allows you to deploy and manage your bot with ease. 

### Benefits of Using Replit:

- **Instant Deployment:** Get your bot up and running in seconds.
- **Easy Configuration:** No need to worry about setting up complex environments.
- **Integrated Version Control:** Manage and track changes effortlessly.
- **Collaborative Coding:** Work with others in real-time, making it easier to develop and maintain your bot.

For a smooth experience, follow these steps:

1. Clone the repository to your Replit environment.
2. Install the required dependencies.
3. Configure the settings with your API keys.
4. Run the bot and enjoy!

<div style="border-bottom: 2px solid #00ffff; margin-bottom: 20px;"></div>

## Getting Started

To get BatchBot up and running on your Discord server, follow these steps:

### 📋 Prerequisites

- A Discord server.
- Python 3.9+ installed.
- A Discord Bot account: [Discord Applications](https://discord.com/developers/applications) 
- An API Key from Google Generative AI (Gemini): [Gemini API Key](https://aistudio.google.com/app/apikey)
- An API Key from Hugging Face: [Hugging Face API Key](https://huggingface.co/settings/tokens)

### 🛠️ Install Dependencies

1. Clone the repository:
```
git clone https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot.git
cd Advanced-AI-Discord-Bot-BatchBot
```
2. Install the required Python packages:

```
pip install -r requirements.txt
```

### ⚙️ Configure Settings

Edit the `system/config.py` file with the following content and replace the placeholders with your actual API keys and tokens:

```
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
API_KEY = "YOUR_GEMINI_API_KEY"
HUGGING_FACE_API = "YOUR_HUGGING_FACE_API_KEY"
DEFAULT_MUSIC_MODEL = "facebook/musicgen-small"
limit_history = False
history_limit = 100
show_time = True
custom_model = False
custom_model_name = "gemini-1.5-flash"
custom_model_tokens = 1048576
```

### 🚀 Run the Bot

Start the bot using the following command:
```
python main.py
```
## Usage

Interact with BatchBot using the following commands:

- `/ai [prompt]`: Starts a conversation with BatchBot. Use this command for any text-based prompt.
- `/aitoggle on/off`: Starts a conversation and responses automatically without using the /ai!
- `/img [prompt] [model(Optional)]`: Generates an image based on the provided description.
- `works if you have aitoggle on`: Analyzes an image and provides a detailed description.
- `no need for a command`: Summarizes a YouTube video and provides a transcript.
- `no need for a command`: Analyzes a file and provides key insights.
- `/music [prompt]`: Generates a music piece based on your text prompts.

For a full list of commands, type `//help` in Discord after adding BatchBot to your server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Google Generative AI](https://aistudio.google.com/app) for providing the advanced AI models.
- [Hugging Face](https://huggingface.co/) for the image generation models.
- [DuckDuckGo](https://duckduckgo.com/) for the web search API.
- And all the amazing contributors who have helped improve BatchBot!

## Support

If you have questions or need assistance, you can:

- Reach out via email: [Support](mailto:batchbothelp@gmail.com)
- Open an issue on our [GitHub repository](https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot/issues)
- Watch our [YouTube tutorial](https://youtu.be/ow-Cw8OLTdI) for setup instructions
- Watch our [Youtube Update Video (v1.5.0)](https://www.youtube.com/watch?v=CiG4pMOyPUo) for more information
- Check our [Documentation](DOCUMENTATION.md) for detailed guides

Enjoy using BatchBot! 🚀

___

**Update Info:**

- **Latest Version:** v2.0.0
- **Release Date:** 9/11/2024 | September 11, 2024
- **Published By:** Youssef Elsafi

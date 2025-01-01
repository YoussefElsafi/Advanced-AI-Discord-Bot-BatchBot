# 🌌 **BatchBot: The AI-Powered Discord Bot (Free & Open Source) 🚀**

![BatchBot Logo](https://github.com/user-attachments/assets/76b8a6fa-168c-43f8-b9cf-6a439d90b063)

---

## **Introduction**

BatchBot is a cutting-edge Discord bot powered by advanced AI models from **Google Gemini** and **Hugging Face**, designed to elevate your server experience with a futuristic, neon-infused aesthetic. Engage in natural conversations, analyze and generate images, get YouTube summaries, perform web searches, and much more – all for free!

> ❌ Disclaimer!!!
> Image and file analysis are not working, may be due to the new change of google's google.generativeai library, but we are actively working on a fix.

---

## **Videos**

* **Demo:** A quick walkthrough of the basics to get you up and running.
    [![Watch the Demo](https://img.shields.io/badge/Watch%20Demo-%F0%9F%93%BA-red)](https://youtu.be/ow-Cw8OLTdI)

* **What's New in v1.5.0:** Learn about the latest features and improvements in this update video.
    [![Watch the v1.5.0 Update Video](https://img.shields.io/badge/What%20's%20New%20in%20v1.5.0-%F0%9F%93%BA-red)](https://youtu.be/CiG4pMOyPUo?si=qCuVss8UxUCzIEim)

* **In-Depth Setup Guide:** A comprehensive guide to setting up the code from scratch.
    *Coming soon! Stay tuned for updates.*

---

## 🌟 **Features**

BatchBot offers a rich suite of features powered by state-of-the-art AI:

### 🤖 **AI Chat**

Engage in dynamic and context-aware conversations using **Google Gemini AI** (Pro, Pro Advanced, or Flash). Experience natural language understanding, insightful answers, creative content generation, and even role-playing.

### 🖼️ **Image Processing & Object Detection**

Upload images for detailed AI-powered analysis. BatchBot can identify objects, scenes, and even emotions within images. **New in v2.1:** Analyze multiple images at once!

* **Object Detection Example:**
    * **Prompt:** Detect the objects in this image
    * ![bugatti_object_image](https://github.com/user-attachments/assets/c88bb44f-266b-4a59-aad0-34d59f025502)

* **Image Recognition Example:**
    * ![Image Recognition Example](https://github.com/user-attachments/assets/0f57ab57-28ad-46d1-9863-0e10804e9719)

### 🎥 **Video Processing**

Upload videos for AI-powered analysis, identifying objects, scenes, and more.

### 🎨 **Image Generation**

Create stunning visuals using Hugging Face's **Stable Diffusion** and other powerful models. Generate anything from artistic masterpieces to humorous memes.

* **Expanded Model Choices (v2.0.0 & v2.1.0)**: BatchBot offers a wider selection of models, including specialized LoRAs (Low-Rank Adaptations) for unique styles:
    - `stabilityai/stable-diffusion-xl-base-1.0` (Default)
    - `stabilityai/stable-diffusion-3-medium-diffusers`
    - `ehristoforu/dalle-3-xl-v2`
    - `black-forest-labs/FLUX.1-schnell`
    - `dataautogpt3/FLUX-anime2`
    - `Yntec/Chip_n_DallE`
    - `black-forest-labs/FLUX.1-dev`
    - `Shakker-Labs/FLUX.1-dev-LoRA-Garbage-Bag-Art`
    - **`Shakker-Labs/FLUX.1-dev-LoRA-add-details` (v2.0.0):** For highly detailed images
    - **`Shakker-Labs/FLUX.1-dev-LoRA-Logo-Design` (v2.1.0):** Specializes in logo design

* **Image Example:**
    - **Prompt:** Realistic Bugatti sports car driving on a highway with Lamborghini sports cars.
    - **Model:** `Shakker-Labs/FLUX.1-dev-LoRA-add-details`
    - ![bugatti_generated_image](https://github.com/user-attachments/assets/b94c5eec-a543-46ac-8c9f-62488e66d677)

### 🎶 **Music Generation**

Compose unique musical pieces using AI! The `/music` command uses Hugging Face models to generate music based on your prompts.

* **Model Choices:**
    - `facebook/musicgen-small` (Default)
    - `facebook/musicgen-stereo-small`

### 📺 **YouTube Analysis**

Get quick summaries and full transcripts from YouTube videos. BatchBot analyzes video URLs and extracts key information.

* **Enhanced YouTube Search (v2.0.0)**: More accurate and relevant results using the **DuckDuckGo Search API**.

### 📂 **File Analysis**

Analyze and extract valuable information from various file types, including PDFs, DOCX, Markdown, Python, JavaScript, and more. BatchBot can even summarize complex documents.

* **Advanced File Handling (v2.0.0)**: Expanded support for DOCX, XLSX, PPTX, and MCMETA files.

### 🌐 **Web Search and Summarization**

Search the web efficiently using the DuckDuckGo API. BatchBot summarizes the most relevant results, saving you time and effort.

### 🧠 **Memory & Core Memory**

BatchBot remembers important information from conversations and through the dedicated `/memory_save` command (v2.0.0). This enhances personalization and context awareness.

### 🔤 **Custom User Names**

Personalize your interactions by setting a custom name for yourself.

### 🎙️ **Text-to-Speech in Voice Channels (v2.1)**

BatchBot can now join and speak in voice channels! Control its voice, replay messages, and more. See the "Features" section for details.

### 🌍 **Language Support**
- **7 Supported Languages:** BatchBot now supports **7 additional languages**, enhancing accessibility and global interaction. Supported languages include:
    - **English (Default)**
    - **Russian**
    - **Spanish**
    - **French**
    - **German**
    - **Arabic (Egypt)**
    - **Arabic**
  
- **Localized Responses**: BatchBot provides localized responses and improved comprehension in these languages. More languages will be added in future updates!

---

## 📈 Why Host on [bot-hosting.net](https://bot-hosting.net/?aff=1096964888972230767) Instead of Replit for Deployment?

While Replit is excellent for development and experimenting with BatchBot, it's not always the best choice for a bot that needs to be online 24/7. Replit's free tier has limitations, and their paid options can become expensive for continuous bot hosting.  For a reliable and cost-effective solution for *deploying* BatchBot, we strongly recommend [bot-hosting.net](https://bot-hosting.net/?aff=1096964888972230767).

### **Benefits of [bot-hosting.net](https://bot-hosting.net/?aff=1096964888972230767) for Deployment:**

*   **Superior Reliability for 24/7 Uptime:** Unlike Replit's free tier, `bot-hosting.net` is designed from the ground up to provide consistent uptime for bots, keeping BatchBot available whenever your users need it.
*   **Dedicated Server Resources:** You get dedicated resources, ensuring that your bot has smooth and consistent performance without the constraints imposed by shared hosting environments which Replit offers on their free tier.
*   **Optimized Bot Hosting Environment:** `bot-hosting.net` is specifically tailored for bots, providing an optimized server environment.
*   **Scalability:** As your bot's user base grows, you can easily scale your resources to handle the increased demand, without the downtime that is associated with migrating to a bigger server.
*   **Cost-Effective for Continuous Hosting:** In many cases, hosting with `bot-hosting.net` is more affordable than Replit for long-term, continuous bot hosting, especially if you are relying on Replit's paid plans.
*   **Easy Management:** Their platform provides an intuitive and easy-to-use dashboard, allowing you to manage and monitor your bot without complex server knowledge.
*   **Automated Backups:** Your valuable bot data is safe and secure with their automated backup system.
*   **Expert Bot Support:** Access specialized support from a team that understands the nuances of bot hosting.

### **How Using Our Link Supports Our Development Efforts:**

By choosing to host your bot with `bot-hosting.net` through [this link](https://bot-hosting.net/?aff=1096964888972230767), you're directly supporting our efforts to develop and maintain BatchBot. The referral credits we receive help us dedicate more time and resources to:

*   **Improving the Bot:** Adding new features, enhancing performance, and fixing bugs so BatchBot remains the best AI-powered Discord bot.
*   **Creating More Resources:** Producing tutorials, documentation, and other helpful materials to ensure you have a great experience using BatchBot.
*   **Keeping BatchBot Free and Open Source:** Your support helps us keep BatchBot accessible to everyone, for free.

**Recommendation:**

We highly recommend using Replit for the initial coding, testing, and experimentation phase.  However, when you are ready to deploy your bot and keep it running 24/7, we strongly suggest using [bot-hosting.net](https://bot-hosting.net/?aff=1096964888972230767) as a reliable and often more cost-effective hosting solution. Your support using [this link](https://bot-hosting.net/?aff=1096964888972230767) will greatly help us improve BatchBot.

---

## **Getting Started**

### 📋 **Prerequisites**

* A Discord server
* Python 3.9+
* A Discord Bot account ([Discord Applications](https://discord.com/developers/applications))
* A **Google Gemini API Key** ([Gemini API Key](https://aistudio.google.com/app/apikey))
* A **Hugging Face API Key** ([Hugging Face API Key](https://huggingface.co/settings/tokens))

### 🛠️ **Installation**

1. Clone the repository:

```bash
git clone https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot.git
cd Advanced-AI-Discord-Bot-BatchBot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### ⚙️ **Configuration**

Edit `system/config.py` with your API keys and desired settings (see detailed explanation above).

### 🚀 **Running the Bot**

```bash
python main.py
```

---

## **Usage**

* `/ai [prompt]`: Chat with BatchBot.
* `/aitoggle on/off`: Enable/disable automatic AI responses.
* `/img [prompt] [model]`: Generate images (optional model selection).
* Upload images for analysis (automatic with `aitoggle` on).
* Paste YouTube URLs for summaries and transcripts (automatic with `aitoggle` on).
* Upload files for analysis (automatic with `aitoggle` on).
* `/music [prompt] [model]`: Generate music (optional model selection).
* `/vc [action] [channel_name(optional)]`: Voice chat controls (join, leave, status, tts, voice, replay).
* `//help`: See all commands.

---

## **License**

MIT License - see the [LICENSE](LICENSE) file.

---

## **Acknowledgements**

Thanks to Google, Hugging Face, DuckDuckGo, and all contributors!

---

## **Known Issues and Limitations**

BatchBot is under active development. We are aware of potential issues and are working to resolve them. Please report any problems you encounter.

---

## **Support**

- Reach out via email: [Support](mailto:batchbothelp@gmail.com)
- Open an issue on our [GitHub repository](https://github.com/YoussefElsafi/Advanced-AI-Discord-Bot-BatchBot/issues)
- Watch our [YouTube Demo](https://youtu.be/ow-Cw8OLTdI) for setup instructions
- Watch our [YouTube Update Video (v1.5.0)](https://www.youtube.com/watch?v=CiG4pMOyPUo) for more information
- Check our [Documentation](DOCUMENTATION.md) for detailed guides

Enjoy using BatchBot! 🚀

---

**Update Info:**

* **Latest Version:** v2.2  
* **Release Date:** 12/07/2024  
* **Published By:** Youssef Elsafi

# IMPORTANT
#Discord Bot Token
TOKEN = "YOUR_DISCORD_BOT_TOKEN" # Grab your discord bot token at https://discord.com/developers/applications
#Gemini API KEY
API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY" # Grab your gemini api key at https://aistudio.google.com/app/apikey
#Hugging Face API KEY
HUGGING_FACE_API = "YOUR_HUGGING_FACE_API_KEY" # Grab your hugging face api key at https://huggingface.co/settings/tokens | (You can leave it but you will not have access to Image, music and object detection generation)
#Discord Bot's Name
NAME = "Your Bot Name" # Change it to what you want to name the AI Bot | The AI bot will use the name for conversations and chats 
# Server Name
server_name = "Your Server Name" # Replace with your server name
# Creator Name
creator = "Youssef Elsafi" # You can edit it to your name.

# Do not touch! ⛔🚫(It's system stuff.)
Ultimate = "ultimate" # Do not touch this setting! ⛔🚫
Super = "super" # Do not touch this setting! ⛔🚫


# Web Search
web_search = True # Enable or disable web search
GOOGLE_CUSTOM_SEARCH_API_KEY = "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY" # Grab your google custom search api key at https://developers.google.com/custom-search/docs/paid_element
GOOGLE_PROJECT_SEARCH_ENGINE_ID = "YOUR_GOOGLE_PROJECT_SEARCH_ENGINE_ID" # Grab your google project search engine id at https://programmablesearchengine.google.com/controlpanel/all

# Model Configuration
gemini_model = "Flash-002" # Options (Flash: Gemini 1.5 Flash | Pro: Gemini 1.5 Pro | Flash-8B: Gemini 1.5 Flash 8B | Flash-002: Gemini 1.5 Flash 002 | Pro-002: Gemini 1.5 Pro 002 | Flash-Latest: Gemini 1.5 Flash Latest | Pro-Latest: Gemini 1.5 Pro Latest | Exp-1114: Gemini Experimental 1114 | Exp-1121: Gemini Experimental 1121 | Exp-1206: Gemini Experimental 1206)
model_temperature = 1 # Model Temperature

# Settings
limit_history = True  # Use a limited conversation history
history_limit = 100 # Limit for conversation history (if limit_history is True)
show_time = False # Makes the bot able to know what is the time and date and also the time that the messages was sent
history_channel_toggle = True  # Enable or disable per-channel history
embed_colors = 0x00ff00 # Embed's color
show_tokens_at_startup = False # Shows the tokens and the api keys on the console at startup
safe_search = True # Give out safe searches (True, False)
ffmpeg_executable_path = r'C:\path\to\ffmpeg.exe'  # Replace with the actual path to ffmpeg executable | Doesn't need to be an .exe file
tts = True # When the bot is in a Voicechat channel, When you chat with the bot in text, it will output the text and outputs the generated audio (When you are in the vc channel with the bot)
vc_voice = 1  # Default voice index (1 corresponds to en-US-BrianNeural as its the default voice)
sync_voice_with_text = True # It will sync up the text and the voice in the exact time, but the response may be a little slower to respond
HISTORY_FILE = 'system/data/data.json' # File to store conversation history
preview_code_output = True # It's a Google Gemini feature which allows you to preview what will happen if you run a code.
safegen = True  # Activates filtering to block harmful or explicit content in image and music generation. We recommend keeping this set to True to ensure a safe and user-friendly experience for all users.
create_mod_channel = False # When is there is an very inappropriate prompt, it will automaticly create a mod channel that you can manage if you wanna ban, kick or timeout the user. (Only works if safegen is set to True)
mod_channel_name = "🔧・mod" # The mod channel name (Only works if safegen and create_mod_channel is set to True)
additional_details = False # Keeps the old Additional Image/Media/File Details from v1.0.0, v1.5.0, v2.0 and v2.1, which gives the Bot some more info about the image/file/media | May slow down the speed of the responses
discord_heartbeat_timeout = 60  # (Default is 60 seconds) If you encounter frequent heartbeat timeouts, increase this (e.g., to 90 or 120) to give the bot more time to respond before Discord assumes the connection is lost.
show_tokens = False # Shows the input and output tokens for the AI (Debug Setting)
add_watermark_to_generated_image = False # Add watermarks to the AI generated images, the watermark image source is in system/assets/watermark.png and you can change the watermark but make sure that the image is named as `watermark.png`
show_safety_settings_on_startup = False # Shows the safety settings on startup

# Experimental Settings
vc_AI = False # This is a feature that will make the bot recognize and respond to user's voice prompts in voice chat, Basically an AI Voice assistant. (Doesn't work perfectly but it will improve in future updates)
show_invite_link_on_startup = False # When you start the bot it will give you the invite link for the bot
smart_recognition = False # When is True, the bot will be able to detect that the user is talking to the bot or talking to a diffrent user so you can talk to your friend while aitoggle is on! (Sometimes Buggy and isn't perfect but it will improve in future updates)
fix_repeating_prompts = True # This feature will help and stop the bot from repeating responses and sending broken responses (Experimental Feature)

# Additional Personality (Options: True | Super | Ultimate | False)
cool_personality = False # Makes the AI talk in a cool way (Experimental Feature)

# Generation Models Settings
Image_Generator_Model = "stabilityai/stable-diffusion-xl-base-1.0" # Model of the image generator | You might need to reinvite the bot to fully update the model
DEFAULT_MUSIC_MODEL = "facebook/musicgen-small" # Model of the music generation | You might need to reinvite the bot to fully update the model
Object_Detection_Model = "facebook/detr-resnet-50" # Model of the object detection

# Safety Settings (Options: Default | None | Low | Moderate | High) We have set "None" as defualt becuase the chances of getting errors will be low.
Dangerous = "None"
Harassment = "None"
Hate_Speech = "None"
Sexually_Explicit = "None"
Dangerous_Content = "None"

# Advanced Stuff (Recommended to not change)
advanced_model = 'gemini-exp-1206'




Image_Model = Image_Generator_Model
if Image_Model == "stabilityai/stable-diffusion-xl-base-1.0":
    Image_Model_Name = "Stable Diffusion XL Base 1.0"
else:
    Image_Model_Name = Image_Model

# List of available voices (20 in total)
VOICES = [
    'en-US-BrianNeural',     # 1 (Defualt)
    'en-US-JennyNeural',     # 2
    'en-US-GuyNeural',       # 3
    'en-GB-SoniaNeural',     # 4
    'en-AU-NatashaNeural',   # 5
    'en-IN-NeerjaNeural',    # 6
    'en-NZ-MitchellNeural',  # 7
    'en-CA-ClaraNeural',     # 8
    'en-IE-EmilyNeural',     # 9
    'en-SG-WayneNeural',     # 10
    'en-ZA-LeonNeural',      # 11
    'en-GB-RyanNeural',      # 12
    'en-AU-WilliamNeural',   # 13
    'en-IN-PrabhatNeural',   # 14
    'en-NZ-MollyNeural',     # 15
    'en-CA-LiamNeural',      # 16
    'en-IE-OrlaNeural',      # 17
    'en-SG-LunaNeural',      # 18
    'en-US-AriaNeural',      # 19
    'en-GB-MaisieNeural'     # 20
]

def get_safety_setting(level):
    levels = {
        "none": "BLOCK_NONE",
        "low": "BLOCK_ONLY_HIGH",
        "moderate": "BLOCK_MEDIUM_AND_ABOVE",
        "high": "BLOCK_LOW_AND_ABOVE",
        "default": "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
    }
    setting = levels.get(level.lower())
    if setting is None:
        print(f"Safety Set Error: '{level}' is not a valid safety setting option. Must be one of: None, Low, Moderate, High or Default.")
        quit()
    return setting

dangerous_safety_set = get_safety_setting(Dangerous)
harassment_safety_set = get_safety_setting(Harassment)
hate_speech_safety_set = get_safety_setting(Hate_Speech)
sexually_explicit_safety_set = get_safety_setting(Sexually_Explicit)
dangerous_content_safety_set = get_safety_setting(Dangerous_Content)

sys_security = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": dangerous_safety_set},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": harassment_safety_set},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": hate_speech_safety_set},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": sexually_explicit_safety_set},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": dangerous_content_safety_set},
]

if gemini_model.lower() in ["pro"]:
    preview_model_name = "Gemini 1.5 Pro"
    model_name = "gemini-1.5-pro"
elif gemini_model.lower() in ["pro-2", "pro-002"]:
    preview_model_name = "Gemini 1.5 Pro 002"
    model_name = "gemini-1.5-pro-002"
elif gemini_model.lower() in ["flash-2", "flash-002"]:
    preview_model_name = "Gemini 1.5 Flash 002"
    model_name = "gemini-1.5-flash-002"
elif gemini_model.lower() in ["flash-8b", "flash-8B"]:
    preview_model_name = "Gemini 1.5 Flash 8B"
    model_name = "gemini-1.5-flash-8b"
elif gemini_model.lower() in ["flash"]:
    preview_model_name = "Gemini 1.5 Flash"
    model_name = "gemini-1.5-flash"
elif gemini_model.lower() in ["flash-latest"]:
    preview_model_name = "Gemini 1.5 Flash Latest"
    model_name = "gemini-1.5-flash-latest"
elif gemini_model.lower() in ["pro-latest"]:
    preview_model_name = "Gemini 1.5 Pro Latest"
    model_name = "gemini-1.5-Pro-latest"
elif gemini_model.lower() in ["exp-1114", "experimental-1114", "1114"]:
    preview_model_name = "Gemini Experimental 1114"
    model_name = "gemini-exp-1114"
elif gemini_model.lower() in ["exp-1121", "experimental-1121", "1121"]:
    preview_model_name = "Gemini Experimental 1121"
    model_name = "gemini-exp-1121"
elif gemini_model.lower() in ["exp-1206", "experimental-1206", "1206"]:
    preview_model_name = "Gemini Experimental 1206"
    model_name = "gemini-exp-1206"
else:
    print(f"Error choosing Gemini Model: {gemini_model} is not a valid model. valid models are: (Pro, Flash, Flash-8B, Pro-002, Flash-002, Pro-Latest, Flash-Latest, Exp-1114)")
    exit()

tts_toggle = tts

# Configure the Google Generative AI
gen_config = {
    "temperature": model_temperature,
    "response_mime_type": "text/plain",
}

gen_config2 = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 90,
    "response_mime_type": "text/plain",
}


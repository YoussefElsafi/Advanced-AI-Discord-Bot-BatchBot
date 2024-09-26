#Discord Bot Token
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
#Gemini API KEY
API_KEY = "YOUR_GEMINI_API_KEY"
#Hugging Face API KEY
HUGGING_FACE_API = "YOUR_HUGGING_FACE_API_KEY" # You can leave it but you will not have access to Image, music and object detection generation
#Discord Bot's Name
NAME = "BatchBot"
# Server Name
server_name = "EPIC SERVER" # Replace with your server name

# Config Settings
ai_toggle = False # Start automatically with ai toggle on or off
pro = False # Options (True (Gemini 1.5 Pro), True+ (gemini-1.5-pro-exp-002), False (Gemini 1.5 Flash))
model_temperature = 1 # Model Temperature
limit_history = False  # Use a limited conversation history
history_limit = 100     # Limit for conversation history (if limit_history is True)
show_time = False # Makes the bot able to know what is the time and date and also the time that the messages was sent
history_channel_toggle = True  # Enable or disable per-channel history
embed_colors = 0x00ff00 # Embed color
show_tokens_at_startup = False # Shows the tokens and the api keys on the terminal at startup
fix_repeating_prompts = True # This feature will help and stop the bot from repeating responses and sending broken responses (Experimental Feature)
safe_search = 'On' # Give out safe searches (On, Off)
voicechat = True # Enable or disable voice chat
ffmpeg_path = r'c:\ffmpeg\ffmpeg.exe'  # replace with the actual path to ffmpeg.exe | C:\path\to\ffmpeg.exe
tts_toggle = False # When you start the bot, it will start automatically with tts on or off
vc_voice = 1  # Default voice index (1 corresponds to en-US-BrianNeural as its the default voice)
sync_voice_with_text = True # It will sync up the text and the voice in the exact time, but the response may be a little slower to respond
HISTORY_FILE = 'system/data/user_data.json' # File to store conversation history
auto_start_tts = True # When you use /vc join or /vc leave, it will automatically activate and deactivate TTS

# Models Settings
Image_Generator_Model = "stabilityai/stable-diffusion-xl-base-1.0" # Model of the image generator | You might need to reinvite the bot to fully update the model
DEFAULT_MUSIC_MODEL = "facebook/musicgen-small" # Model of the music generation | You might need to reinvite the bot to fully update the model
Object_Detection_Model = "facebook/detr-resnet-50" # Model of the object detection
custom_model = False # Use a custom google gemini model
custom_model_name = "gemini-1.5-flash" # Name of the custom model
custom_model_tokens = 1048576 # Tokens of the custom model

Image_Model = Image_Generator_Model
if Image_Model == "stabilityai/stable-diffusion-xl-base-1.0":
    Image_Model_Name = "Stable Diffusion XL Base 1.0"
else:
    Image_Model_Name = Image_Model


# List of available voices (20 in total)
VOICES = [
    'en-US-BrianNeural',     # 1
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

sys_security = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]
if custom_model:
    max_tokens = custom_model_tokens
else:
    if pro == True:
        max_tokens = 2097152 
        MODEL = "Gemini 1.5 Pro"
    elif pro == "True+":
        max_tokens = 32769
        MODEL = "Gemini 1.5 Pro Advanced"
    elif pro == False:
        max_tokens = 1048576
        MODEL = "Gemini 1.5 Flash"

if pro == "True+":
    top_k_num = 40
else:
    top_k_num = 64

# Configure the Google Generative AI
gen_config = {
    "temperature": model_temperature,
    "top_p": 0.95,
    "top_k": top_k_num,
    "max_output_tokens": max_tokens,
    "response_mime_type": "text/plain",
}
gen_config2 = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 90,
    "response_mime_type": "text/plain",
}


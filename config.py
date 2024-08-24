#Discord Bot Token
TOKEN = "DISCORD_TOKEN_HERE"
#Gemini API KEY
API_KEY = "GEMINI_API_KEY_HERE"
#Hugging Face API KEY
HUGGING_FACE_API = "HUGGING_FACE_API_KEY_HERE" # You can leave it but you will not have access to Image generation
#Discord Bot's Name
NAME = "BatchBot" # Change to whatever you want!
# Server Name
server_name = "EPIC SERVER" # Replace with your server name

# Config Settings
ai_toggle = False # Start automatically with ai toggle on or off
pro = False # Options (True (Gemini 1.5 Pro), True+ (gemini-1.5-pro-exp-0801), False (Gemini 1.5 Flash))
online_toggle = False # will activate always on bot (Under-Dev)

# Visualizer Settings (AI Generators)
Image_Generator_Model = "stabilityai/stable-diffusion-xl-base-1.0" # May require to reinvite the bot to get the full changes

Image_Model = Image_Generator_Model
if Image_Model == "stabilityai/stable-diffusion-xl-base-1.0":
    Image_Model_Name = "Stable Diffusion XL Base 1.0"
else:
    Image_Model_Name = Image_Model



sys_security = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

if pro == True:
    max_tokens = 2097152 
    MODEL = "Gemini 1.5 Pro"
elif pro == "True+":
    max_tokens = 2097152 
    MODEL = "Gemini 1.5 Pro Advanced"
elif pro == False:
    max_tokens = 1048576
    MODEL = "Gemini 1.5 Flash"

# Configure the Google Generative AI
gen_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
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


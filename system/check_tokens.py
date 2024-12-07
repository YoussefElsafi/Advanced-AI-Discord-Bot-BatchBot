import os
import json
import requests
from colorama import Fore, Style
from system.config import TOKEN, API_KEY, HUGGING_FACE_API, gen_config, sys_security, GOOGLE_CUSTOM_SEARCH_API_KEY, GOOGLE_PROJECT_SEARCH_ENGINE_ID, web_search
import google.generativeai as genai

# Function to load saved tokens
def load_saved_tokens(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save tokens
def save_tokens(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to check bot token
def check_bot_token(token):
    headers = {"Authorization": f"Bot {token}"}
    try:
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking bot token: {e}")
        return False

# Function to check Gemini API
def check_gemini_api(api_key):
    try:
        genai.configure(api_key=api_key)
        test_model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=gen_config, safety_settings=sys_security)
        test_model.generate_content("say '.'")  # Simple test
        return True
    except Exception as e:
        print(f"Error checking Gemini API: {e}")
        return False

# Function to check Hugging Face API
def check_hugging_api(api_key):
    url = "https://huggingface.co/api/whoami-v2"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking Hugging Face API: {e}")
        return False

# Function to check Google Custom Search API key and search engine ID
def check_google_search_api(api_key, cse_id):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': 'test',
        'num': 1,
    }
    try:
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking Google Custom Search API: {e}")
        return False

# Function to verify Google API Key and Project ID independently
def verify_token(token, file_path, token_name, check_function):
    token_data = load_saved_tokens(file_path)
    saved_token = token_data.get(token_name)
    token_verified = token_data.get(f"{token_name}_verify", False)

    # Check if the token matches the saved one and is already verified
    if token == saved_token and token_verified:
        return True  # Token is already verified
    if not (token_name == "google_search_api_key" or "google_search_project_id" in token_name):
        print(f"{Fore.WHITE + Style.BRIGHT + Style.DIM}Verifying {token_name}...{Style.RESET_ALL}")
    is_valid = check_function(token)
    if is_valid:
        if not (token_name == "google_search_api_key" or "google_search_project_id" in token_name):
            print(f"{Fore.GREEN + Style.BRIGHT}{token_name} verified!{Style.RESET_ALL}")
        save_tokens({token_name: token, f"{token_name}_verify": True}, file_path)
    else:
        if not (token_name == "google_search_api_key" or "google_search_project_id" in token_name):
            print(f"{Fore.RED + Style.BRIGHT}Invalid {token_name}!{Style.RESET_ALL}")
        save_tokens({token_name: token, f"{token_name}_verify": False}, file_path)
    return is_valid


# Function to verify all tokens
def tokens():
    """Verifies and manages API tokens."""
    tokens_file_path = 'system/data/saved-token.json'
    gemini_api_file_path = 'system/data/saved-genai-api-key.json'
    hugging_api_file_path = 'system/data/saved-hugging-face-api-key.json'
    google_search_api_file_path = 'system/data/saved-google-search-api-key.json'
    google_search_id_file_path = 'system/data/saved-google-search-project-id.json'

    discord_token_verified = False
    gemini_api_key_verified = False
    hugging_face_api_verified = False
    google_search_api_key_verified = False
    google_search_project_id_verified = False

    # --- Discord Token Verification ---
    discord_token_verified = verify_token(
        TOKEN, tokens_file_path, "discord_token", check_bot_token
    )
    if not discord_token_verified:
        return False, False, False, False

    # --- Gemini API Verification ---
    gemini_api_key_verified = verify_token(
        API_KEY, gemini_api_file_path, "gemini_api_key", check_gemini_api
    )

    # --- Hugging Face API Verification ---
    hugging_face_api_verified = verify_token(
        HUGGING_FACE_API, hugging_api_file_path, "hugging_api_key", check_hugging_api
    )

    # --- Google Custom Search API Key Verification ---
    if web_search:
        google_search_api_key_verified = verify_token(
            GOOGLE_CUSTOM_SEARCH_API_KEY,
            google_search_api_file_path,
            "google_search_api_key",
            lambda key: check_google_search_api(key, GOOGLE_PROJECT_SEARCH_ENGINE_ID),
        )

        # --- Google Project ID Verification ---
        google_search_project_id_verified = verify_token(
            GOOGLE_PROJECT_SEARCH_ENGINE_ID,
            google_search_id_file_path,
            "google_search_project_id",
            lambda cse_id: check_google_search_api(GOOGLE_CUSTOM_SEARCH_API_KEY, cse_id),
        )

    return (
        discord_token_verified,
        gemini_api_key_verified,
        hugging_face_api_verified,
        google_search_api_key_verified,
        google_search_project_id_verified,
    )

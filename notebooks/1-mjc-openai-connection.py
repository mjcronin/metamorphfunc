# %%
import keyring
import openai

# %%
# Load credentials and configure openai
keychain_entry = 'openai-metamorphfunc'
keychain_username = ''
openai.api_key = keyring.get_password(keychain_entry, keychain_username)

# %%
# Set conversation args
args = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "messages": []
}

# %%
# Set system prompt
system_prompt = "You are a code completion assistant. Provide concise responses to user prompts"
sys = {
    "role": "system",
    "content": system_prompt
}
args["messages"].append(sys)

# %%
# Get openai response
response = openai.ChatCompletion.create(**args)

# %%
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt_msg = ""

# take the prompt from the input
if len(sys.argv) > 1:
    prompt_msg = sys.argv[1]
else:
    print("You need to provide a prompt message!")
    exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt_msg)]),
]
generated_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

# # Print the text
print(generated_response.text)

# # Print the meta data
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(f"User prompt: {prompt_msg}")
    print(f"Prompt tokens: {generated_response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {generated_response.usage_metadata.candidates_token_count}")
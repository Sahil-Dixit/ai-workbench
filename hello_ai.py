import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found!")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": "What is generative AI in one sentence?"},
        ],
        temperature=0.7,
        max_tokens=100,
    )

    print("Response:")
    print(f"  {response.choices[0].message.content}")
    print()
    print("-" * 50)
    print("Response metadata:")
    print(f"  Model used:        {response.model}")
    print(f"  Prompt tokens:     {response.usage.prompt_tokens}")
    print(f"  Completion tokens: {response.usage.completion_tokens}")
    print(f"  Total tokens:      {response.usage.total_tokens}")

except AuthenticationError:
    print("Authentication failed. Check your API key in .env")
    sys.exit(1)
except APIConnectionError:
    print("Cannot connect to OpenAI. Check your internet connection.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
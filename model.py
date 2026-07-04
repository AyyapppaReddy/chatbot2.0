import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def get_response(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"
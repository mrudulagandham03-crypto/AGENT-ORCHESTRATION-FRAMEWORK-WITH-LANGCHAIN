import os
from dotenv import load_dotenv

load_dotenv()

from google import genai  # correct import from google‑genai package

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",  # or another valid Gemini model
    contents="Explain what image smoothing filters are in simple words."
)

print(response.text)


import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# Configure Gemini
genai.configure(api_key=api_key)

# Choose a valid model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate content
response = model.generate_content("Explain Machine Learning in simple words in simple terms")

# Print the response text
print(response.text)

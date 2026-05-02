import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("API Key not found!")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-flash-latest")

try:
    response = model.generate_content("Hello, how are you?")
    print("Gemini Response:", response.text)
except Exception as e:
    print("Gemini Error:", e)

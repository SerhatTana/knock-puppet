import os
import requests
import json
import base64
from dotenv import load_dotenv

load_dotenv()

# Google API Key'i .env'den alıyoruz
# Eğer GEMINI_API_KEY ile aynıysa onu kullanabiliriz, 
# değilse GOOGLE_API_KEY adında yeni bir değişken ekleyebilirsiniz.
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

def generate_speech(text, filename="response.mp3"):
    if not API_KEY:
        print("Error: GOOGLE_API_KEY not found in .env")
        return None

    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"

    # SSML (Speech Synthesis Markup Language) kullanarak sesi "yorgun" hale getiriyoruz
    ssml_text = f"""
    <speak>
      <prosody rate="85%" pitch="-2st">
        {text}
      </prosody>
    </speak>
    """

    payload = {
        "input": {"ssml": ssml_text},
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Neural2-D",
            "ssmlGender": "MALE"
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "effectsProfileId": ["small-bluetooth-speaker-class-device"]
        }
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        audio_content = base64.b64decode(data["audioContent"])

        file_path = os.path.join("static", "audio", filename)
        with open(file_path, "wb") as out:
            out.write(audio_content)
            
        return filename
    except Exception as e:
        print(f"TTS REST Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Details: {e.response.text}")
        return None

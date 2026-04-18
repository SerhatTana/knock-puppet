import requests
import urllib.parse
from pathlib import Path

MOOD_VISUALS = {
    "weary":         "a worn marionette puppet of a soldier, hanging loosely, Vietnam era uniform, dark background, watercolor style",
    "nostalgic":     "a soldier puppet looking at a faded photograph, soft warm light, 1970s aesthetic, painted texture",
    "accepting":     "a marionette puppet with cut strings beginning to fall, peaceful expression, golden hour light",
    "fading":        "a puppet dissolving into dust and light, strings breaking, silhouette against a bright doorway, heaven's door",
    "angry":         "a marionette puppet of a soldier with clenched wooden fists, harsh red lighting, tangled strings, chaotic background",
    "afraid":        "a trembling soldier puppet huddled in a dark corner, deep shadows, wide hollow eyes, cold blue lighting",
    "hallucinating": "a surreal marionette puppet of a soldier, melting background, neon jungle colors, distorted perspective, psychedelic",
    "regretful":     "a soldier puppet kneeling in the mud, head bowed, rain pouring down, somber grey tones, melancholic atmosphere"
}

def generate_puppet_image(mood: str, output_dir: str = "static/generated") -> str:
    """
    Ruh haline göre görsel üret, dosya yolunu döndür. 
    Pollinations.ai API'si kullanılır (Ücretsizdir ve API Key gerektirmez).
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    prompt = f"{MOOD_VISUALS.get(mood, MOOD_VISUALS['weary'])}, artistic, cinematic, no text"
    encoded_prompt = urllib.parse.quote(prompt)
    
    # Pollinations image generation endpoint
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
    
    # Görseli indir ve kaydet
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = f"{output_dir}/puppet_{mood}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        print("Görsel oluşturulurken bir hata oluştu.")
        return ""

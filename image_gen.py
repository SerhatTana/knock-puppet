import requests
import urllib.parse
from pathlib import Path

# Karakterin asla değişmeyen fiziksel özellikleri
CHARACTER_BASE = "A weathered, hand-carved wooden marionette puppet of a 1970s Vietnam soldier, wearing a tattered olive-drab uniform, a faded headband, visible wood grain texture, vintage doll joints."

# Genel sanat tarzı
STYLE_BASE = "watercolor and charcoal sketch style, moody cinematic lighting, dark vignetted background, 4k, artistic, no text"

# Sabit tohum (Consistency için en kritik ayar)
DEFAULT_SEED = 12345

MOOD_VISUALS = {
    "weary":         "hanging loosely from tangled strings, head bowed, exhausted expression",
    "nostalgic":     "looking closely at a small faded photograph in its wooden hands, warm soft lighting",
    "accepting":     "strings being cut and falling, looking upwards towards a soft golden light, peaceful",
    "fading":        "dissolving into glowing dust particles, silhouette against a bright doorway",
    "angry":         "clenched wooden fists, harsh red lighting, aggressive posture, tangled strings",
    "afraid":        "huddled in a dark corner, wide hollow eyes, deep blue shadows, trembling",
    "hallucinating": "surreal perspective, melting surroundings, neon jungle colors, distorted proportions",
    "regretful":     "kneeling in thick mud, rain pouring down, somber grey tones, head in hands"
}

def generate_puppet_image(mood: str, output_dir: str = "static/generated") -> str:
    """
    Ruh haline göre görsel üret, dosya yolunu döndür. 
    Karakter bazlı tutarlılık (consistency) için sabit seed ve base prompt kullanılır.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    mood_desc = MOOD_VISUALS.get(mood, MOOD_VISUALS["weary"])
    
    # Tüm parçaları birleştiriyoruz
    full_prompt = f"{CHARACTER_BASE}, {mood_desc}, {STYLE_BASE}"
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    # Pollinations URL'sine seed ekliyoruz
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed={DEFAULT_SEED}"
    
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            filename = f"{output_dir}/puppet_{mood}.png"
            with open(filename, "wb") as f:
                f.write(response.content)
            return filename
        else:
            print(f"Görsel hatası: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Görsel oluşturulurken bir hata oluştu: {e}")
        return ""

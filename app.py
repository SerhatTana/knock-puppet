from flask import Flask, render_template, request, jsonify, send_from_directory
from llm_agent import get_puppet_response, detect_mood
from image_gen import generate_puppet_image
from tts_engine import generate_speech
import os
import time

app = Flask(__name__)
conversation_history = []
current_puppet_mood = "weary"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history, current_puppet_mood
    
    user_message = request.json.get("message", "")
    
    # Mevcut ruh halini kaydet
    prev_mood = current_puppet_mood
    
    # Yeni ruh halini kullanıcının mesajına göre LLM ile belirle
    current_puppet_mood = detect_mood(user_message, current_puppet_mood)
    
    # LLM yanıtı al
    print(f"Getting LLM response for mood: {current_puppet_mood}...")
    puppet_response = get_puppet_response(user_message, conversation_history, current_puppet_mood)
    print(f"LLM Response received: {puppet_response[:50]}...")
    
    # Konuşma geçmişini güncelle
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": puppet_response})
    
    # Görsel üret (sadece mood değiştiğinde)
    image_path = None
    if current_puppet_mood != prev_mood:
        print(f"Generating image for mood: {current_puppet_mood}...")
        image_path = generate_puppet_image(current_puppet_mood)
        print(f"Image generation finished: {image_path}")
        if image_path:
            image_path = image_path.replace("static/", "")  # URL için düzelt
    
    # Ses üret (Google Cloud TTS)
    audio_file = f"speech_{int(time.time())}.mp3"
    audio_path = generate_speech(puppet_response, audio_file)
    
    return jsonify({
        "response": puppet_response,
        "mood": current_puppet_mood,
        "image": image_path,
        "audio": audio_path
    })

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history, current_puppet_mood
    conversation_history = []
    current_puppet_mood = "weary"
    
    # Reset durumunda ilk resmi (weary) oluştur
    image_path = generate_puppet_image("weary")
    if image_path:
        image_path = image_path.replace("static/", "")
        
    return jsonify({"status": "reset", "image": image_path})

if __name__ == "__main__":
    app.run(debug=True)

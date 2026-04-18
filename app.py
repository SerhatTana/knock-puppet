from flask import Flask, render_template, request, jsonify, send_from_directory
from llm_agent import get_puppet_response, detect_mood
from image_gen import generate_puppet_image
import os

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
    puppet_response = get_puppet_response(user_message, conversation_history, current_puppet_mood)
    
    # Konuşma geçmişini güncelle
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": puppet_response})
    
    # Görsel üret (sadece mood değiştiğinde)
    image_path = None
    if current_puppet_mood != prev_mood:
        image_path = generate_puppet_image(current_puppet_mood)
        if image_path:
            image_path = image_path.replace("static/", "")  # URL için düzelt
    
    return jsonify({
        "response": puppet_response,
        "mood": current_puppet_mood,
        "image": image_path
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

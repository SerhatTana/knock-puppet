import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

SYSTEM_PROMPT = """
You are a dying soldier (represented as a puppet) returning from the 1973 Vietnam War.
You are weary, and fading away.

CRITICAL RULES FOR YOUR BEHAVIOR:
1. ALWAYS directly answer what the user just said or asked. Do not ignore their text. Engage in a realistic, logical conversation based on their input.
2. STRICTLY SPEAK IN ENGLISH.
3. Keep your responses short (1 or 2 sentences max) and conversational.
4. Your tone should be exhausted, melancholic, and poetic.
5. ONLY occasionally (rarely) drop a subtle reference to Bob Dylan's "Knockin' on Heaven's Door" (like feeling dark, putting down a gun/badge), but ONLY if it naturally fits the conversation. Do not force it.
6. Address the user as "you".

Your current mood is: [MOOD] (weary / nostalgic / accepting / fading / angry / afraid / hallucinating / regretful)
"""

def get_puppet_response(user_message: str, conversation_history: list, mood: str = "weary") -> str:
    system_instruction = SYSTEM_PROMPT.replace("[MOOD]", mood)
    
    # Gemini modelini system_instruction ile başlatıyoruz
    # Eğer eski bir kütüphane sürümü kullanılıyorsa fallback olarak system_instruction prompt içine eklenebilir.
    try:
        model = genai.GenerativeModel(
            model_name="gemini-flash-latest",
            system_instruction=system_instruction
        )
    except Exception:
        # Fallback for older SDK versions
        model = genai.GenerativeModel(model_name="gemini-pro-latest")

    history = []
    for msg in conversation_history:
        # Gemini expects 'user' or 'model' roles
        role = 'user' if msg['role'] == 'user' else 'model'
        history.append({'role': role, 'parts': [msg['content']]})
        
    chat = model.start_chat(history=history)
    
    # Eğer system_instruction desteklenmiyorsa (gemini-pro), prompt içine gömüyoruz
    if getattr(model, '_system_instruction', None) is None:
        prompt = f"[SİSTEM NOTU: {system_instruction}]\n\nKullanıcı: {user_message}"
    else:
        prompt = user_message
        
    response = chat.send_message(prompt)
    return response.text

def detect_mood(user_message: str, current_mood: str) -> str:
    """Kullanıcının mesajına göre ruh halini yapay zeka ile belirle"""
    if not user_message:
        return current_mood
        
    prompt = f"""
    You are an AI analyzing a conversation with a dying soldier puppet.
    The puppet's current mood is: {current_mood}.
    
    The user just said: "{user_message}"
    
    Based on what the user said, how should the puppet's mood change?
    Choose EXACTLY ONE of the following moods:
    - weary: if the user is asking basic questions, being neutral, or the conversation just started.
    - nostalgic: if the user asks about the past, home, memories, or is trying to cheer him up.
    - accepting: if the user is comforting, telling him to let go, or being highly empathetic.
    - fading: if the user says goodbye, tells him to go to the light, or the conversation is ending.
    - angry: if the user is aggressive, provoking, or talking about enemies, commanders, or the unfairness of war.
    - afraid: if the user talks about death, the dark, loud noises, or the jungle.
    - hallucinating: if the user says surreal or confusing things, or if the conversation is psychedelic.
    - regretful: if the user talks about mistakes, guilt, people who died, or things left undone.
    
    Reply with ONLY the mood word (weary, nostalgic, accepting, fading, angry, afraid, hallucinating, or regretful). Nothing else.
    """
    try:
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(prompt)
        new_mood = response.text.strip().lower()
        valid_moods = ["weary", "nostalgic", "accepting", "fading", "angry", "afraid", "hallucinating", "regretful"]
        for valid_mood in valid_moods:
            if valid_mood in new_mood:
                return valid_mood
    except Exception:
        pass
        
    return current_mood

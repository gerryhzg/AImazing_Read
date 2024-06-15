import os
from gtts import gTTS
from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_voice(text, character='default'):
    tts = gTTS(text, lang='en', tld=character)
    audio_path = save_audio(tts)
    return audio_path

def save_audio(tts):
    audio_directory = "static/audio"
    os.makedirs(audio_directory, exist_ok=True)
    audio_path = os.path.join(audio_directory, "audio.mp3")
    tts.save(audio_path)
    return audio_path

@app.route('/api/generate-voice', methods=['POST'])
def generate_voice_endpoint():
    data = request.get_json()
    text = data.get('text')
    character = data.get('character', 'default')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    audio_path = generate_voice(text, character)
    audio_url = request.host_url + audio_path
    return jsonify({'audio_url': audio_url})

if __name__ == '__main__':
    app.run(debug=True)

###########
# run and test the code:
# python text_to_speech_with_effects.py
# curl -X POST http://127.0.0.1:5000/api/generate-voice -H "Content-Type: application/json" -d '{"text": "Hello, this is a test.", "character": "co.uk"}'

###############
# Here are some examples of the tld (Top-Level Domain) parameter which changes the accent:

# "com" (default) - American English
# "co.uk" - British English
# "ca" - Canadian English
# "com.au" - Australian English
# "co.in" - Indian English
# Additionally, gTTS supports various languages which can also provide different voices:

# "en" - English
# "fr" - French
# "de" - German
# "es" - Spanish
# "it" - Italian
# "pt" - Portuguese
# "ru" - Russian
# "hi" - Hindi
# "ja" - Japanese
# "ko" - Korean
# "zh-CN" - Chinese (Mandarin)
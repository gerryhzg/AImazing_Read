import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the Musicfy API key from environment variables
MUSICFY_API_KEY = os.getenv('MUSICFY_API_KEY')

def generate_music(text):
    headers = {
        'Authorization': f'Bearer {MUSICFY_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "prompt": text,
        "duration": 15  # Duration of the generated audio in seconds
    }
    response = requests.post('https://api.musicfy.lol/v1/generate-music', headers=headers, json=payload)
    
    if response.status_code == 200:
        # Check if response is a list and access the first item
        response_data = response.json()
        if isinstance(response_data, list) and len(response_data) > 0:
            audio_url = response_data[0].get('file_url')
            return audio_url
        else:
            raise ValueError("Unexpected response format: {}".format(response_data))
    else:
        response.raise_for_status()    

@app.route('/api/generate-audio', methods=['POST'])
def generate_audio_endpoint():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        audio_url = generate_music(text)
        return jsonify({'audio_url': audio_url})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except ValueError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


#########
#this program will listen to /api/generate-audio for POST method, get the text and generate a 15 sec music based on the text
#then it will return the url of the generated music in json in audio_url
#sample curl
#  curl -X POST http://127.0.0.1:5000/api/generate-audio -H "Content-Type: application/json" -d '{"text": "A calm forest with birds chirping"}'


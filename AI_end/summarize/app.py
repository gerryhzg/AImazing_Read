from openai import OpenAI
import requests
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

api_file = open("api_key.txt", "r")
api_key_str = api_file.read()
client = OpenAI(api_key = api_key_str)

def summarize_text(text, prompt, max_tokens=500):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}:\n\n{text}\n\nKids Story:",
            }
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].message
    return summary

# Endpoint to receive text and return summarized text
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    prompt = data.get('prompt', 'Summarize the following text for kids:')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    summary = summarize_text(text, prompt)

    # # Send summarized text to another API
    # another_api_url = 'https://example.com/receive_summary'
    # response = requests.post(another_api_url, json={'summary': summary})
    
    # if response.status_code != 200:
    #     return jsonify({'error': 'Failed to send summary to another API'}), 500
    
    return jsonify({'summary': summary.content})

if __name__ == '__main__':
    app.run(debug=True)
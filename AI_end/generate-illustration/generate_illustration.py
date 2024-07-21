import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import re

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_prompt(text):
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a descriptive prompt for an illustration based on the following text:\n\n{text}"}
    ],
    max_tokens=100
    )

    prompt = response.choices[0].message.content.strip()
    return prompt

def generate_image(prompt):
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url

def save_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        raise Exception(f"Failed to download image: {response.status_code}")

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def sanitize_filename(text, max_length=50):
    # Replace spaces with underscores and remove invalid characters
    filename = re.sub(r'[^\w\-_\. ]', '', text[:max_length].replace(' ', '_'))
    return filename + '.png'

@app.route('/api/generate-illustration', methods=['POST'])
def generate_illustration_endpoint():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        prompt = generate_prompt(text)
        image_url = generate_image(prompt)

        # Define the save path
        save_dir = "../Media/Images"
        os.makedirs(save_dir, exist_ok=True)
        clear_folder(save_dir)

        # image_name = f"{text[:50].replace(' ', '_')}.png"  # Create a filename from the first 50 characters of the text
        image_name = sanitize_filename(text)
        save_path = os.path.join(save_dir, image_name)

        # Save the image
        save_image(image_url, save_path)

        return jsonify({'image_url': image_url})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except openai.OpenAIError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

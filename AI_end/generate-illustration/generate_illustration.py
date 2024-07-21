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

#####sample curl
# curl -X POST http://127.0.0.1:5000/api/generate-illustration \
# -H "Content-Type: application/json" \
# -d @- << 'EOF'
# {
#   "text": "Peppa Pig and the Secret Ingredient Adventure\nPeppa: \"Hello, everyone! Today, we have a fun story about something very interesting. Do you know what tumors are? They're tiny little things that can grow inside our bodies, and they need a special ingredient to grow, just like how our cakes need sugar to be sweet!\"\nGeorge: \"Ooh, what's the special ingredient, Peppa?\"\nPeppa: \"It's called acetate! Imagine you're making a magic potion, and acetate is the magic dust that makes it work. Tumors use this acetate to grow bigger and stronger.\"\nGeorge: \"Wow, that's interesting! But how do they get this magic dust?\"\nPeppa: \"Great question, George! Scientists found out that there's a little helper called ACSS2. This helper is like a tiny worker that grabs the acetate from our food and gives it to the tumors.\"\nGeorge: \"And what did the scientists do next?\"\nPeppa: \"They did a clever experiment with mice! They took away the ACSS2 helper from the mice. Guess what happened? The tumors couldn't get their special ingredient and stayed small!\"\nGeorge: \"That's great news, Peppa! What does it mean for us?\"\nPeppa: \"It means scientists can make medicines to block the ACSS2 helper. It's like finding a way to stop the magic potion from working, so the tumors can't grow anymore. Isn't that cool?\"\nGeorge: \"That's amazing, Peppa! Scientists are like real-life superheroes!\"\nPeppa: \"They sure are, George! And that's our fun story for today, everyone. Remember, science can do wonderful things!\"\nGeorge: \"Bye-bye, everyone!\"\nPeppa and George: \"Oink, oink!\""
# }
# EOF

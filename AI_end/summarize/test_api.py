import requests

# URL of the locally running Flask server
url = 'http://127.0.0.1:5000/summarize'

print('API is running on', url)
print('\n\n')

# Text to be summarized
file_input = open("D:\AImazing_Read\AI_end\summarize\input.txt", 'r', encoding='UTF-8')
text_to_summarize = file_input.read()

custom_prompt = 'give me 10 sentences to summarize the story. these 10 sentences are vivid and suitable as 10 promts to generate comics through Stable Diffusion'

# Make a POST request to the Flask server
response = requests.post(url, json={'text': text_to_summarize, 'prompt': custom_prompt})

print('Your input:\n', text_to_summarize)
print('\n\n')

print('Your prompt:\n', custom_prompt)
print('\n\n')

# Print the response from the server
if response.status_code == 200:
    summary = response.json().get('summary')
    print("Summary:\n", summary)
else:
    error = response.json().get('error')
    print("Error:", error)
    
    
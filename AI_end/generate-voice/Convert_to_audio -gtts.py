

from gtts import gTTS
import os

def translate_to_prompt(paragraph):
    # For simplicity, return the paragraph as the prompt
    return paragraph

def generate_speech(text, lang='en'):
 """Generate speech from text using gTTS and return it as in-memory audio."""
    tts = gTTS(text=text, lang=lang)
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)  # Rewind the buffer to the beginning
    return audio_io

def save_audio(audio_io, file_path):
    """Save the in-memory audio data to an MP3 file."""
    with open(file_path, 'wb') as f:
        f.write(audio_io.read())

def generate_voice_from_summary(summary_dict):
    generated_files = {}
    
for key, paragraph in summary_dict.items():
        # Translate the paragraph to a prompt (if needed)
        prompt = translate_to_prompt(paragraph)
        
        # Generate speech and get in-memory audio data
        audio_io = generate_speech(prompt)
        
        # Store the in-memory audio data in a dictionary
        generated_files[key] = audio_io
    
    return generated_files

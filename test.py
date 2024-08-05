
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:53:46 2024

@author: luyang
"""

# import py packages
import os
import time

# import all functions
# import func01_summarize as summ
# import func02_generate_image as image
# import func03_generate_music as music
# import func04_generate_voice as voice
# import func05_generate_final_product as result

from flask import Flask, request, jsonify ,send_from_directory
from flask_cors import CORS


# Global Input - a user-specified document
file_path = 'THE LOCAL MULTIPLIER IN THE STATE OF OHIO.docx'



app = Flask(__name__,static_url_path="/AI_end/",static_folder="Media/")
CORS(app)

@app.route('/')
def root():
    return "Connection Successful!"

@app.route('/AI_end/Media/Images/<path:filename>')
def serve_image(filename):
    return send_from_directory('AI_end/Media/Images', filename)

@app.route('/AI_end/Media/BackgroundMusic/<path:filename>')
def serve_bgmusic(filename):
    return send_from_directory('AI_end/Media/BackgroundMusic', filename)

@app.route('/AI_end/Media/VoiceAudio/<path:filename>')
def serve_voice(filename):
    return send_from_directory('AI_end/Media/VoiceAudio', filename)

@app.route('/generate', methods=['POST'])

def main():
    
    time.sleep(3)

    return jsonify(Video = "" ,Images = ["http://127.0.0.1:5000/AI_end/Media/Images/generated_image_1.png","http://127.0.0.1:5000/AI_end/Media/Images/generated_image_2.png"] ,Content = ["Peppa Pig and the Secret Ingredient Adventure","Peppa: \"Hello, everyone! Today, we have a fun story about something very interesting. Do you know what tumors are? They're tiny little things that can grow inside our bodies, and they need a special ingredient to grow, just like how our cakes need sugar to be sweet!"] , Voices = ["",""] ,Bgm = "")

if __name__ == '__main__':
    app.run(debug=True)
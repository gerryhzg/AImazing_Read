
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
import func01_summarize as summ
import func02_generate_image as image
import func03_generate_music as music
import func04_generate_voice as voice
import func05_generate_final_product as result

from flask import Flask, request, jsonify ,send_from_directory
from flask_cors import CORS, cross_origin


app = Flask(__name__,static_url_path="/AI_end/",static_folder="Media/")
CORS(app, resources={r"/generate": {"origins": "http://localhost:3000"}})  # Allow only example.com
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/AI_end/Media/Video/<path:filename>')
def serve_video(filename):
    return send_from_directory('AI_end/Media/Video', filename)

@app.route('/generate', methods=['POST'])
@cross_origin()
def main():

    Content = request.get_json()["Content"]

    SummaryList = []
    ImageUrlList = result.GetImageUrls()
    VoiceUrlList = result.GetVoiceUrls()

    chatgpt_api_key_file = "chatgpt_api_key.txt"
    summary = summ.summarize_text(Content, api_key = chatgpt_api_key_file , max_tokens=500, model="gpt-3.5-turbo")

    bgmUrl = "http://localhost:5000/AI_end/Media/BackgroundMusic/" + music.generate_bgm(summary, dalle_api_key_file)

    dalle_api_key_file = 'dalle_api_key.txt'
    images = image.generage_image_dalle(summary, dalle_api_key_file)

    voices = voice.generate_voice(summary)

    for Sentence in summary.values():
        SummaryList.append(Sentence)

    VideoUrl = result.Combine(SummaryList)

    return jsonify(Video = VideoUrl ,Images = ImageUrlList ,Content = SummaryList , Voices = VoiceUrlList ,Bgm = bgmUrl)

if __name__ == '__main__':
    app.run(debug=True)
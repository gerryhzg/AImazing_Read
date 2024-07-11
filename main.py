#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:53:46 2024

@author: luyang
"""

# import py packages
import os

# import all functions
import func01_summarize as summ
import func02_generate_image as image
import func03_generate_music as music
import func04_generate_voice as voice


# Global Input - a user-specified document
file_path = 'THE LOCAL MULTIPLIER IN THE STATE OF OHIO.docx'

# Module 1 - Generate summarization
# Input: user-specified document
# Output: 'summary' - a Python dictionary
# Description: Each value of 'summary' is the text on each page of the final product.
#              indexed by numbers starting from 1.
chatgpt_api_key_file = "chatgpt_api_key.txt"
summary = summ.summarize_text(file_path, api_key = chatgpt_api_key_file , max_tokens=500, model="gpt-3.5-turbo")

# Module 2 - Generate images
# Input: 'summary'
# Output: 'images' - a Python dictionary
# Description: Each value of 'images' is the image on each page of the final product.
#              indexed by numbers starting from 1.
dalle_api_key_file = 'dalle_api_key.txt'
images = image.generage_image_dalle(summary, dalle_api_key_file)


# Module 3 - Generate BGM
# Input: 'summary'
# Output: 'bgms' - a Python dictionary
# Description: Each value of 'bgms' is the background music associated with each page of the final product.
#              indexed by numbers starting from 1.
bgms = music.generate_bgm(summary, ohter inputs)


# Module 4 - Text to Speech
# Input: 'summary'
# Output: 'Speech' - a Python dictionary
# Description: Each value of 'images' is the read-out of text on each page of the final product, 
#              indexed by numbers starting from 1.
voices = voice.generate_voice(summary, other inputs)


# combine multimedia 
# Task is to combine all 4 elements (summary, image, bgm, voice) by aligning the keys of each Py dictionary.
# e.g. The first page of our final product consist of summary[1], images[1], bgms[1] and voices[1].
# maybe this step can be done in the GUI?
final_product = combine(images[0], summary, musics, voices)





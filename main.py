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




# generate summarization

# Full path to the input file
file_input = "input.pdf"

# Prompt
custom_prompt = 'give me 10 sentences to summarize the story. these 10 sentences are vivid and suitable as 10 promts to generate comics through Stable Diffusion'

summary = summ.summarize_text(file_input, custom_prompt)

summary = generate_sumary(input1, input2)


# generate images


# 定义角色描述
character_description = 'A young wizard with a blue robe, holding a magic wand, with a pointy hat and glasses'

# 定义不同场景
scenes = ["standing in a magical forest", 
          "casting a spell in a dark cave", 
          "riding a flying broomstick over a city", 
          "studying ancient scrolls in a library"
          ]

# synthetic input - 'summary' as a list of paragraphs, suppose generate_image_dalle() can translate each paragraph to a prompt
summary = [character_description + s for s in scenes]

# file path and name of the api key
api_key_file = '/Users/luyang/Desktop/AImazing_Read/AI_end/generate-illustration/dalle_api_key.txt'

# execute function that generates images
images = image.generage_image_dalle(summary, api_key_file)


# generate music
musics = generate_music(summary, inputs)


# generate voice

voices = generate_voice(summary, inputs)

# combine multimedia 

final_product = combine(images[0], summary, musics, voices)





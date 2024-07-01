#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:58:55 2024

@author: luyang
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:50:04 2024

@author: Mingda Wang
"""

# 安装必要的库
# =============================================================================
# !pip install openai==0.28.0
# !pip install openai
# 
# =============================================================================
# 导入库
import openai
from IPython.display import display
import requests
from PIL import Image as PILImage
from io import BytesIO


def translate_to_prompt(paragraph):
    # place holder
    prompt = paragraph
    return prompt

# 定义函数来调用 DALL-E API 并显示生成的图像
def generate_1_image_dalle(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response['data'][0]['url']
    image_response = requests.get(image_url) 
    img = PILImage.open(BytesIO(image_response.content)).convert('RGBA') 
    return img


def sav_img(img, filename):
    img.save(filename) 
    return
    

def generage_image_dalle(summary, api_key_file):
    f = open(api_key_file, "r")
    api_key = f.read()
    openai.api_key = api_key
    
    images = {}
    for i, paragraph in enumerate(summary, start=1):
        prompt = translate_to_prompt(paragraph)
        images[i] = generate_1_image_dalle(prompt)
        filename = f"generated_image_{i}.png" 
        images[i].save(filename)
        display(PILImage.open(filename))
        
    return images
    
    
    
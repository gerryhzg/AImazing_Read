# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:50:04 2024

@author: Mingda Wang
"""

# 安装必要的库
!pip install openai==0.28.0
!pip install openai

# 导入库
import openai
from IPython.display import display
import requests
from PIL import Image as PILImage
from io import BytesIO

# 设置你的 OpenAI API 密钥
openai.api_key = 

# 定义函数来调用 DALL-E API 并显示生成的图像
def generate_image(prompt, filename):
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # 生成图像的数量
        size="1024x1024"  # 图像大小
    )
    image_url = response['data'][0]['url']

    # 下载图像并保存
    image_response = requests.get(image_url)
    img = PILImage.open(BytesIO(image_response.content)).convert('RGBA')
    img.save(filename)

    return filename

# 定义角色描述
character_description = "A young wizard with a blue robe, holding a magic wand, with a pointy hat and glasses"

# 定义不同场景
scenes = [
    "standing in a magical forest",
    "casting a spell in a dark cave",
    "riding a flying broomstick over a city",
    "studying ancient scrolls in a library"
]

# 生成每张图像，包括角色和场景描述
for i, scene in enumerate(scenes, start=1):
    prompt = f"{character_description}, {scene}"
    filename = f"generated_image_{i}.png"
    generate_image(prompt, filename)
    display(PILImage.open(filename))
    
    
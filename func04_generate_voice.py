# =============================================================================
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Jun 30 12:01:29 2024
# 
# @author: Qiong Li, Xiang
# """

# 模块一：定义将段落翻译为提示词的函数
def translate_to_prompt(paragraph):
    # 简单返回段落作为提示词
    return paragraph


    # 模块二：定义调用并生成声音的函数
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf
import requests
from io import BytesIO

def generate_1_voice(prompt, description, model_name, output_file, max_new_tokens=5000):

  # Load model and tokenizer
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    model = ParlerTTSForConditionalGeneration.from_pretrained(model_name, force_download=True).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # 处理输入
    input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
    prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    
    # 生成语音
    generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids, max_new_tokens=max_new_tokens)
    audio_arr = generation.cpu().numpy().squeeze()
    
    # 保存音频文件
    sf.write(output_file, audio_arr, model.config.sampling_rate)
    return output_file
    
# 模块三：定义新的调用ParlerTTSForConditionalGeneration并生成声音的函数（使用API密钥文件）

def generate_1_voice_new(prompt, description, model_name, output_file, api_key_file, max_new_tokens=5000):
    # 加载模型和分词器
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    model = ParlerTTSForConditionalGeneration.from_pretrained(model_name, force_download=True).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # 处理输入
    input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
    prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    
    # 从API密钥文件中读取密钥
    with open(api_key_file, "r") as f:
        api_key = f.read().strip()
    
    # 调用API生成语音
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "input_ids": input_ids.tolist(),
        "prompt_input_ids": prompt_input_ids.tolist(),
        "max_new_tokens": max_new_tokens
    }
    response = requests.post("https://api.parler-tts.com/generate", headers=headers, json=data)
    
    # 处理响应结果
    if response.status_code == 200:
        audio_bytes = BytesIO(response.content)
        audio_arr, sr = sf.read(audio_bytes)
        sf.write(output_file, audio_arr, sr)
        print(f"语音生成成功并保存至 {output_file}")
    else:
        print(f"生成语音失败：{response.text}")

# 模块四：定义根据摘要生成声音的函数
def generate_voice_from_summary(summary_dict, api_key_file):
    generated_files = {}
    
    for key, paragraph in summary_dict.items():
        prompt = translate_to_prompt(paragraph)
        output_file = f"generated_audio_{key}.wav"
        generate_1_voice_new(prompt, paragraph, model_name, output_file, api_key_file)
        generated_files[key] = output_file
    
    return generated_files
# 
# 
# 
# =============================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:59:24 2024

@author: Zhaoyan, Liang Han
"""

from openai import OpenAI
from flask import Flask, request, jsonify
import requests

import mimetypes
import fitz
from docx import Document
import re


app = Flask(__name__)

api_file = open("api_key.txt", "r")
api_key_str = api_file.read()

client = OpenAI(api_key = api_key_str)

prompt = 'give me 10 sentences to summarize the story. these 10 sentences are vivid and suitable as 10 promts to generate comics through Stable Diffusion'

def summarize_text(file_path, prompt, max_tokens=500):
    
    text = read_document(file_path)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}:\n\n{text}\n\nKids Story:",
            }
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].message
    return summary

def read_document(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type == 'application/pdf':
        return read_pdf(file_path)
    elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return read_docx(file_path)
    elif mime_type == 'text/plain':
        return read_txt(file_path)
    else:
        return "File type not supported."

def read_pdf(file_path):
    """
    Reads the content of a PDF file.
    """
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    return text

def read_docx(file_path):
    """
    Reads the content of a DOCX file.
    """
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file_path):
    """
    Reads the content of a TXT file.
    """
    file_input = open(file_path, 'r', encoding='UTF-8')
    text = file_input.read()
    return text



# Endpoint to receive text and return summarized text
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    prompt = data.get('prompt', 'Summarize the following text for kids:')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    summary = summarize_text(text, prompt)

    # # Send summarized text to another API
    # another_api_url = 'https://example.com/receive_summary'
    # response = requests.post(another_api_url, json={'summary': summary})
    
    # if response.status_code != 200:
    #     return jsonify({'error': 'Failed to send summary to another API'}), 500
    
    return jsonify({'summary': summary.content})

if __name__ == '__main__':
    app.run(debug=True)
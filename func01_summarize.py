#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:59:24 2024

@author: Zhaoyan, Liang Han
"""

from openai import OpenAI
import requests

import mimetypes
import fitz
from docx import Document
import re


# Define methods that read an input file in different format
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


def engineer_prompt_summary():
    #prompt engineering part
    prompt_preset = 'give me 10 sentences to summarize the story, using simple words so that reader with elementory school level vocabulary can understand'
    
    return prompt_preset


def divide_paragraphs(text):
    # divide the text to multiple paragraphs and save as a Python dictionary
    # Each page in the final output has one paragraph.
    # 
    # MVP version is to divide by period.
    sliced_text = {}
    for i, p in enumerate(text.split('.'), start=1):
        if p != '':
            sliced_text[i] = p + '.'
        else:
            sliced_text[i] = 'The End'
        
    return sliced_text


# Define a method that summarize a long text
def summarize_text(file_path, api_key = "chatgpt_api_key.txt", max_tokens=500, model="gpt-3.5-turbo"):
    
    text = read_document(file_path)
    
    api_file = open(api_key, "r")
    api_key_str = api_file.read()
    client = OpenAI(api_key = api_key_str)
    
    prompt_preset = engineer_prompt_summary()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"{prompt_preset}:\n\n{text}\n\nKids Story:",
            }
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = divide_paragraphs(response.choices[0].message.content)
    return summary




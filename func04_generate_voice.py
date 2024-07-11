#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:01:29 2024

@author: Qiong Li, Xiang
"""


# =============================================================================
# pip install google-cloud-language
# =============================================================================

import boto3
from google.cloud import language_v1
from google.oauth2 import service_account
import re
import os


class TextToSpeech:
    def __init__(self, key_path):
        self.key_path = key_path
        self.credentials = service_account.Credentials.from_service_account_file(key_path)
        self.client = language_v1.LanguageServiceClient(credentials=self.credentials)

    def analyze_sentiments(self, text):
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentences = self.client.analyze_sentiment(request={'document': document}).sentences
        return [(sentence.text.content, sentence.sentiment.score) for sentence in sentences]

    def split_into_sentences(self, text):
        return re.split(r'(?<=[.!?]) +', text)

    def generate_ssml(self, sentences_with_scores):
        ssml_sentences = []
        for sentence, score in sentences_with_scores:
            if score > 0.5:
                prosody = "<prosody rate='medium' pitch='high'>{}</prosody>".format(sentence)
            elif score < -0.5:
                prosody = "<prosody rate='slow' pitch='medium'>{}</prosody>".format(sentence)
            else:
                prosody = "<prosody rate='medium' pitch='medium'>{}</prosody>".format(sentence)
            ssml_sentences.append(prosody)
        return "<speak>{}</speak>".format(" ".join(ssml_sentences))

    def synthesize_speech(self, ssml_text, output_file='speech.mp3'):
        polly = boto3.client('polly')
        response = polly.synthesize_speech(
            Text=ssml_text,
            OutputFormat='mp3',
            VoiceId='Joanna',
            TextType='ssml'
        )
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
        os.system(f"start {output_file}")

    def process_text(self, text, output_file='speech.mp3'):
        sentence_moods = self.analyze_sentiments(text)
        ssml_text = self.generate_ssml(sentence_moods)
        self.synthesize_speech(ssml_text, output_file)


from text_to_speech import TextToSpeech

def main():
    key_path = r"C:\Users\joanna\Documents\Chase_AI_team\sentiment-auth.json"
    text = "I'm so happy today! But I was sad yesterday. Wow, what a nice trip."

    tts = TextToSpeech(key_path)
    tts.process_text(text)

if __name__ == "__main__":
    main()




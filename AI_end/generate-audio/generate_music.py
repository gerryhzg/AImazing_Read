#!/usr/bin/env python
# coding: utf-8

# In[6]:


# ===================================================================
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Jun 30 12:01:29 2024
# 
# @author: Rin Hayashi
# """
#
#
# Installation of libarary============================================
#!pip install simpleaudio  
#!pip install vaderSentiment
#!pip install pydub
#=====================================================================
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

from pydub import AudioSegment
import simpleaudio as sa

# ===Function to analyze summary and generate sentiment
#
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment
#
# === Function needed when play the mp3 music file
def play_mp3(file_path):

     audio = AudioSegment.from_file(file_path, format="mp3")

# Play the audio file
     play_obj = sa.play_buffer(audio.raw_data, 
                          num_channels=audio.channels,
                          bytes_per_sample=audio.sample_width,
                          sample_rate=audio.frame_rate)
#
# === Function to genetate BGM based on music, the prepared mp3 files are for 20 seconds
#    
def generate_bgm(summary_text):
    sentiment = get_sentiment(summary_text)
    # Determine which MP3 file to play based on sentiment
    if sentiment['compound'] >= 0.05:
        bgm = 'PositiveHappy.mp3'  # Replace with the path to your positive sentiment MP3 file
    elif sentiment['compound'] <= -0.05:
        bgm = 'NegativeSad.mp3'  # Replace with the path to your negative sentiment MP3 file
    else:
        bgm = 'NeutralRelax.mp3'  # Replace with the path to your neutral sentiment MP3 file

    return bgm
    
if __name__ == '__main__':
      summary_text = input("Enter text to analyze sentiment: ")

##    print(f"Playing {bgm} for sentiment: {sentiment['compound']}")
      bgm=generate_bgm(summary_text)
      play_mp3(bgm)
    


# In[ ]:





# In[ ]:





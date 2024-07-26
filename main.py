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
import func05_generate_final_product as result


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
# summary = {1: "Peppa Pig and the Secret Ingredient Adventure\nPeppa: \"Hello, everyone! Today, we have a fun story about something very interesting. Do you know what tumors are? They're tiny little things that can grow inside our bodies, and they need a special ingredient to grow, just like how our cakes need sugar to be sweet!\"\nGeorge: \"Ooh, what's the special ingredient, Peppa?\"\nPeppa: \"It's called acetate! Imagine you're making a magic potion, and acetate is the magic dust that makes it work. Tumors use this acetate to grow bigger and stronger.\"\nGeorge: \"Wow, that's interesting! But how do they get this magic dust?\"\nPeppa: \"Great question, George! Scientists found out that there's a little helper called ACSS2. This helper is like a tiny worker that grabs the acetate from our food and gives it to the tumors.\"\nGeorge: \"And what did the scientists do next?\"\nPeppa: \"They did a clever experiment with mice! They took away the ACSS2 helper from the mice. Guess what happened? The tumors couldn't get their special ingredient and stayed small!\"\nGeorge: \"That's great news, Peppa! What does it mean for us?\"\nPeppa: \"It means scientists can make medicines to block the ACSS2 helper. It's like finding a way to stop the magic potion from working, so the tumors can't grow anymore. Isn't that cool?\"\nGeorge: \"That's amazing, Peppa! Scientists are like real-life superheroes!\"\nPeppa: \"They sure are, George! And that's our fun story for today, everyone. Remember, science can do wonderful things!\"\nGeorge: \"Bye-bye, everyone!\"\nPeppa and George: \"Oink, oink!\""} 
summary = {1: "Peppa Pig and the Secret Ingredient Adventure", 2: "Peppa: \"Hello, everyone! Today, we have a fun story about something very interesting. Do you know what tumors are? They're tiny little things that can grow inside our bodies, and they need a special ingredient to grow, just like how our cakes need sugar to be sweet!\"", 3: "George: \"Ooh, what's the special ingredient, Peppa?\"", 4: "Peppa: \"It's called acetate! Imagine you're making a magic potion, and acetate is the magic dust that makes it work. Tumors use this acetate to grow bigger and stronger.\"", 5: "George: \"Wow, that's interesting! But how do they get this magic dust?\"", 6: "Peppa: \"Great question, George! Scientists found out that there's a little helper called ACSS2. This helper is like a tiny worker that grabs the acetate from our food and gives it to the tumors.\"", 7: "George: \"And what did the scientists do next?\"", 8: "Peppa: \"They did a clever experiment with mice! They took away the ACSS2 helper from the mice. Guess what happened? The tumors couldn't get their special ingredient and stayed small!\"", 9: "George: \"That's great news, Peppa! What does it mean for us?\"", 10: "Peppa: \"It means scientists can make medicines to block the ACSS2 helper. It's like finding a way to stop the magic potion from working, so the tumors can't grow anymore. Isn't that cool?\"", 11: "George: \"That's amazing, Peppa! Scientists are like real-life superheroes!\"", 12: "Peppa: \"They sure are, George! And that's our fun story for today, everyone. Remember, science can do wonderful things!\"", 13: "George: \"Bye-bye, everyone!\"", 14: "Peppa and George: \"Oink, oink!\""} 
dalle_api_key_file = 'dalle_api_key.txt'
images = image.generage_image_dalle(summary, dalle_api_key_file)


# Module 3 - Generate BGM
# Input: 'summary'
# Output: 'bgms' - a Python dictionary
# Description: Each value of 'bgms' is the background music associated with each page of the final product.
#              indexed by numbers starting from 1.
summary = {1: "Peppa Pig and the Secret Ingredient Adventure", 2: "Peppa: \"Hello, everyone! Today, we have a fun story about something very interesting. Do you know what tumors are? They're tiny little things that can grow inside our bodies, and they need a special ingredient to grow, just like how our cakes need sugar to be sweet!\"", 3: "George: \"Ooh, what's the special ingredient, Peppa?\"", 4: "Peppa: \"It's called acetate! Imagine you're making a magic potion, and acetate is the magic dust that makes it work. Tumors use this acetate to grow bigger and stronger.\"", 5: "George: \"Wow, that's interesting! But how do they get this magic dust?\"", 6: "Peppa: \"Great question, George! Scientists found out that there's a little helper called ACSS2. This helper is like a tiny worker that grabs the acetate from our food and gives it to the tumors.\"", 7: "George: \"And what did the scientists do next?\"", 8: "Peppa: \"They did a clever experiment with mice! They took away the ACSS2 helper from the mice. Guess what happened? The tumors couldn't get their special ingredient and stayed small!\"", 9: "George: \"That's great news, Peppa! What does it mean for us?\"", 10: "Peppa: \"It means scientists can make medicines to block the ACSS2 helper. It's like finding a way to stop the magic potion from working, so the tumors can't grow anymore. Isn't that cool?\"", 11: "George: \"That's amazing, Peppa! Scientists are like real-life superheroes!\"", 12: "Peppa: \"They sure are, George! And that's our fun story for today, everyone. Remember, science can do wonderful things!\"", 13: "George: \"Bye-bye, everyone!\"", 14: "Peppa and George: \"Oink, oink!\""} 
dalle_api_key_file = 'dalle_api_key.txt'
bgms = music.generate_bgm(summary, dalle_api_key_file)


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
final_product = result.combine(images, summary, bgms, voices)





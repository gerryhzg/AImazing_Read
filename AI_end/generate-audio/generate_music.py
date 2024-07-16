{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c6d49bfc-c2e9-4270-92c8-6d0b07bda999",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'simpleaudio'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 20\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtime\u001b[39;00m\n\u001b[0;32m     19\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mpydub\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m AudioSegment\n\u001b[1;32m---> 20\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msimpleaudio\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01msa\u001b[39;00m\n\u001b[0;32m     22\u001b[0m \u001b[38;5;66;03m# ===Function to analyze summary and generate sentiment\u001b[39;00m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;66;03m#\u001b[39;00m\n\u001b[0;32m     24\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_sentiment\u001b[39m(text):\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'simpleaudio'"
     ]
    }
   ],
   "source": [
    "# ===================================================================\n",
    "# #!/usr/bin/env python3\n",
    "# # -*- coding: utf-8 -*-\n",
    "# \"\"\"\n",
    "# Created on Sun Jun 30 12:01:29 2024\n",
    "# \n",
    "# @author: Rin Hayashi\n",
    "# \"\"\"\n",
    "#\n",
    "#\n",
    "# Installation of libarary============================================\n",
    "#!pip install simpleaudio  \n",
    "#!pip install vaderSentiment\n",
    "#!pip install pydub\n",
    "#=====================================================================\n",
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer\n",
    "import time\n",
    "\n",
    "from pydub import AudioSegment\n",
    "import simpleaudio as sa\n",
    "\n",
    "# ===Function to analyze summary and generate sentiment\n",
    "#\n",
    "def get_sentiment(text):\n",
    "    analyzer = SentimentIntensityAnalyzer()\n",
    "    sentiment = analyzer.polarity_scores(text)\n",
    "    return sentiment\n",
    "#\n",
    "# === Function needed when play the mp3 music file\n",
    "def play_mp3(file_path):\n",
    "\n",
    "     audio = AudioSegment.from_file(file_path, format=\"mp3\")\n",
    "\n",
    "# Play the audio file\n",
    "     play_obj = sa.play_buffer(audio.raw_data, \n",
    "                          num_channels=audio.channels,\n",
    "                          bytes_per_sample=audio.sample_width,\n",
    "                          sample_rate=audio.frame_rate)\n",
    "#\n",
    "# === Function to genetate BGM based on music, the prepared mp3 files are for 20 seconds\n",
    "#    \n",
    "def generate_bgm(summary_text):\n",
    "    sentiment = get_sentiment(summary_text)\n",
    "    # Determine which MP3 file to play based on sentiment\n",
    "    if sentiment['compound'] >= 0.05:\n",
    "        bgm = 'PositiveHappy.mp3'  # Replace with the path to your positive sentiment MP3 file\n",
    "    elif sentiment['compound'] <= -0.05:\n",
    "        bgm = 'NegativeSad.mp3'  # Replace with the path to your negative sentiment MP3 file\n",
    "    else:\n",
    "        bgm = 'NeutralRelax.mp3'  # Replace with the path to your neutral sentiment MP3 file\n",
    "\n",
    "    return bgm\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "      summary_text = input(\"Enter text to analyze sentiment: \")\n",
    "\n",
    "##    print(f\"Playing {bgm} for sentiment: {sentiment['compound']}\")\n",
    "      bgm=generate_bgm(summary_text)\n",
    "      play_mp3(bgm)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df04201a-f052-4fbb-8307-2c6beaa12c0a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "620cd691-b67b-4ee9-a505-d1132ed635c7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

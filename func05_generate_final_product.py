import cv2
import numpy as np
from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip, TextClip
import wave

import os 


def get_duration_wave(file_path):

    with wave.open(file_path, 'r') as audio_file:
        frame_rate = audio_file.getframerate()
        n_frames = audio_file.getnframes()
        duration = n_frames / float(frame_rate)
    
    return float(f"{duration:.2f}")

def combine(images , summary, bgms:list[str], voice):

    pass

def combineAudios(bgms:list[str], voices:list[str]):

    return

def Video( images:list[str] , summary:list[str], bgms:list[str], voices:list[str] ):

    VideoLength = 0

    VoicesLength = []

    for voice in voices:

        TimeLength = get_duration_wave(voice)

        VideoLength += TimeLength

        VoicesLength.append()

    FirstFrame = cv2.imread(images[0])

    VideoWidth , VideoHeight = FirstFrame.shape[1],FirstFrame.shape[0]

    # Create a video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (image.shape[1], image.shape[0]))

    for Index,ImagePath in enumerate(images):

        # Load the image
        image = cv2.imread(ImagePath)

        image = cv2.resize(image,(VideoWidth,VideoHeight))

        # Create a 30-second video
        for i in range( (VoicesLength[Index]+2) * 30 ):
            video.write(image)

    # Release the video writer
    video.release()

    # Load the audio file
    audio = AudioFileClip(bgms[0])

    # Create the subtitle text
    subtitle_text = "This is a 30-second video with subtitles."
    subtitle = TextClip(subtitle_text, fontsize=36, color='white')
    subtitle = subtitle.set_position(('center', 'bottom')).set_duration(30).set_start(3)

    # Create the final video clip
    final_clip = ImageSequenceClip([image] * (30 * 30), fps=30)
    final_clip = final_clip.set_audio(audio)
    final_clip = final_clip.set_subtitle(subtitle)

    # Write the final video to a file
    final_clip.write_videofile('output_video_with_audio_and_subtitles.mp4')

def display():

    pass
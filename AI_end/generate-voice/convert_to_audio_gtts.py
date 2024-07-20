pip install gtts


from gtts import gTTS
import os
# text = "Hello, how are you?"
## Original Windows-style path
# think about other text files from the other path:     
original_path = r'C:\Users\joanna\Documents\Chase_AI_team\Sample_text.txt'
with open(original_path, 'r') as file:
    text = file.read()
tts = gTTS(text=text, lang='en')

current_directory = os.getcwd()
print(f"Current directory of Python file: {current_directory}")

# 创建一个名为"audio_files"的子目录
audio_directory = os.path.join(current_directory, 'audio_files')
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# 将语音保存为MP3文件到"audio_files"目录
file_name = "hello.mp3"
file_path = os.path.join(audio_directory, file_name)
tts.save(file_path)

# 检查文件是否成功保存并播放文件
if os.path.exists(file_path):
    print(f"File saved successfully at {file_path}")
    # 在不同操作系统上播放MP3文件
    if os.name == 'nt':  # Windows
        os.startfile(file_path)
    elif os.name == 'posix':  # macOS or Linux
        if 'darwin' in os.uname().sysname.lower():  # macOS
            os.system(f"afplay {file_path}")
        else:  # Linux
            os.system(f"mpg321 {file_path}")
else:
    print("Failed to save file")








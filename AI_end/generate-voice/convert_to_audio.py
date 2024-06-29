#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install gtts


# In[5]:


from gtts import gTTS
import os
# text = "Hello, how are you?"
## Original Windows-style path
# think about other text files from the other path:     
original_path = r'C:\Users\joanna\Documents\Chase_AI_team\Sample_text.txt'
with open(original_path, 'r') as file:
    text = file.read()
tts = gTTS(text=text, lang='en')


# In[6]:


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


# In[5]:


pip install boto3


# In[3]:


pip install awscli


# In[7]:


import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os

# Initialize the Polly client
polly = boto3.client('polly', region_name='us-east-2')

# The text you want to convert to speech
text = "Hello, how are you today?"

# Synthesize speech
try:
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna',  # Choose a voice ID, e.g., Joanna for a female voice
        TextType='text',
        Engine='standard',  # Use 'neural' for Neural TTS if available
        LanguageCode='en-US'
    )

    # Save the audio to a file
    audio_file = 'output.mp3'
    with open(audio_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    # Play the audio file (for Windows)
    os.system(f"start {audio_file}")

except (BotoCoreError, ClientError) as error:
    print(f"An error occurred: {error}")


# ###how to get the access fo the AmazonPolly
# 
# 1. Open the AWS Management Console
# Go to the AWS Management Console and log in with your credentials.
# 
# 2. Navigate to the IAM Service
# In the AWS Management Console, search for IAM (Identity and Access Management) in the search bar and select it.
# 
# Click on IAM to open the IAM Dashboard.
# 
# 3. Find Your User
# In the IAM Dashboard, click on Users in the left-hand menu.
# Click on the IAM user you created for the AWS CLI (e.g., cli_user).
# 4. Add Permissions
# In the user summary page, click on the Add permissions button.
# 
# Choose Attach policies directly.
# 
# Search for the policy that grants permissions to use Amazon Polly. You can use the AmazonPollyFullAccess managed policy if you want full access to Amazon Polly:
# 
# In the search bar, type AmazonPollyFullAccess.
# Select the checkbox next to AmazonPollyFullAccess.
# Click the Next: Review button.
# Click on the Add permissions button to apply the policy to the user.
# 
# 5. Verify Permissions
# Now that the policy has been attached to the IAM user, you can try running the AWS CLI command again to see if the permissions issue is resolved.

# In[11]:


pip install awscli


# In[8]:


import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os

original_path = r'C:\Users\joanna\Documents\Chase_AI_team\Sample_text.txt'
with open(original_path, 'r') as file:
    text_to_speak = file.read()

# Initialize the Polly client
polly = boto3.client('polly', region_name='us-west-2')  # Replace with your region

# The text you want to convert to speech
text = "Hello, how are you today?"

#  <prosody rate="fast">This is spoken quickly.</prosody>
#   <prosody rate="slow">This is spoken slowly.</prosody>

# <speak>
#   <prosody pitch="x-low">This is spoken with a very low pitch.</prosody>
#   <prosody pitch="x-high">This is spoken with a very high pitch.</prosody>
# </speak>

# <speak>
#   <prosody volume="soft">This is spoken softly.</prosody>
#   <prosody volume="loud">This is spoken loudly.</prosody>
# </speak>

ssml_text = f"""
<speak>
  <prosody rate="slow" pitch="low" volume="loud">{text_to_speak}</prosody>
</speak>
"""

# Synthesize speech
try:
    response = polly.synthesize_speech(
        Text=ssml_text,
        OutputFormat='mp3',
        VoiceId='Matthew',  # Choose a voice ID, e.g., Joanna for a female voice
        TextType='ssml',
        Engine='standard',  # Use 'neural' for Neural TTS if available
        LanguageCode='en-US'
    )

    # Save the audio to a file
    audio_file = 'output.mp3'
    with open(audio_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    # Play the audio file (for Windows)
    os.system(f"start {audio_file}")

except (BotoCoreError, ClientError) as error:
    print(f"An error occurred: {error}")


# In[ ]:





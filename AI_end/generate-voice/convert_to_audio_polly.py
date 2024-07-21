
import os
from google.cloud import language_v1
import boto3

class TextToSpeech:
    def __init__(self, google_credentials_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials_path
        self.language_client = language_v1.LanguageServiceClient()
        self.polly_client = boto3.client('polly')

    def analyze_sentiments(self, text):
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentences = self.language_client.analyze_sentiment(request={'document': document}).sentences
        return [(sentence.text.content, sentence.sentiment.score) for sentence in sentences]

    def create_ssml(self, sentence_moods):
        ssml_text = "<speak>"
        for sentence, score in sentence_moods:
            if score > 0.5:
                ssml_text += f"<prosody rate='medium' pitch='high'>{sentence}</prosody>"
            elif score < -0.5:
                ssml_text += f"<prosody rate='slow' pitch='low'>{sentence}</prosody>"
            else:
                ssml_text += f"<prosody rate='medium' pitch='medium'>{sentence}</prosody>"
        ssml_text += "</speak>"
        return ssml_text

    def synthesize_speech(self, ssml_text, output_filename='speech.mp3'):
        response = self.polly_client.synthesize_speech(
            Text=ssml_text,
            OutputFormat='mp3',
            VoiceId='Joanna',
            TextType='ssml'
        )

        # Save the audio stream
        with open(output_filename, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Saved synthesized speech to {output_filename}")



from text_to_speech import TextToSpeech

def main():
    google_credentials_path = 'path/to/your/service-account-file.json'  # Update this path
    text = "I'm so happy today! But I was sad yesterday."

    tts = TextToSpeech(google_credentials_path)

    # Analyze sentiment for each sentence
    sentence_moods = tts.analyze_sentiments(text)

    # Create SSML with adjustments
    ssml_text = tts.create_ssml(sentence_moods)

    # Synthesize speech and save MP3 file
    tts.synthesize_speech(ssml_text)

if __name__ == "__main__":
    main()


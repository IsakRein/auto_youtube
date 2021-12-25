from gtts import gTTS
from mutagen.mp3 import MP3
import boto3
from contextlib import closing
import os
from data_manager import secret, data_object, save_data_object

class AudioManager:
    def authenticate(self):
        self.polly_client = boto3.Session(
            aws_access_key_id=secret["aws_access_key_id"],
            aws_secret_access_key=secret["aws_secret_access_key"],
            region_name="eu-north-1"
            ).client('polly')

    def save_audio(self, text, path):
        tts = gTTS(text)
        tts.save(path)
        return self.get_audio_length(path)

    def save_audio_production(self, text, path):
        response = self.polly_client.synthesize_speech(
            Engine='standard',
            LanguageCode='en-US',
        	OutputFormat='mp3',
    		TextType='text',
            VoiceId='Matthew',
            Text=text
        )

        data_object["characters_used"] += len(text)
        save_data_object()

        with closing(response["AudioStream"]) as stream:
            with open(path, "wb") as file:
                file.write(stream.read())

        return self.get_audio_length(path)
 
    def get_audio_length(self, path):
        clip = MP3(path)
        return clip.info.length

audio_manager = AudioManager()
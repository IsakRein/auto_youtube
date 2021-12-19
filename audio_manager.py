import pyttsx3
import importlib
from mutagen.aiff import AIFF

class AudioManager:
    def save_audio(self, text, path):
        importlib.reload(pyttsx3)
        self.engine = pyttsx3.init()
        self.engine.save_to_file(text, path)
        self.engine.runAndWait()
        self.engine.stop()
        clip = AIFF(path)
        return clip.info.length


audio_manager = AudioManager()
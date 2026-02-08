from gtts import gTTS
import os

def speak_tamil(text):
    tts = gTTS(text=text, lang='ta')
    audio_file = "output.mp3"
    tts.save(audio_file)

    os.system(f'start {audio_file}')  # Windows play

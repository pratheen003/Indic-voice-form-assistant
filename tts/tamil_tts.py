from gtts import gTTS
import os
from playsound import playsound

def speak_tamil(text):
    os.makedirs("output", exist_ok=True)

    tts = gTTS(text=text, lang='ta')
    audio_path = "output/explanation.mp3"
    tts.save(audio_path)

    playsound(audio_path)


if __name__ == "__main__":
    sample_text = """
    இந்த படிவம் தமிழ் மென்பொருள் சான்றிதழ் பெறுவதற்கான விண்ணப்பப் படிவம்.
    இதில் நிறுவனத்தின் பெயர், முகவரி மற்றும் தொடர்பு விவரங்களை நிரப்ப வேண்டும்.
    """

    speak_tamil(sample_text)

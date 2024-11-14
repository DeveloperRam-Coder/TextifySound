from gtts import gTTS
import os

def text_to_speech(text, filename="audio/output.mp3"):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    print(f"Audio saved as {filename}")

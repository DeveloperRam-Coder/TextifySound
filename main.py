from utils.tts import text_to_speech

# Input text you want to convert
text = "Hello, welcome to the CodeVenture tutorial on text to speech!"
output_path = "audio/speech_output.mp3"
text_to_speech(text, output_path)

import tkinter as tk
from utils.tts import text_to_speech

def on_convert():
    text = text_input.get("1.0", tk.END)
    output_path = "audio/gui_speech_output.mp3"
    text_to_speech(text, output_path)

# GUI setup
root = tk.Tk()
root.title("Text to Speech Converter")

tk.Label(root, text="Enter Text Below:").pack()
text_input = tk.Text(root, height=10, width=40)
text_input.pack()

tk.Button(root, text="Convert to Speech", command=on_convert).pack()
root.mainloop()

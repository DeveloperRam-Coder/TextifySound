from flask import Flask, render_template, request, send_file
from utils.tts import text_to_speech
import os

app = Flask(__name__)

# Define the route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        output_path = "audio/speech_output.mp3"
        
        # Convert text to speech
        text_to_speech(text, output_path)
        
        # Send the audio file for download
        return send_file(output_path, as_attachment=True)
    
    return render_template("index.html")

if __name__ == "__main__":
    # Ensure the audio folder exists
    os.makedirs("audio", exist_ok=True)
    # Run the Flask app
    app.run(debug=True)

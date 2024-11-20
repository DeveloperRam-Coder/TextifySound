from flask import Flask, render_template, request, send_file, jsonify
import pyttsx3
import os

app = Flask(__name__)

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def text_to_speech(text, voice_id, filename="audio/output.mp3"):
    engine.setProperty('voice', voice_id)  # Set the voice to the selected one
    engine.save_to_file(text, filename)
    engine.runAndWait()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        voice_id = request.form["voice"]
        output_path = "audio/speech_output.mp3"

        # Convert text to speech with selected voice
        text_to_speech(text, voice_id, output_path)

        # Send the audio file for download
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    data = request.get_json()
    text = data["text"]
    voice_id = data["voice"]
    output_path = "audio/preview_output.mp3"

    # Preview the speech without saving to a file
    text_to_speech(text, voice_id, output_path)

    # Return the audio file as a response
    return send_file(output_path, mimetype="audio/mp3")

@app.route("/voices", methods=["GET"])
def voices():
    # Get all available voices from pyttsx3
    voices = engine.getProperty('voices')
    voice_list = [{"id": voice.id, "name": voice.name} for voice in voices]
    return jsonify(voice_list)

if __name__ == "__main__":
    # Ensure the audio folder exists
    os.makedirs("audio", exist_ok=True)
    # Run the Flask app
    app.run(debug=True)

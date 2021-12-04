from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json

from asr_model import decode_speech

# Define a flask app
app = Flask(__name__)

sample_rate = 16000
model = Model("../../vosk-api/python/example/model")

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
        f.save(file_path)
        texts = decode_speech(model, file_path, sample_rate)
        text_file = str(f.filename).rsplit(".", 1)[0]
        text_filepath = os.path.join(basepath, 'static','texts', secure_filename(text_file))
        with open(text_filepath, "w") as file:
            print(texts, file=file)
        app.logger.info(f"text::: {texts}")
    return render_template("upload.html", predictions=texts, display_video=f.filename, text_file=text_file) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="5000")
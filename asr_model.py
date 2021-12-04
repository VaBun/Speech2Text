from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json
import argparse


def decode_speech(model, file, sample_rate=16000):
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                file,
                                '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                                stdout=subprocess.PIPE)
    rec = KaldiRecognizer(model, sample_rate)

    texts = []
    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            texts.append(rec.Result())
    
    texts = [json.loads(x) for x in texts]
    texts = " ".join([x["text"] for x in texts if len(x) != 0])
    return texts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Video to text')
    parser.add_argument('modelpath', type=str, help="Vosk file path", default="../../vosk-api/python/example/model")
    parser.add_argument('videopath', type=str, help='Video Path')
    parser.add_argument('output', type=str, help='Output text file')
    args = parser.parse_args()

    sample_rate = 16000
    model = Model(args.modelpath)
    texts = decode_speech(model, args.videopath)
    with open(args.output, "r") as f:
        print(texts, file=args.output)

from vosk import Model, KaldiRecognizer
import os
import json
import pyaudio
model = Model(r"../vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=16000, 
    input=True, 
    frames_per_buffer=8000
)
def WaitRecognize():
    stream.start_stream()
    iterator = 0
    x = ""
    while not len(x):
        for i in range(20):
            data = stream.read(2000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                pass
        x  =  json.loads(rec.FinalResult())["text"]
    stream.stop_stream()
    return x

def FastRecognize():
    stream.start_stream()
    x = ""
    for i in range(10):
        data = stream.read(3000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass
    x  =  json.loads(rec.FinalResult())["text"]
    stream.stop_stream()
    return x
print(FastRecognize())

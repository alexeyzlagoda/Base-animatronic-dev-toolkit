# -*- coding: cp1251 -*-
import threading
from random import randint
import speech_recognition  
import pyttsx3  
import wave  
import json  
import os  
#import random
import time, subprocess
#import openai
from silero import  silero_tts
import torch
import sounddevice as sd
import cv2
#import OS_DATA.Source.mySerial as mySerial
import pyaudio
#import speech_recognition
#GPT
#Checker 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)  
#SNAKES4/silero
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar' # baya aidar kseniya xenia
put_accent = True
put_yo = True
device = torch.device('cpu')
def millis():
    return round(time.time() * 1000)
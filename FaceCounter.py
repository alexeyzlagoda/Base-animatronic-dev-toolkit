# -*- coding: cp1251 -*-
from Config import *
def CountFaces():
    ret, frame = cap.read()
    if not ret:
        return -1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    return len(faces)
def CountByDT(dt):
    last = 0
    while True:
        if millis - last > dt:
            Children_count = CountFaces()
        
def InitAutoCounter():
    t1 = threading.Thread(target=CountByDT, args=(500))
    t1.start()

print(CountFaces())

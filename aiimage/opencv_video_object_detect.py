import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(base_path+'/haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(base_path+'/haarcascade/haarcascade_eye.xml')
lefteye = cv2.CascadeClassifier(base_path+'/haarcascade/haarcascade_lefteye_2splits.xml')

if not (cap.isOpened()):
    print("Could not open vides device")
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        leyes = eye_cascade.detectMultiScale(roi_gray)
        for(lex,ley,lew,leh) in leyes:
            cv2.rectangle(roi_color,(lex,ley),(lex+lew,ley+leh),(0,255,0),2)
    cv2.imshow("frame", frame)
    # out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

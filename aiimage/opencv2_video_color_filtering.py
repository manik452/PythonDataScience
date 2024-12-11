import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
# print("hello" + base_path)
cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
# cap = cv2.VideoCapture(base_path + '\videos\PXL_20230519_113650777.mp4')

if not (cap.isOpened()):
    print("Could not open vides device")
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([50, 0, 0])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    # dark_red = np.uint8([[[12, 22, 121]]])
    # dar = cv2.cvtColor(dard_red, cv2.COLOR_BGR2HSV)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    # out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

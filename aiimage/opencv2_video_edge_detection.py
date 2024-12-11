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

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow("frame", frame)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    cv2.imshow("edges", edges)
    # out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
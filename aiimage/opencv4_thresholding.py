import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(base_path + "\images\low-light.jpg")

retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)


grayscaled= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
retval3,otsu = cv2.threshold(grayscaled,112,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# grayscaled =cv2.cvtColor(img,cv2.Col)
# Show image through cv2
cv2.imshow("original", img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract

base_path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(base_path + "\images\captcha\image.png")
# img = cv2.imread(r'C:/Users/Acer/Documents/python/PythonDataScience/aiimage/images/captcha/itled.jpg')
if img is None: 
    print("Image is empty!!")
else :
    print("Image is not empty!!")
# resize_image = cv2.resize(img, (200, 200))
# cv2.imwrite("panda/" + str(pic_num) + ".jpg", resize_image)
# cv2.imshow("img_bgr", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    # Open the file in append mode
    # file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
    print(text)
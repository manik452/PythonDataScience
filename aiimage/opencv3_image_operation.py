import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
# print("hello" + base_path)
img1 = cv2.imread(base_path + "\images\dmatplotlib.png")
img2 = cv2.imread(base_path + "\images\mainlogo.png")

# img[55, 55] = [255, 255, 255]
# px = img[55, 55]
# watch_face = img[37:111, 107:194]
# img[100:150, 100:150] = [255, 255, 255]
# img[0:74, 0:87] = watch_face

rows1, cols1, channels = img2.shape
roi = img1[0:rows1, 0:cols1]


img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst

# Show image through cv2
cv2.imshow("res", img1)
# cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show image through matpilib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

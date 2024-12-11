import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
img_bgr = cv2.imread(base_path + "\images\corner_detection_images.png")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
# print(img_gray)
corners = cv2.goodFeaturesToTrack(img_gray, 10000, 0.0001, 20)
corners = np.int8(corners)
print(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img_bgr, (x, y), 3, 255, -1)

cv2.imshow("img_bgr", img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
img1 = cv2.imread(base_path + "\images\match_image.jpg.png", 1)
img2 = cv2.imread(base_path + "\images\match_image.jpg.png", 1)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

matches = bf.match(des2, des1)
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10],None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Show image through cv2
cv2.imshow("img3", img3)
# cv2.imshow("img_gray", img_gray)
# cv2.imshow("template", template)
# cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

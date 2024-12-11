import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
img_bgr = cv2.imread(base_path + "\images\hearts_image.png")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread(base_path + "\images\hearts_match_template.png", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.40

loc = np.where(res >= threshold)
# print(loc.count)
# cv2.rectangle(img_bgr, (5, 5), (220, 220), (255, 0, 0), 2)
for pt in zip(*loc[::-1]):
    # print(pt)
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)


# Show image through cv2
cv2.imshow("img_bgr", img_bgr)
# cv2.imshow("img_gray", img_gray)
# cv2.imshow("template", template)
# cv2.imshow("image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

# Show image through matpilib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

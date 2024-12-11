import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(os.path.abspath(__file__))
# print("hello" + base_path)
img = cv2.imread(base_path + "\images\BRISTY.jpg", cv2.IMREAD_GRAYSCALE)

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.rectangle(img, (15, 25), (200, 150), (255, 255, 255), 15)
cv2.circle(img, (100, 63), 65, (55, 25, 215), 15)

pts = np.array([[10, 15], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (219, 0, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "I love you", (0, 130), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Show image through cv2
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Show image through matpilib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

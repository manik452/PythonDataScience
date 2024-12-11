import sys

import cv2
import numpy as np
import pytesseract
from pytesseract import Output

if (len(sys.argv)) != 2:
    sys.exit("Useage: python filter.fy and image")

# inputImage = Image.open(sys.argv[1])
inputImage = cv2.imread(
    r"C:\Users\Acer\Documents\python\PythonDataScience\aiimage\image.png"
)

# image = Image.open(r'C:\Users\Acer\Pictures\Screenshots\image.png')
print(inputImage)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR\tesseract"
)


# custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321 --psm 6'
# text = pytesseract.image_to_string(inputImage, output_type=Output.DICT, config=custom_config)
# print(text)
#
# d = pytesseract.image_to_data(inputImage, output_type=Output.DICT)
# print(d)


# image = image.convert("RGBA")
# filtered = image.filter(ImageFilter.Kernel(size=(3, 3), kernel=[-1, -1, -1, -1, 9, -1, -1, -1, -1], scale=1))

# d1 = ImageDraw.Draw(image)
# d1.text((28, 36), "Hello, TutorialsPoint!", fill=(255, 0, 0))
# image.show()
# filtered = image.filter(ImageFilter.MaxFilter(size=3))

# out.show()
# filtered.show()


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


gray = get_grayscale(inputImage)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
# cv2.imshow(gray, mat=cv2.UMat)

print(pytesseract.image_to_string(inputImage, output_type=Output.DICT))
outputImage = inputImage
h, w, c = outputImage.shape
boxes = pytesseract.image_to_boxes(outputImage)

for b in boxes.splitlines():
    b = b.split(" ")
    outputImage = cv2.rectangle(
        outputImage,
        (int(b[1]), h - int(b[2])),
        (int(b[3]), h - int(b[4])),
        (0, 255, 0),
        2,
    )


# cv2.imshow('img', outputImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(pytesseract.image_to_string(inputImage, output_type=Output.DICT))

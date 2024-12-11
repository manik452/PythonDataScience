import urllib.request
import cv2
import numpy as np
import os


base_path = os.path.dirname(os.path.abspath(__file__))


def store_raw_images():
    # net_images_link = "https://image-net.org/api/imagenet.synset.geturls?wnid=n00523513" 1
    net_images_link = "https://image-net.org/api/imagenet.synset.geturls?wnid=n07942152"
    # net_images_link = "https://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152" 3
    neg_image_urls = urllib.request.urlopen(net_images_link).read().decode()

    if not os.path.exists(base_path+"/neg"):
        os.makedirs(base_path+"/neg")

    pic_num = 6

    for i in neg_image_urls.split("\n"):
        try:
            print('url\n'+i)
            urllib.request.urlretrieve(i,"neg/" + str(pic_num) + ".jpg")
            print('this is ivalue')
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            resize_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resize_image)
            pic_num += 1
        except Exception as e:
            print('failed')
            print(str(e))

           


store_raw_images()

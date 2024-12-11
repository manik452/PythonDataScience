import glob
import CaptchaCracker as cc
import os

base_path = os.path.dirname(os.path.abspath(__file__))
# Training image data path
train_img_path_list = glob.glob(base_path + "/images/train_numbers_only/*.png")
# for name in train_img_path_list:
#     print(name)
# Training image data size
img_width = 200
img_height = 50
# print("Image Path")
# print(train_img_path_list)
# Creating an instance that creates a model
CM = cc.CreateModel(train_img_path_list, img_width, img_height)

# Performing model training
model = CM.train_model(epochs=100)

# Saving the weights learned by the model to a file
model.save_weights(base_path + "/images/weights.h5")

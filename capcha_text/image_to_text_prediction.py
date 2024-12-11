import CaptchaCracker as cc
import os

# Target image data size
img_width = 200
img_height = 50
# Target image label length
max_length = 6
# Target image label component
characters = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
base_path = os.path.dirname(os.path.abspath(__file__))
# Model weight file path
weights_path = base_path + "/images/weights.h5"
# Creating a model application instance
AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)

# Target image path
target_img_path = base_path + "/images/test_numbers_only/028026.png"

# Predicted value
pred = AM.predict(target_img_path)
print(pred)

# RGB to YCbCr

import cv2 as cv
from google.colab.patches import cv2_imshow as imshow

img_path = '/content/Lenna.png'
img = cv.imread(img_path)

# ycbcr = cv.cvtColor(cv.cvtColor(img, cv.COLOR_BGR2RGB), cv.COLOR_RGB2YCR_CB)

imshow(cv.cvtColor(cv.cvtColor(img, cv.COLOR_BGR2RGB), cv.COLOR_RGB2YCR_CB))

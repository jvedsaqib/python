import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt
import numpy as np


img_path = '/content/Lenna.png'
bgr_img = cv.imread(img_path, 0)
img = bgr_img.copy()

imshow(img)

for i in range(len(bgr_img)):
  for j in range(len(bgr_img[0])):
    temp = (bgr_img[i][j] * 0.8) + 50   # make changes here
    if temp > 255:
      bgr_img[i][j] = 255
    else:
      bgr_img[i][j] = temp

imshow(bgr_img)

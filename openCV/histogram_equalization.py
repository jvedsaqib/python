import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt
import numpy as np


img_path = '/content/Lenna.png'
bgr_img = cv.imread(img_path, 0)

equ_img = cv.equalizeHist(bgr_img, 0)

plt.subplot(2,2,1)
plt.imshow(bgr_img)
plt.title("Original Image")

hist_org = cv.calcHist([bgr_img], [0], None, [256], [0, 256])

plt.subplot(2,2,2)
plt.plot(hist_org)
plt.title("Original Image Histogram")

plt.subplot(2,2,3)
plt.imshow(equ_img)
plt.title("Equalized Image")

hist_equ = cv.calcHist([equ_img], [0], None, [256], [0, 256])

plt.subplot(2,2,4)
plt.plot(hist_equ)
plt.title("Equalized Image Histogram")

plt.show()

import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt
import numpy as np


def pixelVal(pix, r1, s1, r2, s2):
  if 0 <= pix and pix <= r1:
    return (s1 / r1) * pix
  elif r1 < pix and pix <= r2:
    return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
  else:
    return ((255 - s2)/(255 - r2)) * (pix - r2) + s2


img_path = '/content/Lenna.png'
img = cv.imread(img_path)

bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

r1 = 90
s1 = 0
r2 = 120
s2 = 255

pixelVal_vec = np.vectorize(pixelVal)

new_img = pixelVal_vec(bgr_img, r1, s1, r2, s2)

plt.subplot(2,1,1)
plt.imshow(bgr_img)
plt.title("Original Image")

plt.subplot(2,1,2)
plt.imshow(new_img)
plt.title("Contrast Stretched Image")

plt.show()

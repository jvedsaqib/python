import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt
import numpy as np


img_path = '/content/Lenna.png'
img = cv.imread(img_path)

bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

loc = 1
plt.subplot(2, 3, loc)
plt.imshow(bgr_img)
plt.title("Original")
for gamma in [0.1, 0.5, 1.2, 2.2]:
  loc += 1
  gamma_corrected = np.array(255*(bgr_img / 255) ** gamma, dtype= 'uint8')
  plt.subplot(2, 3, loc)
  plt.title(gamma)
  plt.imshow(gamma_corrected)

plt.show()

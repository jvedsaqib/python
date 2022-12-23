import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt
import numpy as np


img_path = '/content/Lenna.png'
img = cv.imread(img_path)

bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

# bgr image

plt.subplot(1,2,1)
plt.imshow(bgr_img)
plt.title("BGR Image")

# bgr histogram

color = ('b', 'g', 'r')

plt.subplot(1,2,2)
plt.title("B,G,R Histogram")
for i,col in enumerate(color):
  histr = cv.calcHist([bgr_img], [i], None, [256], [0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0,256])

plt.show()

# log transformation

c = 255 / np.log(1 + np.max(bgr_img))
log_image = c * (np.log(bgr_img + 1))

log_image = np.array(log_image, dtype = np.uint8)

plt.subplot(1,2,1)
plt.imshow(log_image)
plt.title("Log Image")

# bgr histogram

color = ('b', 'g', 'r')

plt.subplot(1,2,2)
plt.title("B,G,R Histogram")
for i,col in enumerate(color):
  histr = cv.calcHist([log_image], [i], None, [256], [0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0,256])

plt.show()

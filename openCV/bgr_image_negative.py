import cv2 as cv
from google.colab.patches import cv2_imshow as imshow
import matplotlib.pyplot as plt

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

h, w, _ = bgr_img.shape

for i in range(h-1):
  for j in range(w-1):
    pixel = bgr_img[i][j]

    pixel[0] = 255 - pixel[0]
    pixel[1] = 255 - pixel[1]
    pixel[2] = 255 - pixel[2]

    bgr_img[i][j] = pixel

plt.subplot(1,2,1)
plt.imshow(bgr_img)
plt.title("BGR Image Negative")

plt.subplot(1,2,2)
plt.title("B,G,R Histogram Negative")
for i,col in enumerate(color):
  histr = cv.calcHist([bgr_img], [i], None, [256], [0, 256])
  plt.plot(histr, color = col)
  plt.xlim([0,256])

plt.show()

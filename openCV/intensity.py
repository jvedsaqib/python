import cv2 as cv
from matplotlib import pyplot as plp
import numpy as np

img = cv.imread('images/3bit.png', 0)
cv.imshow("image", img)
print(img.shape)

intensity_count = [0]*256

height, width = img.shape[:2]
print(height)
print(width)

new_image = np.zeros(img.shape)

for i in range(0, height):
    for j in range(0, width):
        intensity_count[img[i][j]]+=1

print(intensity_count)



cv.waitKey(0)

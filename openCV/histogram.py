# Histogram of an image
import cv2 as cv
from matplotlib import pyplot as plp

img = cv.imread('images/Lenna.png', 0)
cv.imshow("image", img)

histr = cv.calcHist([img], [0], None, [256], [0, 255]) 
plp.plot(histr)
plp.show()

print(img.shape)

cv.waitKey(0)

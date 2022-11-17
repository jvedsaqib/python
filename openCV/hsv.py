import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow("image", img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

cv.waitKey(0)

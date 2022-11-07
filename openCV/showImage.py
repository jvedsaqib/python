import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow('image', img)

cv.waitKey(0)

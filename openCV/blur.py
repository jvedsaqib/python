import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow('image', img)

blurred = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blurred)

cv.waitKey(0)

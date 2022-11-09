import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow('image', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)

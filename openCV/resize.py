import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow('image', img)

resized_img = cv.resize(img, (250, 250))
cv.imshow('resized image', resized_img)

cv.waitKey(0)

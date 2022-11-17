import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow("image", img)

cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)

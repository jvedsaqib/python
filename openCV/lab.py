import cv2 as cv

img = cv.imread('images/Lenna.png', 0)
cv.imshow("image", img)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0)

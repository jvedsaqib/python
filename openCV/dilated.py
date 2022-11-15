import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow("image", img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

dilated_img = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated', dilated_img)

dilated_img2 = cv.dilate(img, (3,3), iterations=3)
cv.imshow('dilated2', dilated_img2)

cv.waitKey(0)

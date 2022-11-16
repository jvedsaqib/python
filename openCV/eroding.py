import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow("image", img)

dilated_img2 = cv.dilate(img, (3,3), iterations=3)
cv.imshow('dilated2', dilated_img2)

eroded = cv.erode(img, kernel=(3,3), iterations=3)
cv.imshow('eroded', eroded)

cv.waitKey(0)

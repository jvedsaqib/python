import cv2 as cv

img = cv.imread('images/Lenna.png')
cv.imshow("image", img)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)

# program to add two images
import cv2 as cv

img1 = cv.imread("images/Lenna.png", 0)
img2 = cv.imread("images/LennaNew.png", 0)
cv.imshow("Image1", img1)


for i in range(len(img1)):
    for j in range(len(img1[0])):
        img1[i][j] = (img1[i][j] + img2[i][j])

cv.imshow("Image3", img1)
cv.imshow("Image2", img2)


cv.waitKey(0)

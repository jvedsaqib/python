import cv2 as cv
from google.colab.patches import cv2_imshow as imshow

img_path = '/content/Lenna.png'
img = cv.imread(img_path)

imshow(img)

a = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
imshow(a)

b = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
imshow(b)

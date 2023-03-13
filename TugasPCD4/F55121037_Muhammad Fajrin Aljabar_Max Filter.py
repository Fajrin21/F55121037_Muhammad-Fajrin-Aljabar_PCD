import cv2
import numpy as np

img = cv2.imread('gambar1.JPG')

ksize = 5

kernel = np.ones((ksize, ksize), np.uint8)
max_filtered = cv2.dilate(img, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Max Filtered Image', max_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('gambar1.jpg')

ksize = 5

kernel = np.ones((ksize, ksize), np.uint8)
min_filtered = cv2.erode(img, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Min Filtered Image', min_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
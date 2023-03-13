import cv2

img = cv2.imread('gambar1.jpg')

ksize = 5

median = cv2.medianBlur(img, ksize)

cv2.imshow('Original Image', img)
cv2.imshow('Median Filtered Image', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
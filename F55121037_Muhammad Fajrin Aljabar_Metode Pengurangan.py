import cv2

img1 = cv2.imread('gambar1.jpg')
img2 = cv2.imread('gambar2.jpg')
img2 = cv2.resize(img2, (327, 536))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.subtract(gray1, gray2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()

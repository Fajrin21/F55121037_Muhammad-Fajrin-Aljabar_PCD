import cv2

img = cv2.imread('xray.jpg', 0)

diff_img = cv2.absdiff(cv2.GaussianBlur(img, (5, 5), 0), img)
equalized_diff_img = cv2.equalizeHist(diff_img)
equalized_img = cv2.equalizeHist(img)

cv2.imshow('Original Image', img)
cv2.imshow('Difference Image', diff_img)
cv2.imshow('Equalized Difference Image', equalized_diff_img)
cv2.imshow('Equalized Image', equalized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
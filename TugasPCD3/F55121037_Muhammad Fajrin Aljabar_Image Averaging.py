import cv2

img1 = cv2.imread('gambar1.jpg')
img2 = cv2.imread('gambar2.jpg')
img2 = cv2.resize(img2, (327, 536))

avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 1)

cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

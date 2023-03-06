import cv2

from matplotlib import pyplot as plt

img = cv2.imread('gambar1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.plot(hist)

plt.show()

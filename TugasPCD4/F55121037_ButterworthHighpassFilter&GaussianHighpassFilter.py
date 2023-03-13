import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar1.jpg',0)
rows, cols = img.shape

butterworth_hp = np.zeros((rows, cols))
D = 30
n = 2
for i in range(rows):
    for j in range(cols):
        butterworth_hp[i, j] = 1 / (1 + (D / np.sqrt((i - rows/2)**2 + (j - cols/2)**2))**(2*n))

butterworth_hp_img = np.fft.fftshift(np.fft.fft2(img)) * butterworth_hp
butterworth_hp_img = np.real(np.fft.ifft2(np.fft.ifftshift(butterworth_hp_img)))

gaussian_hp = np.zeros((rows, cols))
sigma = 5
for i in range(rows):
    for j in range(cols):
        gaussian_hp[i, j] = 1 - np.exp(-((i - rows/2)**2 + (j - cols/2)**2) / (2 * sigma**2))

gaussian_hp_img = np.fft.fftshift(np.fft.fft2(img)) * gaussian_hp
gaussian_hp_img = np.real(np.fft.ifft2(np.fft.ifftshift(gaussian_hp_img)))

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(butterworth_hp_img, cmap = 'gray')
plt.title('Butterworth Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(gaussian_hp_img, cmap = 'gray')
plt.title('Gaussian Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()


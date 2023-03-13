import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar1.jpg',0)
rows, cols = img.shape

blur = cv2.GaussianBlur(img, (5,5), 0)
unsharp_mask = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
laplacian_filter = np.zeros((rows, cols), np.float32)
laplacian_filter[int(rows/2)-1:int(rows/2)+2, int(cols/2)-1:int(cols/2)+2] = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
laplacian_freq = fshift * laplacian_filter
laplacian_img = np.real(np.fft.ifft2(np.fft.ifftshift(laplacian_freq)))

gaussian_filter = np.zeros((rows, cols), np.float32)
for i in range(rows):
    for j in range(cols):
        gaussian_filter[i, j] = np.exp(-((i - rows/2)**2 + (j - cols/2)**2) / (2 * 50**2))
selective_filtered_img = gaussian_filter * img + (1 - gaussian_filter) * unsharp_mask
selective_filtered_mask = gaussian_filter * unsharp_mask + (1 - gaussian_filter) * img

plt.subplot(2,3,1),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(unsharp_mask, cmap = 'gray')
plt.title('Unsharp Masking Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(laplacian_img, cmap = 'gray')
plt.title('Laplacian Domain Frequency Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(selective_filtered_img, cmap = 'gray')
plt.title('Selective Filtering (Original Image)'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(selective_filtered_mask, cmap = 'gray')
plt.title('Selective Filtering (Unsharp Mask)'), plt.xticks([]), plt.yticks([])
plt.show()

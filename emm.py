import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt


image1 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/speed-plus/0.jpeg')
image2 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/speed-plus/1.jpeg')
pixel_diff = cv2.absdiff(image1, image2)

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ssim_score = 1 - (ssim(gray1, gray2))

print(ssim_score)
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('P1')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('P2')

plt.subplot(1, 3, 3)
plt.imshow(pixel_diff, cmap='gray')
plt.title(f'SSIM: {ssim_score:.2f}')

plt.show()
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt


image1 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/speed-plus/0.jpeg')
image2 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/speed-plus/5.jpeg')
image0 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/black.jpeg')
pixel_diff = cv2.absdiff(image1, image2)

gray0 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_ = cv2.cvtColor(pixel_diff, cv2.COLOR_BGR2GRAY)
ssim_score = 1 - (ssim(gray1, gray2))
print(gray0.shape)
print(gray_.shape)
print(gray1.shape)
print(gray2.shape)
differ = 1 - (ssim(gray_, gray0))
final = 1 - (ssim_score/differ)

pixel_diff_ = cv2.absdiff(gray_, gray0)

print(ssim_score)
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('P1')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('P2')

plt.subplot(1, 4, 3)
plt.imshow(pixel_diff, cmap='gray')
plt.title(f'SSIM: {ssim_score:.2f}')

plt.subplot(1, 4, 4)
plt.imshow(gray_)
plt.title(f'Final: {final:.2f}')

plt.show()

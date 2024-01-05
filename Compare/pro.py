import Compare
import cv2
from skimage.metrics import structural_similarity as ssim


def compair(image1, image2, black):  # 黑的是一样的,白的是不一样的
    return ssim(cv2.cvtColor(cv2.absdiff(image1, image2), cv2.COLOR_BGR2GRAY), cv2.cvtColor(black, cv2.COLOR_BGR2GRAY))

import numpy as np
import cv2


def main():
    img1 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/正式数据/2023.12.20/0/13.10/Capture_1.bmp')
    img2 = cv2.imread('/Volumes/home/Experiment/定量/细胞环流/数据/正式数据/2023.12.20/0/13.10/Capture_5.bmp')

    diffImg1 = cv2.subtract(img1, img2)
    diffImg2 = cv2.subtract(img2, img1)

    cv2.imshow('subtract(img1,img2)', diffImg1)
    cv2.imshow('subtract(img2,img1)', diffImg2)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()

import cv2
import os
import glob
from skimage.metrics import structural_similarity as ssim
import re


image_basic =cv2.imread('/Volumes/home/Experiment/定量/细胞环流/程序/image/black-1296*972.jpg')


def sort(filelist: list):
    if len(filelist) < 2:
        return filelist
    else:
        pivot = filelist[0]
        less = [i for i in filelist[1:] if i[0] <= pivot[0]]
        greater = [i for i in filelist[1:] if i[0] > pivot[0]]
        return sort(less) + [pivot] + sort(greater)


def rank(filelist: list):
    return sort([[re.findall('\d+', file)[0], file] for file in filelist])


def path():
    pass


def compare(image1, image2):
    return (1 - (
            (1 - (ssim(cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY),  # 两张图片的相对差
                       cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)))) /
            (1 - (ssim(cv2.cvtColor(cv2.absdiff(image1, image2), cv2.COLOR_BGR2GRAY),  # 两张图片的差与纯黑图片的差(相对差)
                       cv2.cvtColor(image_basic, cv2.COLOR_BGR2GRAY))))))


def file(folder, point):
    return rank(glob.glob(os.path.join(folder + '/' + point, '*.bmp')))


def main(folder: str, point=None):
    output = {}
    gentle = 0
    if point is None:
        point = ['a', 'b', 'c', 'd', 'e']
    for i in point:
        last = None
        file_list = file(folder, i)
        for t in file_list:
            if last is not None:
                now = cv2.imread(t[1])
                gentle += compare(last, now)
            last = cv2.imread(t[1])
        output[i] = gentle / (len(file_list) - 1)
        gentle = 0
    return output

import cv2
import os
import glob
from skimage.metrics import structural_similarity as ssim
import re


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


def compare(folder: str, point=None):
    output = {}
    gentle = 0
    if point is None:
        point = ['a', 'b', 'c', 'd', 'e']
    for i in point:
        last = None
        file_list = rank(glob.glob(os.path.join(folder + '/' + i, '*')))
        for t in file_list:
            if last is not None:
                now = cv2.imread(t[1])
                cv2.absdiff(now, last)
                gentle += (1 - (ssim(cv2.cvtColor(now, cv2.COLOR_BGR2GRAY), cv2.cvtColor(last, cv2.COLOR_BGR2GRAY))))
            last = cv2.imread(t[1])
        output[i] = gentle/(len(file_list)-1)
        gentle = 0
    return output

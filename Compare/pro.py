import os
import re

import Compare
import Compare.sql
import cv2
import pymysql
from skimage.metrics import structural_similarity as ssim


def sort(filelist: list):
    if len(filelist) < 2:
        return filelist
    else:
        pivot = filelist[0]  # len(filelist)/2
        less = [i for i in filelist[1:] if int(re.findall('\d+', i)[0]) <= int(re.findall('\d+', pivot)[0])]
        greater = [i for i in filelist[1:] if int(re.findall('\d+', i)[0]) > int(re.findall('\d+', pivot)[0])]
        return sort(less) + [pivot] + sort(greater)


def compare(image1, image2, black=Compare.image_basic):  # 黑的是一样的,白的是不一样的
    return (1 -
            ssim(cv2.cvtColor(cv2.absdiff(image1, image2), cv2.COLOR_BGR2GRAY),
                 cv2.cvtColor(black, cv2.COLOR_BGR2GRAY))
            )


def point(folder):
    return [i for i in os.listdir(folder) if os.path.isdir(os.path.join(folder, i))]


def grope_compare(images):
    last = None
    gentle = 0
    for i in sort(images):
        if last is not None:
            now = cv2.imread(i)
            gentle += compare(last, now)
        last = cv2.imread(i)
    return gentle / (len(images) - 1)


def ergodic(folder, pattern, tables='CellCirculation'):
    for root, dirs, files in os.walk(folder):
        file_list = []
        for file in files:
            if re.match(pattern, file):
                file_list.append(os.path.join(root, file))
        if file_list:
            try:
                with Compare.sql.SQL() as database:
                    database.tables(tables)
                    database + [grope_compare(file_list), os.path.basename(root), os.path.basename(os.path.dirname(root))]
            except pymysql.err.DataError:
                pass


def main(folder, point_=None):
    if point_ is None:
        point_ = point(folder)
    print(point_)
    output = {}
    gentle = 0
    for i in point_:
        last = None
        file_list = Compare.file(folder, i)
        for t in file_list:
            if last is not None:
                now = cv2.imread(t[1])
                gentle += compare(last, now)
            last = cv2.imread(t[1])
        output[i] = gentle / (len(file_list) - 1)
        gentle = 0
    return output

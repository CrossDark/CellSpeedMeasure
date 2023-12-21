import glob
import os.path

import Compare


if __name__ == '__main__':
    print(Compare.compare(folder='/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/', point=['speed-plus']))
    # print(Compare.rank(glob.glob(os.path.join('/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/speed-basic', '*'))))

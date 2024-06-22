from itertools import cycle
from moviepy.editor import ImageSequenceClip
from ultralytics import YOLO
from Tools.sql import SQL
import av
import os
import time
import glob
import math
import copy


class Video:
    def __init__(self, path: str, cache: str):
        self.value = 0
        self.lost = 0
        self.stream: list[list[list[float, float, float, float]]] = []
        self.image_paths = []
        self.path = path
        self.cache = cache
        self.video = av.open(path)

    def split_flame(self, sampling_rate: int = 1):  # 将视频拆分成帧(可设置间隔)
        flames = self.video.decode(self.video.streams.video[0])
        # 逐帧遍历视频
        for index, frame in enumerate(flames):
            if index % sampling_rate == 0:
                image = frame.to_image()
                image_path = os.path.join(self.cache, f'frame-{index:04d}.jpg')
                self.image_paths.append(image_path)
                image.save(image_path)

    def generate_video(self, fps: int = 25):
        # 通过图片生成视频
        clip = ImageSequenceClip(self.image_paths, fps=fps)
        # 写入视频文件
        clip.write_videofile(os.path.join(self.cache, 'processed.mp4'), codec='libx264')  # 写入视频文件，指定编码器为libx264

    def yolo(self, model: str):
        lost = 0
        output_ = []
        for i in YOLO(model).track(source=os.path.join(self.cache, 'processed.mp4'), save=True, conf=0.05, iou=0.1):
            print(i.boxes.id.tolist())
            print(i.boxes.xyxy.tolist())
            print('-------------------------')
            i_xy = []
            for j in i:
                j_xy = []
                for k in i.boxes.xyxy:
                    j_xy.append([float(item) for item in list(k)])
                i_xy.append(j_xy)
            try:  # 这么干会让结果不准确,把两帧当成一帧,导致间隔扩大了两倍,有空修复
                output_.append(i_xy[0])
            except IndexError:
                lost += 1
        self.stream = output_
        self.lost = lost

    def output(self, path: str):
        with open(path, 'w', encoding='utf-8') as file:
            for flame in self.stream:
                for block in flame:
                    file.write(str(block[0]) + ' ' + str(block[1]) + ' ' + str(block[2]) + ' ' + str(block[3]) + '  ')
                file.write('\n')

    def clean(self):
        # 使用glob模块列出目录下的所有文件
        for filename in glob.glob(os.path.join(self.cache, '*')):
            try:
                # 检查是否为文件（而不是目录）
                if os.path.isfile(filename) or os.path.islink(filename):
                    os.unlink(filename)  # 删除文件
            except Exception as e:
                print(f'Error deleting {filename}: {e}')

    @staticmethod
    def analise(datas, max_distance: int = 10):
        sub = 0
        last = []
        for i in datas:  # 逐帧遍历视频(数据)
            if (last is None) or (i is None):  # 如果两帧全没识别到
                continue
            distance = []  # distance中取最小值,可以认为是一个叶绿体在两帧之间的移动距离
            for post1 in last:  # 遍历前一帧的所有叶绿体
                distances = []  # 帧1的一个叶绿体于帧2中所有叶绿体的距离,其中最小的可以认为是叶绿体在两帧中运动的距离
                for post2 in i:  # 遍历后一帧的所有叶绿体
                    distances.append(math.sqrt((post1[0] - post2[0]) ** 2 + (post1[1] - post2[1]) ** 2))  # 计算两个叶绿体间的距离
                if min(distances) <= max_distance:  # 说明没跟丢
                    distance.append(min(distances))
            try:
                sub += sum(distance) / len(distance)
            except ZeroDivisionError:
                sub += 0
            last = i
        return sub / len(datas)

    def database(self, spread: int):
        xy = self.stream
        part = len(self.stream) / spread
        part1 = cycle([math.floor(part), math.ceil(part)])
        part2 = copy.deepcopy(part1)
        for index, k in enumerate([xy[i:i + next(part2)] for i in range(0, len(xy), next(part1))]):
            with SQL() as db:
                db.tables('LightTemperature')
                db.keys = 'value,temperature,light,part,wrong'
                info = os.path.splitext(os.path.basename(self.path))[0].split('-')
                db + ([str(self.analise(k))] + list(info[:2] if len(info) == 2 else info[:1] + [0]) + [index + 1, self.lost])


def main():
    video = Video('/Volumes/home/Experiment/细胞环流/数据/实验数据/光照强度/NO-6/2000lux-5.mp4', 'cache/')
    video.split_flame(10)
    video.generate_video()
    video.yolo('/Volumes/home/Project/YoloV8/model/不错.pt')
    video.output('/Users/crossdark/Downloads/result.txt')
    video.database(20)
    video.clean()


if __name__ == '__main__':
    # 开始计时
    start_time = time.perf_counter_ns()
    # 主函数
    main()
    # 停止计时
    end_time = time.perf_counter_ns()
    # 输出用时
    print("运行时间: {:.9f} 秒".format((end_time - start_time) / 1e9))

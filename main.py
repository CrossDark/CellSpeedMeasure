from CDBio import Video
import time


def main(path):
    video = Video(path, 'cache/')
    """video.split_flame(1)
    video.generate_video()
    video.yolo('/Volumes/home/Project/YoloV8/model/不错.pt')
    video.output('/Users/crossdark/Downloads/result.txt')"""
    video.load('/Users/crossdark/Downloads/result.txt')
    video.database(10, 10, 'LightIntensity')
    video.clean()


if __name__ == '__main__':
    # 开始计时
    start_time = time.perf_counter_ns()
    # 主函数
    main('/Volumes/home/Experiment/细胞环流/数据/实验数据/光照强度/NO-6/2000lux-6.mp4')
    # 停止计时
    end_time = time.perf_counter_ns()
    # 输出用时
    print("运行时间: {:.9f} 秒".format((end_time - start_time) / 1e9))

import cv2

# 读取两张图片
image1 = cv2.imread('/Volumes/home/Experiment/细胞环流/数据/校准数据/speed-plus/0.jpeg')
image2 = cv2.imread('/Volumes/home/Experiment/细胞环流/数据/校准数据/speed-plus/1.jpeg')

# 将两张图片转换为同样的大小（如果需要）
resized_image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# 对两张图片进行相减操作
subtracted_image = cv2.absdiff(resized_image1, image2)  # 黑的是一样的,白的是不一样的

# 显示结果图片
cv2.imshow("Subtracted Image", subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

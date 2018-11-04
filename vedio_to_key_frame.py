from PIL import Image
import cv2
import os.path
# print('ok')

path = 'D:/project/vedio to picture/image'

def splitFrame(videoFileName):
	# 打开视频文件
	video = cv2.VideoCapture(videoFileName)
	num = 1
	while True:
		# 是否成功，当前帧数据
		success,data = video.read()
		if not success:
			break
		# 重建图像
		im = Image.fromarray(data)
		# win上使用path路径时采用反斜杠
		im.save(os.path.join(path,os.path.basename(str(num)+'.jpg')))
		num += 1
	video.release()

splitFrame('clip1.avi')
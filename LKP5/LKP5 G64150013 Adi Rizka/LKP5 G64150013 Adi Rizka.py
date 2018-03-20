import cv2
import numpy as np

def rgb2hsv(source):
	row, col, ignore = source.shape
	dest = np.zeros((row, col, 3), np.uint8)
	for i in range(row):
		for j in range(col):
			r_ = source[i][j][2] / 255
			g_ = source[i][j][1] / 255
			b_ = source[i][j][0] / 255
			Cmax = max(r_, g_, b_)
			Cmin = min(r_, g_, b_)
			delta = Cmax - Cmin
			h = 0
			if delta == 0:
				h = 0
			elif Cmax == r_:
				h = 60 * (((g_ - b_) / delta) % 6) 
			elif Cmax == g_:
				h = 60 * (((b_ - r_) / delta) + 2)
			elif Cmax == b_:
				h = 60 * (((r_ - g_) / delta) + 4)
			s = 0 if delta == 0 else delta / Cmax
			v = Cmax
			
			h /= 2
			v = v * 255
			s = s * 255
			dest.itemset((i, j, 0), v)
			dest.itemset((i, j, 1), s)
			dest.itemset((i, j, 2), h)
	return dest

def detectFace(source):
	row, col, ignore = source.shape
	dest = np.zeros((row, col, 3), np.uint8)
	for i in range(row):
		for j in range(col):
			v_ = source[i][j][0]
			s_ = source[i][j][1]
			h_ = source[i][j][2]

			if h_ <= 20 and s_ >= 5:
				dest.itemset((i, j, 0), v_)
				dest.itemset((i, j, 1), s_)
				dest.itemset((i, j, 2), h_)

	return dest

def hsv2rgb(source):
	row, col, ignore = source.shape
	dest = np.zeros((row, col, 3), np.uint8)
	for i in range(row):
		for j in range(col):
			v_ = source[i][j][0]/255
			s_ = source[i][j][1]/255
			h_ = source[i][j][2]*2

			c = (v_) * (s_)
			x = c * (1 - abs((h_ / 60) % 2 - 1))
			m = v_ - c

			r_, g_, b_ = 0, 0, 0
			if h_ < 60:
				r_, g_, b_ = c, x, 0
			elif h_ < 120:
				r_, g_, b_ = x, c, 0
			elif h_ < 180:
				r_, g_, b_ = 0, c, x
			elif h_ < 240:
				r_, g_, b_ = 0, x, c
			elif h_ < 300:
				r_, g_, b_ = x, 0, c
			elif h_ < 360:
				r_, g_, b_ = c, 0, x

			r, g, b = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
			dest.itemset((i, j, 0), b)
			dest.itemset((i, j, 1), g)
			dest.itemset((i, j, 2), r)

	return dest

source = cv2.imread('FACE DETECTION.png')
print(type(source))
source_hsv = rgb2hsv(source)

result = detectFace(source_hsv)
result = hsv2rgb(result)

cv2.imshow('hasildeteksi.png', result)
cv2.waitKey()
cv2.destroyAllWindows()
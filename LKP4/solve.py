import cv2
import math
import numpy as np

def contrast_stretching(image):
	row, col = image.shape
	dst = np.zeros((row, col, 1), np.uint8)

	maxi = ~(1 << 31)
	mini = 1 << 31
	for i in range(row):
		for j in range(col):
			maxi = max(maxi, image[i][j])
			mini = min(mini, image[i][j])

	for i in range(row):
		for j in range(col):
			dst.itemset((i, j, 0), ((image[i][j] - mini) / (maxi - mini)) * 255)

	return dst

def drawHistogram(image):
	row, col, dummy = image.shape
	data = np.zeros(row * col)

	maxi = ~(1 << 31)
	for i in range(row):
		for j in range(col):
			data[image[i][j][0]] += 1; maxi = max(maxi, data[image[i][j][0]])
			
	histogram = np.zeros((row, col, 1), np.uint8)

	for j in range(col):
		histvalue = col - math.ceil(data[j] * (col - 1) / maxi)
		for i in range(row-1, histvalue-1, -1):
			histogram.itemset((i, j, 0), 255)

	return histogram

def equalization(image):
	row, col = image.shape
	dst = np.zeros((row,col,1), np.uint8)

	pixel=np.zeros(256)
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(image[i,j])
			pixel[nilai]+=1
			
	for i in range(0, 256):
		pixel[i] = float(pixel[i]/(row*col))
	
	for i in range(1, 256):
			pixel[i] = pixel[i]+pixel[i-1]
		
	for i in range(0,256):
		pixel[i]=pixel[i]*(256-1)
		
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(image[i,j])
			nilai = pixel[nilai]
			dst.itemset((i,j,0),nilai)

	return dst

image_grayscale = cv2.imread('car.png', 0)
destination = contrast_stretching(image_grayscale)

image = cv2.imread('car.png')
histogram = drawHistogram(image)

equalized = equalization(image_grayscale)


cv2.imwrite('Contrast_stretching.png', destination)
cv2.imwrite('Histogram.png', histogram)
cv2.imwrite('Equalized.png', equalized)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.destroyAllWindows()
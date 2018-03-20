import cv2
import numpy as np

def BlurMedian(image, size):
	dst = np.zeros((row, col, 1), np.uint8)
	matrix = size
	batas = matrix // 2
	for i in range(row):
		for j in range(col):
			if i >= batas and i <= 255-batas and j >= batas and j <= 255-batas:
				vect = []
				for k in range(i-batas, i+batas+1):
					for l in range(j-batas, j+batas+1):
						vect.append(image[k][l])
				vect.sort()
				mid = matrix*matrix // 2
				dst.itemset((i, j, 0), vect[mid])

	return dst

image = cv2.imread("LennaInput.jpg", 0)
output = cv2.imread("LennaOutput.jpg", 0)
row, col = image.shape

destination = BlurMedian(image, 3)
destination = BlurMedian(destination, 3)

cv2.imshow("My Lenna", destination)
cv2.imshow("Lenna Expectation", output)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.destroyAllWindows()
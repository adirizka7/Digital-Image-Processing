import numpy as np
import cv2

cameraman = cv2.imread('k_cameraman.jpg', 0)
equalized = cv2.imread('k_equalized.jpg', 0)

row, col = cameraman.shape
rowe, cole = equalized.shape

rata, rata2 = 0, 0
for i in range(row):
	for j in range(col):
		rata += cameraman[i,j]
		rata2 += equalized[i,j]

rata /= (row*col)
rata2 /= (row*col)

new_image_c = np.zeros((row, col, 1), np.uint8)
new_image_e = np.zeros((rowe, cole, 1), np.uint8)

for i in range(row):
	for j in range(col):
		new_image_c[i, j] = cameraman[i, j]*0.5 if cameraman[i,j] < rata else 2*cameraman[i, j]
		new_image_e[i, j] = equalized[i, j]*0.5 if equalized[i,j] < rata2 else 2*equalized[i, j]

final_image = np.zeros((row, col, 1), np.uint8)

for i in range(row):
	for j in range(col):
		res = 0 if new_image_e[i,j] == new_image_c[i,j] else new_image_e[i,j]
		final_image.itemset((i, j, 0), res)

cv2.imshow('Final', final_image)
cv2.imshow('Cameraman', cameraman)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
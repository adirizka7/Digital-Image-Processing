import cv2
import numpy as np

img = cv2.imread("ilkom.jpg")

H,W = img.shape[:2]
gray = np.zeros((H,W), np.uint8)
for i in range(H):
	for j in range(W):
		gray[i,j] = np.clip(0.299* img[i,j,0]  + 0.587 * img[i,j,1] + 0.114 * img[i,j,2], 0, 255)

H,W = img.shape[:2]
inv = np.zeros((H,W), np.uint8)
for i in range(H):
	for j in range(W):
		inv[i,j] = np.clip(abs(img[i,j,0]-255), abs(img[i,j,1]-255), abs(img[i,j,2]-255))

H, W = img.shape[:2]
thresh = np.zeros((H, W), np.uint8)
for i in range(H):
	for j in range(W):
		thresh[i, j] = np.clip(img[i, j, 0] if img[i, j, 0] > 150 else 0, img[i, j, 1] if img[i, j, 1] > 150 else 0, img[i, j, 2] if img[i, j, 2] > 150 else 0)

cv2.imwrite("grayscale.jpg", gray)
cv2.imshow("gray", gray)
cv2.imwrite("invert.jpg",inv)
cv2.imshow("invert", inv)
cv2.imwrite("thresh_tozero.jpg",thresh)
cv2.imshow("thresh_tozero",thresh)
cv2.waitKey()
cv2.destroyAllWindows()
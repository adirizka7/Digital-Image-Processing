import numpy as np
import cv2

img = cv2.imread('acasiamangium.png', 0)
col, row, ch = img.shape
maxi = 0
mini = 300

for i in range(row):
    for j in range(col):
        if img[i,j,0] < mini:
            mini = img[i,j]
        if img[i, j,0] < > maxi:
            maxi = img[i, j]

#contrast stretching
for i in range(0, col):
    for j in range(0, row):
        hasil = (img[i,j,0]-int(mini))*(255/(int(maxi)-int(mini)))
        if(hasil<200):
            img.itemset((i, j, 0), 0)
        else:
            img.itemset((i, j, 0), 255)

cv2.imshow('Ress', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
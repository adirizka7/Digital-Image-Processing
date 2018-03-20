import cv2
import numpy as np
 
img = cv2.imread("koinIPB.jpg")
cv2.imshow("koinIPB aseli", img)
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
 
#Fungsi konvolusi manual
def konvolusi(image, mask):
    row, col, ch = image.shape
    kanvas = np.zeros((row, col, 1), np.uint8)
    rowMask, colMask = mask.shape
    for i in range(0, row):
        for j in range(0, col):
            imageSum = maskSum = 0
            for a in range(int(-rowMask/2), int(rowMask-rowMask/2)):
                for b in range(int(-colMask/2), int(colMask-colMask/2)):
                    if((1+a)>=0 and (j+b)>=0):
                        imageSum += image[i+a, j+b] * mask[a+int(rowMask)//2, b+int(colMask)//2]
                        maskSum += mask[a+int(rowMask)//2, b+int(colMask)//2]
            intensitas = imageSum/maskSum
            print(intensitas)
    #         if(intensitas > 255):
    #             intensitas = 255
    #         elif(intensitas < 0):
    #             intensitas = 0
    #         kanvas.itemset((i, j, 0), intensitas)
    # return kanvas
 
hasil = konvolusi(img, kernel)
cv2.imshow("hasil konvolusi", hasil)
 
cv2.waitKey()
cv2.destroyAllWindows()
import Image

import cv2
import numpy as np
import time

img0 = cv2.imread('bloc0.jpg')
img1 = cv2.imread('bloc1.jpg')
def animation(mat):



    M, N,a = img1.shape
    imgf = np.zeros(( N * (len(mat)),M * len(mat[0]), 3), np.uint8)
    cv2.imshow('w',imgf)
    cv2.moveWindow('w', 200, 0);


    for i in range(len(mat)):
      for j in range(len(mat[0])):
                if (mat[i][j]):
                    imgf[i * M: i * M+M,j * N:j * N+N]=img1
                else:
                    imgf[i * M: i * M+M,j * N:j * N+N]=img0

                cv2.imshow('w', imgf)
                cv2.moveWindow('w', 200, 0);
      cv2.waitKey(80)
    while(1):
     if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
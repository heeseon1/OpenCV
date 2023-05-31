import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print("Image load failed!")
    sys.exit()

dst_add = cv2.add(src1, src2)
dst_addWeighted = cv2.addWeighted(src1, 0.5, src2, 0.5, 0, 0.0)
dst_subtract = cv2.subtract(src1, src2)
dst_subtract2 = cv2.subtract(src2, src1)
dst_absdiff = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(dst_add, 'gray'), plt.title('add')
plt.subplot(232), plt.axis('off'), plt.imshow(dst_addWeighted, 'gray'), plt.title('addWeighted')
plt.subplot(233), plt.axis('off'), plt.imshow(dst_subtract, 'gray'), plt.title('subtract')
plt.subplot(234), plt.axis('off'), plt.imshow(dst_subtract2, 'gray'), plt.title('subtract2')
plt.subplot(235), plt.axis('off'), plt.imshow(dst_absdiff, 'gray'), plt.title('absdiff')
plt.show()
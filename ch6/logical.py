import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)
if src1 is None or src2 is None:
    print("Image load failed!")
    sys.exit()

dst_and = cv2.bitwise_and(src1, src2)
dst_or = cv2.bitwise_or(src1, src2)
dst_xor = cv2.bitwise_xor(src1, src2)
dst_not = cv2.bitwise_not(src1)
dst_not2 = cv2.bitwise_not(src2)

plt.subplot(231), plt.axis('off'), plt.imshow(dst_and, 'gray'), plt.title('and')
plt.subplot(232), plt.axis('off'), plt.imshow(dst_or, 'gray'), plt.title('or')
plt.subplot(233), plt.axis('off'), plt.imshow(dst_xor, 'gray'), plt.title('xor')
plt.subplot(234), plt.axis('off'), plt.imshow(dst_not, 'gray'), plt.title('not')
plt.subplot(235), plt.axis('off'), plt.imshow(dst_not2, 'gray'), plt.title('not2')
plt.show()
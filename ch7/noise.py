import cv2
import numpy as np
import random

def gaussian_noise():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("image load failed!")
        return

    cv2.imshow('src',src)

    for stddev in [10, 20, 30]:
        noise = np.zeros(src.shape, np.int32)
        cv2.randn(noise, 0, stddev)

        dst = cv2.add(src, noise, dtype=cv2.CV_8UC1)

        cv2.imshow('dst',dst)
        cv2.waitKey()
    cv2.destroyAllWindows()

def bilateral_Filter():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("image load failed!")
        return

    cv2.imshow('src',src)

    noise = np.zeros(src.shape, np.int32)
    cv2.randn(noise, 0, 5)
    cv2.add(src, noise, src, dtype=cv2.CV_8UC1)

    dst1 = cv2.GaussianBlur(src, (0,0), 5)
    dst2 = cv2.bilateralFilter(src,-1, 10, 5)

    cv2.imshow('src',src)
    cv2.imshow('dst1',dst1)
    cv2.imshow('dst2',dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

def filter_median():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    for i in range(0, int(src.size / 10)):
        x = random.randint(0, src.shape[1] - 1)
        y = random.randint(0, src.shape[0] - 1)
        src[x, y] = (i % 2) * 255

    dst1 = cv2.GaussianBlur(src, (0, 0), 1)
    dst2 = cv2.medianBlur(src, 3)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    gaussian_noise()
    bilateral_Filter()
    filter_median()



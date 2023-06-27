import cv2
import numpy as np

def inverse():
    src = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = np.zeros(src.shape, src.dtype)

    for j in range(src.shape[0]):
        for i in range(src.shape[1]):
            src_pixel = src[j, i]
            dst_pixel = dst[j, i]

            dst_pixel[0] = 255 - src_pixel[0]
            dst_pixel[1] = 255 - src_pixel[1]
            dst_pixel[2] = 255 - src_pixel[2]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def inverse_def():
    src = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.bitwise_not(src)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__' :
    inverse()
    inverse_def()

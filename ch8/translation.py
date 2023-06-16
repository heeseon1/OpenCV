import numpy as np
import cv2

def affine_translation():
    src = cv2.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    affine_mat = np.array([[1, 0, 50],
                           [0, 1, 200]]).astype(np.float32)

    dst = cv2.warpAffine(src, affine_mat, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    affine_translation()
import cv2

def affine_flip():
    src = cv2.imread('eastsea.bmp')

    if src is None:
        print('Image load failed!')
        return

    dst1 = cv2.flip(src,1)
    dst2 = cv2.flip(src,0)
    dst3 = cv2.flip(src,-1)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst3)
    cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    affine_flip()

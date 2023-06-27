import cv2


def image_cg():
    color_src = cv2.imread('butterfly.jpg', cv2.IMREAD_COLOR)
    gray_src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

    if color_src is None:
        print('Image load failed!')
        return

    if gray_src is None:
        print('Image load failed!')
        return

    print('color_src.shape:', color_src.shape)
    print('color_src.dtype:', color_src.dtype)
    print('color_src pixel value [B, G, R] at (0, 0) is', color_src[0, 0])

    print('gray_src.shape:', gray_src.shape)
    print('gray_src.dtype:', gray_src.dtype)
    print('gray_src pixel value [B, G, R] at (0, 0) is', gray_src[0, 0])


if __name__ == '__main__':
    image_cg()


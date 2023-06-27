import cv2

def erode_dilate():
    src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image load failed!")
        return

    _, src_threshold = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dst_erode = cv2.erode(src_threshold, None)
    dst_dilate = cv2.dilate(src_threshold, None)

    cv2.imshow('src', src)
    cv2.imshow('src_threshold', src_threshold)
    cv2.imshow('dst_erode', dst_erode)
    cv2.imshow('dst_dilate', dst_dilate)
    cv2.waitKey()
    cv2.destroyAllWindows()

def morphologyex():
    src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image load failed!")
        return

    _, src_threshold = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dst_open = cv2.morphologyEx(src_threshold, cv2.MORPH_OPEN, None)
    dst_close = cv2.morphologyEx(src_threshold, cv2.MORPH_CLOSE, None)

    cv2.imshow('src', src)
    cv2.imshow('src_threshold', src_threshold)
    cv2.imshow('dst_open', dst_open)
    cv2.imshow('dst_close', dst_close)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    erode_dilate()
    morphologyex()
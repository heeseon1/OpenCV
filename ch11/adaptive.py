import cv2

def treshold_adaptive():
    src = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image load failed!")
        return

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15,10)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    treshold_adaptive()
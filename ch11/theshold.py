import cv2

def treshold_test():
    src = cv2.imread('neutrophils.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("Image load failed!")
        return

    _, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    treshold_test()
import cv2

def cvtColor_ex():
    src = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    dst2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    dst3 = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst3)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    cvtColor_ex()


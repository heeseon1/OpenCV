import cv2

def inrange():
    src = cv2.imread('candies.png')

    if src is None:
        print('Image load failed!')
        return

    src_hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

    dst = cv2.inRange(src, (100, 0, 0), (255, 150, 150))
    dst_hsv = cv2.inRange(src_hsv, (150,0,50), (255,80,255))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('dst_hsv', dst_hsv)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    inrange()

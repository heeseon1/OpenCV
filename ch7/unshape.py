import cv2

def unshape():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print("Image load failed!")
        return

    def callback(alpha):
        for sigma in range(1,11):
            blurred = cv2.GaussianBlur(src, (0,0), sigma)
            dst = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)
            cv2.imshow('dst', dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('unshape', 'dst', 0, 10, callback)
    callback(0)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    unshape()






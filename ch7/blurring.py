import cv2
from matplotlib import pyplot as plt
import sys

def blurring_filter():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    cv2.imshow('src', src)

    dst3 = cv2.blur(src, ksize=(3,3))
    dst5 = cv2.blur(src, ksize=(5,5))
    dst7 = cv2.blur(src, ksize=(7,7))

    cv2.imshow('dst3', dst3)
    cv2.imshow('dst5', dst5)
    cv2.imshow('dst7', dst7)
    cv2. waitKey()
    cv2.destroyAllWindows()



def Gaussianblur_filter():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    cv2.imshow('src', src)

    for sigma in range(1,6):
        dst = cv2.GaussianBlur(src, (0,0), sigma)
        cv2.imshow('dst', dst)
        cv2. waitKey()

    cv2.destroyAllWindows()

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed!")
    sys.exit()

gaussian1 = cv2.GaussianBlur(src, (0,0), 1)
gaussian2 = cv2.GaussianBlur(src, (0,0), 2)
gaussian3 = cv2.GaussianBlur(src, (0,0), 3)
gaussian4 = cv2.GaussianBlur(src, (0,0), 4)
gaussian5 = cv2.GaussianBlur(src, (0,0), 5)

plt.subplot(231), plt.axis('off'), plt.imshow(gaussian1, 'gray'), plt.title('1')
plt.subplot(232), plt.axis('off'), plt.imshow(gaussian2, 'gray'), plt.title('2')
plt.subplot(233), plt.axis('off'), plt.imshow(gaussian3, 'gray'), plt.title('3')
plt.subplot(234), plt.axis('off'), plt.imshow(gaussian4, 'gray'), plt.title('4')
plt.subplot(235), plt.axis('off'), plt.imshow(gaussian5, 'gray'), plt.title('5')
plt.show()

if __name__ == '__main__' :
    blurring_filter()
    Gaussianblur_filter()





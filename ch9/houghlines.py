import cv2
import math

def hough_lines():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv2.Canny(src, 50, 250)
    lines = cv2.HoughLines(edge, 1, math.pi / 150, 200)

    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)
            x0, y0 = rho * cos_t, rho * sin_t

            alpha = 1000
            pt1 = (int(x0 - alpha * sin_t), int(y0 + alpha * cos_t))
            pt2 = (int(x0 + alpha * sin_t), int(y0 - alpha * cos_t))
            cv2.line(dst, pt1, pt2, (0, 100, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def hough_linesP():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    edge = cv2.Canny(src, 50, 150)
    lines = cv2.HoughLinesP(edge, 1, math.pi / 180, 150, minLineLength=100, maxLineGap=10)

    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in lines:
            x1,y1,x2,y2 = i[0]
            cv2.line(dst, (x1,y1), (x2,y2), (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    hough_lines()
    hough_linesP()
import sys
import cv2

src = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2H)
h, s, v= cv2.split(v)
v = cv2.equalizeHist(v)

dst_ycrcb = cv2.merge([h,s,v])
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
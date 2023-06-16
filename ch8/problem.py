import random
import cv2

def camera_in():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        dst1 = cv2.GaussianBlur(frame,(0,0),1)
        dst2 = cv2.medianBlur(frame, 3)

        cv2.imshow('frame', frame)
        cv2.imshow('dst1', dst1)
        cv2.imshow('dst2', dst2)

        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_in()
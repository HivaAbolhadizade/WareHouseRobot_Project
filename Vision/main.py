import cv2
import imutils
from imutils.video import VideoStream
import time
import Tools as tl
import Box_Detection as bd





if __name__ == "__main__":
    cam = cv2.VideoCapture(0)  # change this index with respect to your device.
    time.sleep(2.0)

    uhsv = (13, 255, 187)
    lhsv = (0, 182, 107)
    erode = 7
    dilate = 42
    notfound = True

    while True:
        # time.sleep(0.7)

        print("Search for ball")
        output, notfound = bd.detect_box(frame, uhsv, lhsv, erode, dilate, 10)

    print("________________End of The Program________________")

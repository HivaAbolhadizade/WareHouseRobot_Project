import cv2
import imutils
import time


def get_frame(cam=cv2.VideoCapture(1)):
    ret, frame = cam.read()
    resized_frame = imutils.resize(frame, width=500)

    return ret, resized_frame

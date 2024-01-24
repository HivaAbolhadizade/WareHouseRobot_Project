import cv2
import imutils
from imutils.video import VideoStream
import time


def get_frame(cam):
    ret, frame = cam.read()
    resized_frame = imutils.resize(frame, width=600)

    width = resized_frame.shape[1]
    height = resized_frame.shape[0]
    center_cord = (width // 2,  height // 2)

    cv2.line(resized_frame, pt1=(0, height // 2), pt2=(width, height // 2), color=(0, 255, 0), thickness=2)
    cv2.line(resized_frame, pt1=(width // 2, 0), pt2=(width // 2, height), color=(0, 255, 0), thickness=2)

    cv2.circle(resized_frame, center=center_cord, radius=2, thickness=5, color=(0, 0, 255))

    sp = (3 * center_cord[0] // 4, 3 * center_cord[1] // 4)
    ep = (width - sp[0], height - sp[1])

    cv2.rectangle(resized_frame, sp, ep, color=(255, 0, 0), thickness=3)

    return resized_frame








    return ret, resized_frame

# def draw_rect(rect, frame, center):
#     center = tuple(map(int, rect[0]))
#     size = tuple(map(int, rect[1]))
#
#     sp = (int(center[0] - size[0] / 2), int(center[1] - size[1] / 2))
#     ep = (int(center[0] + size[0] / 2), int(center[1] + size[1] / 2))
#
#     cv2.rectangle(frame, sp, ep, (255, 0, 0), 2)
#     cv2.circle(frame, center=center, radius=5, (255, 255, 255), -1)
#
#
#     return center


cam = cv2.VideoCapture(1)
while True:
    # ret, frame = get_frame(cam=cam)  # shape of the frame : (hight, width, channel)
    # print(frame)
    """
    ret, frame = cam.read()

    # print(ret)
    # print(frame)
    resized_frame = imutils.resize(frame, width=600)

    width = resized_frame.shape[1]
    height = resized_frame.shape[0]
    center_cord = (width // 2, height // 2)

    cv2.line(resized_frame, pt1=(0, height // 2), pt2=(width, height // 2), color=(0, 255, 0), thickness=2)
    cv2.line(resized_frame, pt1=(width // 2, 0), pt2=(width // 2, height), color=(0, 255, 0), thickness=2)

    cv2.circle(resized_frame, center=center_cord, radius=2, thickness=5, color=(0, 0, 255))

    sp = (3 * center_cord[0] // 4, 3 * center_cord[1] // 4)
    ep = (width - sp[0], height - sp[1])

    cv2.rectangle(resized_frame, sp, ep, color=(255, 0, 0), thickness=3)
    """
    resized_frame = get_frame(cam)
    cv2.imshow('stream', resized_frame)
    # print(frame.shape)
    key = cv2.waitKey(1)
    if key == ord('e'):
        break



cam.release()
cv2.destroyAllWindows()
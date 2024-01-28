import cv2
import imutils
from imutils.video import VideoStream
import time
import numpy as np
# from Tools import draw_rect





def detect_box(frame, upper_hsv, lower_hsv, erode, dilate, num_box=1):
    """
    This method finds the center of the ball and detects the ball using color thresholding in HSV.
    :param frame: A (width, height, 3) array, representing our RGB image.
    :param upper_hsv: A number, the upper bound of HSV for color thresholding.
    :param lower_hsv: A number, the lower bound of HSV for color thresholding.
    :param erode: Erosion is a morphological operation that has the effect of "shrinking"
        or eroding the boundaries of the white regions in the binary image.
        It is particularly useful for removing small white objects,
        separating overlapping objects, or breaking thin connections between objects.
    :param dilate: Complementary to erosion. While erosion tends to "shrink" the boundaries of white regions in a binary image,
            dilation has the opposite effect – it tends to "expand" or grow the white regions.
            Dilate is often used to accentuate or emphasize features in an image.
    :return: None if there is no ball in front of the camera,
    else, a tuple (x, y) that are the coordinates of the center of the ball.
    """
    # init default values of the output
    center = None
    size = 0

    # resizing the frame so that it would be easier to handle the image and also lowers the computation.
    frame = imutils.resize(frame, width=600)

    # reducing the details in the frame.
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # converting the RGB color space of the image (frame) to HSV color space
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # color thresholding in hsv system
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    """  
        Erosion is a morphological operation that has the effect of "shrinking"
        or eroding the boundaries of the white regions in the binary image.
        It is particularly useful for removing small white objects,
        separating overlapping objects, or breaking thin connections between objects. 
    """
    mask = cv2.erode(mask, None, iterations=erode)
    """
            complementary to erosion. While erosion tends to "shrink" the boundaries of white regions in a binary image,
            dilation has the opposite effect – it tends to "expand" or grow the white regions.
            Dilate is often used to accentuate or emphasize features in an image.
    """
    mask = cv2.dilate(mask, None, iterations=dilate)

    # finding contours of the processed frame
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # using imutils to make sure we have pure contours and nothing else with it.
    cnts = imutils.grab_contours(cnts)

    # if we've had any contours in the picture,
    # we will find the center of the ball and return it as output, else we return None as output
    if len(cnts) > 0:
        # c is a contour that hase the biggest area among all contours that we found in the frame.
        cnt = max(cnts, key=cv2.contourArea)

        # finding the smallest enclosing circle
        rect = cv2.minAreaRect(cnt)

        center = tuple(map(int, rect[0]))
        size = tuple(map(int, rect[1]))

        sp = (int(center[0] - size[0] / 2), int(center[1] - size[1] / 2))
        ep = (int(center[0] + size[0] / 2), int(center[1] + size[1] / 2))

        cv2.rectangle(frame, sp, ep, (0, 0, 255), 2)
        cv2.circle(frame, center, 5, (255, 255, 255), -1)

    # Adding lines and rects to the frame.
    width = frame.shape[1]
    height = frame.shape[0]
    center_cord = (width // 2, height // 2)

    cv2.line(frame, pt1=(0, height // 2), pt2=(width, height // 2), color=(0, 255, 0), thickness=2)
    cv2.line(frame, pt1=(width // 2, 0), pt2=(width // 2, height), color=(0, 255, 0), thickness=2)

    cv2.circle(frame, center=center_cord, radius=2, thickness=5, color=(0, 0, 255))

    sp = (3 * center_cord[0] // 4, 3 * center_cord[1] // 4)
    ep = (width - sp[0], height - sp[1])

    cv2.rectangle(frame, sp, ep, color=(255, 0, 0), thickness=3)

    return frame, center, size, {"frame_center": center_cord, "sp": sp, "ep": ep, "shape": (width, height)}


"""
if __name__ == "__main__":
    vs = imutils.video.VideoStream(src=1).start()
    time.sleep(2.0)

    # # purple box
    # uhsv = (169, 179, 193)
    # lhsv = (140, 48, 76)
    # erode = 3
    # dilate = 11

    # green box
    uhsv = (93, 255, 199)
    lhsv = (42, 121, 39)
    erode = 0
    dilate = 5

    # # brown box
    # uhsv = (25, 136, 157)
    # lhsv = (17, 56, 131)
    # erode = 10
    # dilate = 21


    while True:
        frame = vs.read()
        img, center, size, cam_info = detect_box(frame, uhsv, lhsv, erode, dilate)
        # print(center[0])
        # print(cam_info['frame_center'])
        # print(cam_info['sp'])
        # print(cam_info['ep'])

        # edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # combined_image = np.hstack((edges, img))


        cv2.imshow("VideoStream", img)

        key = cv2.waitKey(1)  # this is really important that it should be waitkey(1) not waitkey(0)
        if key == 'q':
            break

    print("________________end of the program________________")
"""
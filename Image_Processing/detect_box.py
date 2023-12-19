import cv2
import imutils
from imutils.video import VideoStream
import time


def detect_ball(frame, upper_hsv, lower_hsv, erode, dilate):
    """
    This method finds the center of the ball and detects the ball using color thresholding in HSV.
    :param frame: A (width, height, 3) array, representing our RGB image.
    :param upper_hsv: A number, the upper bound of HSV for color thresholding.
    :param lower_hsv: A number, the lower bound of HSV for color thresholding.
    :param erode:
    :param dilate:
    :return: None if there is no ball in front of the camera,
    else, a tuple (x, y) that are the coordinates of the center of the ball.
    """
    output = None
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
    cv2.imwrite(
        r'/Image_Processing/test/mask.png',
        mask)
    # finding contours of the processed frame
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # using imutils to make sure we have pure contours and nothing else with it.
    cnts = imutils.grab_contours(cnts)
    # if we've had any contours in the picture,
    # we will find the center of the ball and return it as output, else we return None as output
    if len(cnts) > 0:
        # c is a contour that hase the biggest area among all contours that we found in the frame.
        c = max(cnts, key=cv2.contourArea)

        # finding the smallest enclosing circle
        rect = cv2.minAreaRect(c)
        center = rect[0]
        size = rect[1]

        center = tuple(map(int, center))

        print(center)
        print(size)

        # draw the rect and its center of the frame
        sp = (int(center[0] - size[0] / 2), int(center[1] - size[1] / 2))
        ep = (int(center[0] + size[0] / 2), int(center[1] + size[1] / 2))

        cv2.rectangle(frame, sp, ep, (255, 0, 0), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # Display the frame
        cv2.imshow('Captured img', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        output = center

        # cv2.imwrite(
        #         r'E:\University of Kerman\Term 5\Computer Architecture\Project\Robot_Project\Image_Processing\test',
        #         frame)
        return output, False


    return output, True


if __name__ == "__main__":
    vs = imutils.video.VideoStream(src=1).start()
    time.sleep(2.0)

    uhsv = (13, 255, 187)
    lhsv = (0, 182, 107)
    erode = 7
    dilate = 42
    notfound = True
    while notfound:
        time.sleep(0.7)
        frame = vs.read()
        print("Search for ball")
        output, notfound = detect_ball(frame, uhsv, lhsv, erode, dilate)
    print("________________end of the program________________")

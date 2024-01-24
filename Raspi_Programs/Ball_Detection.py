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
    :return: (the frame taken frame the camera, )
    """
    center = None  # this is a tuple which is the cordination of the center
    radius = 0  # this is the radious of the ball found, it will get value later in the code.

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
        r'/home/ca2023/Desktop/mask.png',
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
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        # Calculate the moments of the contour
        M = cv2.moments(c)

        # finding the center of the surface using moments
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        # Check if the radius of the enclosing circle is within a specific range.
        # We check this so that if other objects had the same color intensity, they would not be detected as the target ball.
        if radius > 10 and radius < 170:
            # Drawing the enclosing circle
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

            # Drawing the center of the circle
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            print(radius)
            print(center)

            # return frame, center, radius, True

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

    return frame, center, radius, {"frame_center": center_cord, "sp": sp, "ep": ep}


if __name__ == "__main__":
    vs = imutils.video.VideoStream(src=1).start()
    time.sleep(2.0)
    # green ball
    uhsv = (93, 255, 199)
    lhsv = (42, 121, 39)
    erode = 0
    dilate = 5
    # # purple ball
    # uhsv = (144, 171, 224)
    # lhsv = (121, 109, 89)
    # erode = 1
    # dilate = 10

    while True:
        # time.sleep(0.7)
        # print("in loop")
        frame = vs.read()
        # print("Search for ball")
        img, center, radius, cam_info = detect_ball(frame, uhsv, lhsv, erode, dilate)

        cv2.imshow("VideoStream", img)
        # if notfound is False:
        #     print(img.shape)
        #     print(type(img))
        #     cv2.imshow("contour", img)
        key = cv2.waitKey(1)  # this is really important that it should be waitkey(1) not waitkey(0)
        if key == 'q':
            break

    print("________________end of the program________________")

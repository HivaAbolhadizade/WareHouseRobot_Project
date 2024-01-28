import RPi.GPIO as GPIO
import time
import cv2
# from servo import *
# import Movement_v2 as Moving
from imutils.video import VideoStream
from Sign_Detection import detect_sign
from Box_Detection import detect_box
from cmd_auto import *

if __name__ == "__main__":
    # Starting the camera
    vs = VideoStream(src=0).start()
    time.sleep(4.0)

    # Args
    gate_state = False
    box_state = True

    # Green box threshold
    buhsv = (93, 255, 199)
    blhsv = (42, 121, 39)
    berode = 0
    bdilate = 5

    # # purple ball
    # uhsv = (144, 171, 224)
    # lhsv = (121, 109, 89)
    # erode = 1
    # dilate = 10

    # yellow gate
    guhsv = (28, 255, 211)
    glhsv = (23, 210, 169)
    gerode = 0
    gdilate = 0

    try:
        while True:
            # Getting frame from webcam
            # time.sleep(0.5)
            frame = vs.read()

            if box_state:
                isBoxDetected = False
                frame, center, size, frame_info = detect_box(frame=frame, upper_hsv=buhsv, lower_hsv=blhsv,
                                                             erode=berode,
                                                             dilate=bdilate)

                cv2.imshow("VideoStream", frame)

                key = cv2.waitKey(1)
                if key == 'e':
                    break

                # Checking if we have seen the ball
                if size != 0: isBoxDetected = True

                if isBoxDetected is True:
                    x_box = center[0]
                    y_box = center[1]
                else:
                    turn_right(0.1)
                    right_touch()
                    backward(0.1)
                    back_touch()
                    continue

                # l_bound = frame_info['sp'][0]
                # r_bound = frame_info['ep'][0]

                # this should be deleted, just for test%
                l_bound = 260
                r_bound = 340

                if y_box >= 408:
                    if l_bound <= x_box <= r_bound:  # should change this later%
                        avg_dist = distance()
                        if avg_dist > 6:
                            forward(power=0.1)

                        close_catcher()
                        print("___ CATCHING THE BALL ___")

                        # Changing the state, transferring the robot to gate state
                        box_state = False
                        gate_state = True

                        continue

                    else:
                        backward(power=0.1)
                        back_touch()
                        continue

                if l_bound <= x_box <= r_bound:
                    forward()
                    continue

                elif x_box > r_bound:
                    turn_right()  # we can find a formula based on the distance to r bound for power$
                    right_touch()
                    continue

                elif x_box < l_bound:
                    turn_left()  # we can find a formula based on the distance to r bound for power$
                    left_touch()
                    continue

            if gate_state:
                isGateDetected = False
                frame, center, radius, frame_info = detect_sign(frame=frame, upper_hsv=guhsv, lower_hsv=glhsv,
                                                                erode=gerode,
                                                                dilate=gdilate)

                if radius != 0: isGateDetected = True

                cv2.imshow("VideoStream", frame)
                key = cv2.waitKey(1)
                if key == 'e':
                    break

                # Checking if we have seen the ball if radius != 0: isBallDetected = True
                if isGateDetected is True:
                    x_gate = center[0]
                    y_gate = center[1]
                else:
                    turn_right()
                    continue
                if radius > 78:
                    if l_bound <= x_gate <= r_bound:
                        open_catcher()
                        backward()
                        back_touch()

                        print("Relaesing Catcher")

                        box_state = True
                        gate_state = False
                        open_catcher()
                        print("________End of The Program________")
                        break


                elif l_bound <= x_gate <= r_bound:
                    forward()
                    continue

                elif x_gate > r_bound:
                    turn_right()  # we can find a formula based on the distance to r bound for power$
                    right_touch()
                    continue

                elif x_gate < l_bound:
                    turn_left()  # we can find a formula based on the distance to r bound for power$
                    left_touch()
                    continue








    finally:
        GPIO.cleanup()

        # gateOutPut = detectGate(frame=frame)
        # if gateOutput is not None and isBallcatched:
        #     if 200 <= gateOutPut[0] <= 400:
        #         print("Moving Forward")
        #         Moving.forward()
        #     # change it
        #     # if distance() < 22:
        #     #     print("gate catched")
        #     #     servo.open_catcher()
        #     #     GPIO.cleanup()
        #     #     # change this part
        #     #     exit()
        #
        #     elif 200 >= gateoutPut[0]:
        #         Moving.turn_right(power=0.1)
        #
        #     elif gateoutPut[0] >= 400:
        #         Moving.turn_left(power=0.1)
        #
        # if output is not None and not isBallcatched:
        #     if output[0] <= 400:
        #         print("Moving Forward")
        #         Moving.forward()
        #         # if distance() < 14:
        #         #     print("ball catched")
        #         #     servo.close_catcher()
        #         #     isBallCatched = True
        #
        #     elif 200 <= output[o]:
        #         print("slow turn left")
        #         # Moving.turn_left(power=0.1)
        #         turn_left(0.1)
        #     else:
        #
        #         print("slow turn right")
        #         # Moving.turn_right(power=0.1)
        #         turn_right(0.1)
        #
        # elif not isBallcatched:
        #     print("searching for ball")
        #     # Moving.turn_right(power=0.2)
        #     turn_right(0.2)
        #
        # elif isBallcatched and gateoutput is None:
        #     print("searching for gate")
        #     # Moving.turn_right(power=0.1)
        #     turn_right(0.2)

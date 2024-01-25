# import RPi.GPIO as GPIO
import time
import cv2
# from servo import *
# import Movement_v2 as Moving
from imutils.video import VideoStream
from Ball_Detection import detect_ball

# _____Parameters_____
# Pin numbering as needed

# back_motors
B_IN1 = 6
B_IN2 = 5
B_IN3 = 4
B_IN4 = 26
# front_motors
F_IN1 = 27
F_IN2 = 22
F_IN3 = 23
F_IN4 = 24
# ulteronic
PIN_TRIGGER = 19
PIN_ECHO = 9

sleep_time = 1


# _____Functions_____
def setup_gpios():
    print("GPIO setup")
    """
    GPIO.setmode(GPIO.BCM)
    '''
    # setting up ultras
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECGO, GPIO.IN)
    '''
    # setting up driver motors
    GPIO.setup(B_IN1, GPIO.OUT)
    GPIO.setup(B_IN2, GPIO.OUT)
    GPIO.setup(B_IN3, GPIO.OUT)
    GPIO.setup(B_IN4, GPIO.OUT)
    GPIO.setup(F_IN1, GPIO.OUT)
    GPIO.setup(F_IN2, GPIO.OUT)
    GPIO.setup(F_IN3, GPIO.OUT)
    GPIO.setup(F_IN4, GPIO.OUT)
    """


def forward(power=0.5):
    print("Forward")
    """
    GPIO.output(F_IN4, True)
    GPIO.output(F_IN1, True)
    GPIO.output(B_IN4, True)
    GPIO.output(B_IN1, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(F_IN1, False)
    GPIO.output(B_IN4, False)
    GPIO.output(B_IN1, False)
    """


def backward(power=0.5):
    print("Backward")
    """
    GPIO.output(F_IN3, True)
    GPIO.output(F_IN2, True)
    GPIO.output(B_IN3, True)
    GPIO.output(B_IN2, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN3, False)
    GPIO.output(F_IN2, False)
    GPIO.output(B_IN3, False)
    GPIO.output(B_IN2, False)
    """


def turn_right(power=0.8):
    print("Right")
    """
    GPIO.output(B_IN1, True)
    GPIO.output(F_IN1, True)
    # GPIO.output(B_IN3, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN1, False)
    GPIO.output(B_IN1, False)
    # GPIO.output(B_IN3, False)
    """


def turn_left(power=0.8):
    print("Left")
    """
    GPIO.output(F_IN4, True)
    GPIO.output(B_IN4, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(B_IN4, False)
    """


def distance():
    print("Measuring distance")
    """
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)
    print("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()

    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)

    print("Distance:", distance, "cm")
    return distance
    """
    return 5


if __name__ == "__main__":
    # Starting the camera
    vs = VideoStream(src=1).start()
    time.sleep(2.0)

    # Args
    gate_state = False
    ball_state = True

    # Green ball threshold
    uhsv = (93, 255, 199)
    lhsv = (42, 121, 39)
    erode = 0
    dilate = 5

    isBallCatched = False

    while True:
        # Getting frame from webcam
        time.sleep(0.5)
        frame = vs.read()

        if ball_state:
            isBallDetected = False
            frame, center, radius, frame_info = detect_ball(frame=frame, upper_hsv=uhsv, lower_hsv=lhsv, erode=erode,
                                                            dilate=dilate)

            cv2.imshow("VideoStream", frame)

            key = cv2.waitKey(1)
            if key == 'e':
                break

            # Checking if we have seen the ball
            if radius != 0: isBallDetected = True

            if isBallDetected is True:
                x_ball = center[0]
                y_ball = center[1]
            else:
                turn_right()
                continue

            # l_bound = frame_info['sp'][0]
            # r_bound = frame_info['ep'][0]

            # this should be deleted, just for test%
            l_bound = 260
            r_bound = 340

            if y_ball >= 408:
                if l_bound <= x_ball <= r_bound:  # should change this later%
                    avg_dist = sum([distance() for i in range(3)]) // 3
                    if avg_dist > 6:
                        forward(power=0.1)

                    print("___ CATCHING THE BALL ___")

                    # Changing the state, transferring the robot to gate state
                    ball_state = False
                    gate_state = True

                    continue

                else:
                    backward(power=0.5)
                    continue

            if l_bound <= x_ball <= r_bound:
                forward()
                continue

            elif x_ball > r_bound:
                turn_right()  # we can find a formula based on the distance to r bound for power$
                continue

            elif x_ball < l_bound:
                turn_left()  # we can find a formula based on the distance to r bound for power$
                continue

        # if gate_state:
        break

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

import RPi.GPIO as GPIO
import time

from servo import *
import Movement_v2 as Moving

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


def forward(power=0.5):
    GPIO.output(F_IN4, True)
    GPIO.output(F_IN1, True)
    GPIO.output(B_IN4, True)
    GPIO.output(B_IN1, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(F_IN1, False)
    GPIO.output(B_IN4, False)
    GPIO.output(B_IN1, False)


def backward(power=0.5):
    GPIO.output(F_IN3, True)
    GPIO.output(F_IN2, True)
    GPIO.output(B_IN3, True)
    GPIO.output(B_IN2, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN3, False)
    GPIO.output(F_IN2, False)
    GPIO.output(B_IN3, False)
    GPIO.output(B_IN2, False)


def turn_right(power=0.8):
    GPIO.output(B_IN1, True)
    GPIO.output(F_IN1, True)
    # GPIO.output(B_IN3, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN1, False)
    GPIO.output(B_IN1, False)
    # GPIO.output(B_IN3, False)


def turn_left(power=0.8):
    GPIO.output(F_IN4, True)
    GPIO.output(B_IN4, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(B_IN4, False)


def distance():
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


if __name__ == "__main__":
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    isBallCatched = False

    while True:
        time.sleep(0.7)
        frame = vs.read()
        output = detecting_ball(frame=frame)
        gateOutPut = detectGate(frame=frame)
        if gateOutput is not None and isBallcatched:
            if 200 <= gateOutPut[0] <= 400:
                print("Moving Forward")
                Moving.forward()
            # change it
            if distance() < 22:
                print("gate catched")
                servo.open_catcher()
                GPIO.cleanup()
                # change this part
                exit()

            elif 200 >= gateoutPut[0]:
                Moving.turn_right(power=0.1)

            elif gateoutPut[0] >= 400:
                Moving.turn_left(power=0.1)

        if output is not None and not isBallcatched:
            if output[0] <= 400:
                print("Moving Forward")
                Moving.forward()
                if distance() < 14:
                    print("ball catched")
                    servo.close_catcher()
                    isBallCatched = True

            elif 200 <= output[o]:
                print("slow turn left")
                Moving.turn_left(power=0.1)
            else:
                print("slow turn right")
                Moving.turn_right(power=0.1)

        elif not isBallcatched:
            print("searching for ball")
            Moving.turn_right(power=0.2)

        elif isBallcatched and gateoutput is None:
            print("searching for gate")
            Moving.turn_right(power=0.1)

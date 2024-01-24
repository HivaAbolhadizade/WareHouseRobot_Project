import RPi.GPIO as GPIO
import time

# Pin numbering as needed
# ultrasonic
GPIO_TRIGGER = 19
GPIO_ECGO = 9
# driver_motor
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


# dama
# dood

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


def distance():
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)
    print("Calculating distance")

    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    while GPIO.input(GPIO_ECGO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(GPIO_ECGO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)

    print("Distance:", distance, "cm")
    return distance


sleep_time = 1


def backward(power=0.5):
    # print("on")
    # GPIO.output(F_IN2, True)
    # GPIO.output(F_IN3, True)
    GPIO.output(F_IN1, True)
    GPIO.output(F_IN4, True)
    time.sleep(power * sleep_time)
    # print("off")
    # GPIO.output(F_IN2, False)
    # GPIO.output(F_IN3, False)
    GPIO.output(F_IN1, False)
    GPIO.output(F_IN4, False)
    time.sleep(power * sleep_time)


# def testgpio(power=0.1):
#     GPIO.output(F_IN2, True)


# ________Main code________
setup_gpios()

# dis = 10
try:
    # while True:
    while True:
        backward()
    '''
    while dis >= 4:

        dis = distance()
        print(dis)
        forward()
        '''
finally:
    GPIO.cleanup()
    print("____________END of the Programm ___________")
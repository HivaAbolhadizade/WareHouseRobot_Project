import RPi.GPIO as GPIO
import time

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
# limit switches
button_pin_left = 16
button_pin_right = 20
button_pin_back = 21
# ultersonic
PIN_TRIGGER = 19
PIN_ECHO = 9

sleep_time = 1


def setup_gpios():
    GPIO.setmode(GPIO.BCM)

    # setting up driver motors
    GPIO.setup(B_IN1, GPIO.OUT)
    GPIO.setup(B_IN2, GPIO.OUT)
    GPIO.setup(B_IN3, GPIO.OUT)
    GPIO.setup(B_IN4, GPIO.OUT)
    GPIO.setup(F_IN1, GPIO.OUT)
    GPIO.setup(F_IN2, GPIO.OUT)
    GPIO.setup(F_IN3, GPIO.OUT)
    GPIO.setup(F_IN4, GPIO.OUT)
    # servo
    GPIO.setup(18, GPIO.OUT)
    # limit_switvh
    GPIO.setup(button_pin_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_pin_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_pin_back, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # ultrasonic
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)


# servo codes
def open_catcher():
    servo = GPIO.PWM(18, 50)
    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    # 12
    servo.ChangeDutyCycle(12)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()
    GPIO.cleanup()
    setup_gpios()
    time.sleep(2)


def close_catcher():
    servo = GPIO.PWM(18, 50)
    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    # 6
    servo.ChangeDutyCycle(6)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()
    GPIO.cleanup()
    setup_gpios()
    time.sleep(2)


def mid_catcher():
    servo = GPIO.PWM(18, 50)
    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    # 8
    servo.ChangeDutyCycle(8)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()
    GPIO.cleanup()
    setup_gpios()
    time.sleep(2)


# _____Functions_____

'''
def setup_servo(servo):
    # setting up servo motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    servo = GPIO.PWM(18,50)

    return servo
'''


def forward(power=0.1):
    GPIO.output(F_IN4, True)
    GPIO.output(F_IN1, True)
    GPIO.output(B_IN4, True)
    GPIO.output(B_IN1, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(F_IN1, False)
    GPIO.output(B_IN4, False)
    GPIO.output(B_IN1, False)


def backward(power=0.1):
    GPIO.output(F_IN3, True)
    GPIO.output(F_IN2, True)
    GPIO.output(B_IN3, True)
    GPIO.output(B_IN2, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN3, False)
    GPIO.output(F_IN2, False)
    GPIO.output(B_IN3, False)
    GPIO.output(B_IN2, False)


def turn_right(power=0.2):
    GPIO.output(B_IN1, True)
    GPIO.output(F_IN1, True)
    # GPIO.output(B_IN3, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN1, False)
    GPIO.output(B_IN1, False)
    # GPIO.output(B_IN3, False)


def turn_left(power=0.2):
    GPIO.output(F_IN4, True)
    GPIO.output(B_IN4, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(B_IN4, False)


def left_touch():
    # use this only for turn right movement
    if GPIO.input(button_pin_left) == GPIO.HIGH:
        print("left Micro switch pressed! Your action here.")
        # Add your custom action or function here
        turn_right(0.8)
        time.sleep(2)
        # Add a delay to avoid multiple triggers on a single press
        time.sleep(0.2)


def right_touch():
    # use this only for turn right movement
    if GPIO.input(button_pin_right) == GPIO.HIGH:
        print("right Micro switch pressed! Your action here.")
        # Add your custom action or function here
        turn_left(0.8)
        time.sleep(2)
        # Add a delay to avoid multiple triggers on a single press
        time.sleep(0.2)


def back_touch():
    # use this only for turn right movement
    if GPIO.input(button_pin_back) == GPIO.HIGH:
        print("back Micro switch pressed! Your action here.")
        # Add your custom action or function here
        forward()
        time.sleep(2)
        # Add a delay to avoid multiple triggers on a single press
        time.sleep(0.2)


# Drive_code
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


setup_gpios()
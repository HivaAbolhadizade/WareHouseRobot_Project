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

sleep_time = 1



#servo codes
def open_catcher():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    servo = GPIO.PWM(18, 50)

    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    #12
    servo.ChangeDutyCycle(12)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()
    GPIO.cleanup()

def close_catcher():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    servo = GPIO.PWM(18, 50)

    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    #6
    servo.ChangeDutyCycle(6)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()

    GPIO.cleanup()

def mid_catcher():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    servo = GPIO.PWM(18, 50)

    servo.start(0)
    print("waitng for 1sec")
    time.sleep(1)
    print("180 degrees")
    #8
    servo.ChangeDutyCycle(8)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    servo.stop()

    GPIO.cleanup()

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
    GPIO.setup(18, GPIO.OUT)

'''
def setup_servo(servo):
    # setting up servo motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    servo = GPIO.PWM(18,50)

    return servo
'''

def forward(power=0.2):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(F_IN4, GPIO.OUT)
    GPIO.setup(F_IN1, GPIO.OUT)
    GPIO.setup(B_IN4, GPIO.OUT)
    GPIO.setup(B_IN1, GPIO.OUT)

    GPIO.output(F_IN4, True)
    GPIO.output(F_IN1, True)
    GPIO.output(B_IN4, True)
    GPIO.output(B_IN1, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(F_IN1, False)
    GPIO.output(B_IN4, False)
    GPIO.output(B_IN1, False)

    GPIO.cleanup()


def backward(power=0.2):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(F_IN3, GPIO.OUT)
    GPIO.setup(F_IN2, GPIO.OUT)
    GPIO.setup(B_IN3, GPIO.OUT)
    GPIO.setup(B_IN2, GPIO.OUT)

    GPIO.output(F_IN3, True)
    GPIO.output(F_IN2, True)
    GPIO.output(B_IN3, True)
    GPIO.output(B_IN2, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN3, False)
    GPIO.output(F_IN2, False)
    GPIO.output(B_IN3, False)
    GPIO.output(B_IN2, False)

    GPIO.cleanup()


def turn_right(power=0.5):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(B_IN1, GPIO.OUT)
    GPIO.setup(F_IN1, GPIO.OUT)

    GPIO.output(B_IN1, True)
    GPIO.output(F_IN1, True)


    time.sleep(power * sleep_time)

    GPIO.output(F_IN1, False)
    GPIO.output(B_IN1, False)

    GPIO.cleanup()
def turn_left(power=0.5):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(B_IN4, GPIO.OUT)
    GPIO.setup(F_IN4, GPIO.OUT)

    GPIO.output(F_IN4, True)
    GPIO.output(B_IN4, True)

    time.sleep(power * sleep_time)

    GPIO.output(F_IN4, False)
    GPIO.output(B_IN4, False)

    GPIO.cleanup()


# Drive_code

# setup_gpios()

# try:
#     while True:
#         # setup_gpios()
#         # getting command from the user
#
#         cmd = input("Waiting for your command : ")
#
#         # moving based on that
#         if cmd == 'f':
#             forward()
#         elif cmd == 'b':
#             backward()
#         elif cmd == 'r':
#             turn_right()
#         elif cmd == 'l':
#             turn_left()
#         elif cmd == 'c':
#             close_catcher()
#         elif cmd == 'o':
#             open_catcher()
#         elif cmd == 'm':
#             mid_catcher()
#         else:
#             print("Please enter a valid command!")
#             continue
#
#         # time.sleep(sleep_time * 0.5)
#         print("_______________________________")
#         GPIO.cleanup()
#
#
# finally:
#     GPIO.cleanup()
#     print("___End of the Program___")




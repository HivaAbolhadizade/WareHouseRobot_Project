# Example Python code to handle commands
from flask import Flask

import commands as cmd


def f():
    print("forward")


def b():
    print('backward')


def r():
    print('right')


def l():
    print('left')


app = Flask(__name__)

@app.route('/<command>')
def control_robot(command):
    # Implement logic to control the robot based on the received command

    if command == 'move_forward':
        # Code to move the robot forward
        cmd.forward()
        # print('f')
    elif command == 'move_backward':
        # Code to move the robot backward
        cmd.backward()
        # print('b')
    elif command == 'move_left':
        # Code to turn the robot left
        cmd.turn_left()
        # print('l')
    elif command == 'move_right':
        # Code to turn the robot right
        # print('r')
        cmd.turn_right()
    elif command == 'catch':
        # print('c')
        cmd.close_catcher()
    elif command == 'drop':
        cmd.open_catcher()
        # print('d')

    return 'Command receive'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

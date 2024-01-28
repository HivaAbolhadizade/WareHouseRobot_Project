# Example Python code to handle commands
from flask import Flask

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
        f()
    elif command == 'move_backward':
        # Code to move the robot backward
        b()
    elif command == 'move_left':
        # Code to turn the robot left
        l()
    elif command == 'move_right':
        # Code to turn the robot right
        r()
    return 'Command receive'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

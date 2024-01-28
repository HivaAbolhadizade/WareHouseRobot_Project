# Example Python code to handle commands
from flask import Flask, Response, jsonify
from flask_cors import CORS
import commands as cmd
import Adafruit_DHT
from Box_Detection import detect_box
import cv2

def f():
    print("forward")


def b():
    print('backward')


def r():
    print('right')


def l():
    print('left')


app = Flask(__name__)
CORS(app)

camera = cv2.VideoCapture(0)  # Assuming your camera is at index 0

def generate_frames():
    uhsv = (93, 255, 199)
    lhsv = (42, 121, 39)
    erode = 0
    dilate = 5
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            img, center, size, cam_info = detect_box(frame, uhsv, lhsv, erode, dilate)
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/stream')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/humidity', methods=["GET"])
def humidity():
    humidity, temperature = Adafruit_DHT.read_retry(11, 25)

    response = {
        'status_code': 200,
        'data': {
            'humidity': str(humidity),
        }
    }

    return response

@app.route('/temperature', methods=["GET"])
def temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 25)

    response = {
        'status_code': 200,
        'data': {
            'temperature': str(temperature),
        }
    }

    return response




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

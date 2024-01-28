from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import cv2
import threading
from Ball_Detection import detect_ball

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
            img, center, radius, cam_info = detect_ball(frame, uhsv, lhsv, erode, dilate)
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/stream')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/<command>')
def control_robot(command):
    if command == 'move_forward':
        # Code to move the robot forward
        print("forward")
    elif command == 'move_backward':
        # Code to move the robot backward
        print('backward')
    elif command == 'move_left':
        # Code to turn the robot left
        print('left')
    elif command == 'move_right':
        # Code to turn the robot right
        print('right')
    return 'Command received'


# @app.route('/temperature', methods=['GET'])
# def temp():
#     text = "3"
#     return Response(text, status=200, mimetype='text/plain')

@app.route('/temperature', methods=['GET'])
def temp():
    temp = '3'

    response = {
        'status_code': 200,
        'data': {
            'temperature': temp,
        }
    }

    return jsonify(response)

@app.route('/humidity', methods=['GET'])
def hue():
    temp = '12'

    response = {
        'status_code': 200,
        'data': {
            'humidity': temp,
        }
    }

    return jsonify(response)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000}).start()

from flask import Flask, render_template, Response
import cv2
import threading
from Ball_Detection import detect_ball
app = Flask(__name__)
camera = cv2.VideoCapture(1)  # Assuming your camera is at index 0

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<command>')
def control_robot(command):
    if command == 'forward':
        # Code to move the robot forward
        print("forward")
    elif command == 'backward':
        # Code to move the robot backward
        print('backward')
    elif command == 'left':
        # Code to turn the robot left
        print('left')
    elif command == 'right':
        # Code to turn the robot right
        print('right')
    return 'Command received'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000}).start()

from flask import Flask, send_file
from io import BytesIO
import cv2
import time

app = Flask(__name__)
camera = cv2.VideoCapture(1)


@app.route('/stream')
def stream():
    # Capture image from OpenCV camera
    ret, frame = camera.read()

    # Convert the image to JPEG format
    success, img_encoded = cv2.imencode('.jpg', frame)
    if not success:
        return



    key = cv2.waitKey(0)
    if key == 'q':
        return

    # Create BytesIO object and write the encoded image
    img_stream = BytesIO(img_encoded.tobytes())

    # Move the cursor to the beginning of the stream
    img_stream.seek(0)

    # Return the image as an HTTP response with MIME type 'image/jpeg'
    return send_file(img_stream, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import cv2
import numpy as np

camera = cv2.VideoCapture(1)

while True:
    success, frame = camera.read()
    if success is False:
        break
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 60, 120)  # Typical ratio  : 1:2, 1:3, start with 50, 150
        # # cv2.imshow("edges", edges)
        # key = cv2.waitKey(1)
        # if key == 'q':
        #     break

        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            vertices = len(approx)
            if vertices == 3:
                shape = "Triangle"
            elif vertices == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                ar = w / float(h)
                # A square will have an aspect ratio(ar) that is approximately
                # equal to one, otherwise, the shape is a rectangle
                shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
            elif vertices == 5:
                shape = "Pentagon"
            else:
                shape = "Circle"
            cv2.putText(frame, shape, (approx[0][0][0], approx[0][0][1] + 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("VideoStream", frame)



camera.release()
cv2.destroyAllWindows()

import cv2

cam = cv2.VideoCapture(1)
ret, image = cam.read()

# while True:
# 	ret, image = cam.read()
# 	# cv2.imshow('Imagetest',image)
# 	k = cv2.waitKey(1)
# 	if k != -1:
# 		break
cv2.imwrite(r'/home/ca2023/Desktop/appleball.jpg', image)
cam.release()
print("picture saved")
# cv2.destroyAllWindows()
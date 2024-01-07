import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

"""
    this is a good example to illustrate what is a contours
"""

# Create a binary image with two circular objects
mask = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(mask, (100, 100), 50, 255, -1)  # Circle 1
cv2.circle(mask, (200, 200), 40, 255, -1)  # Circle 2

# Find contours
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print(len(cnts))
# Draw contours on a copy of the original image
output = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)
cv2.drawContours(output, cnts, -1, (0, 255, 0), 2)

# Display the original image and the image with contours
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title('Image with Contours')
plt.axis('off')

plt.show()

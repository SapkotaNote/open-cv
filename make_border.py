import cv2  # Import OpenCV library for image processing
import numpy as np  # Import NumPy (used for handling arrays, though not directly used here)

# Read the image from the specified full file path
img = cv2.imread(r'C:\\Users\\RADHE RADHE\\Desktop\\New folder\\jupyter\\open-cv\\openc2\\img_1.png')

# Resize the image to 500x500 pixels for consistency
img = cv2.resize(img, (500, 500))

# Add a border around the image
# Parameters: image, top, bottom, left, right, border type, optional argument (unused here), color value
img_1 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, value=2)
# 20,20,20,20 → Adds 20 pixels border on all sides (top, bottom, left, right)
# BORDER_CONSTANT → Adds a constant color border
# value=2 → Color of the border; since image is in color, 2 means dark bluish (BGR: (2,2,2))

# Display the final image with border
cv2.imshow('img', img_1)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

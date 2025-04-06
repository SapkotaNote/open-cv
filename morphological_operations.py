import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations

# Load the image
img = cv2.imread(r'C:\\Users\\RADHE RADHE\\Desktop\\New folder\\jupyter\\open-cv\\openc2\\img_1.png')

# Resize the image to 200x200 pixels
img = cv2.resize(img, (200, 200))

# Create a kernel (structuring element) of size 5x5 with all ones
m = np.ones((5, 5), np.uint8)

# Apply erosion (shrinks white regions)
er = cv2.erode(img, m, iterations=1)

# Apply dilation (expands white regions)
di = cv2.dilate(img, m, iterations=1)

# Apply opening (erosion followed by dilation) - removes small noise
op = cv2.morphologyEx(img, cv2.MORPH_OPEN, m, iterations=1)

# Apply closing (dilation followed by erosion) - fills small holes
cl = cv2.morphologyEx(img, cv2.MORPH_CLOSE, m, iterations=1)

# Morphological gradient (difference between dilation and erosion)
gred = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, m, iterations=1)

# Top hat (difference between input image and its opening)
top = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, m, iterations=1)

# Black hat (difference between closing and input image)
black_hate = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, m, iterations=1)

# Stack images horizontally (excluding kernel `m` since it's not an image)
h = np.hstack((img, er, di, op, cl, gred, top, black_hate))

# Display the stacked result
cv2.imshow('Morphological Operations', h)
cv2.waitKey(0)
cv2.destroyAllWindows()

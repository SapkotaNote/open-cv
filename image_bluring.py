import cv2
import numpy as np

img = cv2.imread('img_2.jfif')
re_img = cv2.resize(img, (500,500))

# 1. Apply Gaussian Blur
# Smooths the image using a Gaussian kernel; good for general blurring
y = cv2.GaussianBlur(re_img, (9, 7), sigmaX=0)

# 2. Apply Median Blur
# Replaces each pixel with the median of surrounding pixels; great for salt-and-pepper noise
m = cv2.medianBlur(re_img, 3)

# 3. Apply Bilateral Filter
# Smooths the image while keeping edges sharp; ideal for edge-preserving smoothing
b = cv2.bilateralFilter(re_img, d=9, sigmaColor=75, sigmaSpace=75)

# 4. Stack all images horizontally: original, Gaussian, median, bilateral
# Make sure all images are the same size and type
combined = np.hstack((re_img, y, m, b))

cv2.imshow('GaussianBlur',combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
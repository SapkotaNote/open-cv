import cv2
# Step 1: Load the image from a file
# Make sure the image path is correct
img = cv2.imread('img_2.jfif')

# Step 3: Apply Canny edge detection
# threshold1 = lower threshold
# threshold2 = upper threshold
# apertureSize = size of the Sobel kernel used for gradient calculation (must be 3, 5, or 7)
# L2gradient=True means we use a more accurate calculation of the edge magnitude (sqrt(dx^2 + dy^2))
edges = cv2.Canny(img, threshold1=50, threshold2=150, apertureSize=3, L2gradient=True)

# Step 4: Display the original image
cv2.imshow("Original Image", img)

# Step 5: Display the edges detected by the Canny algorithm
cv2.imshow("Edges", edges)

# Step 6: Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
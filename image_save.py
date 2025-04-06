import cv2

img = cv2.imread(r'C:\\Users\\RADHE RADHE\Desktop\\New folder\\jupyter\\open-cv\\openc2\\img_1.png')
img_1 = cv2.resize(img, (500,500))
cv2.imwrite(r'C:\\Users\\RADHE RADHE\Desktop\\New folder\\jupyter\\open-cv\\openc2\\New_img.jpg', img_1)
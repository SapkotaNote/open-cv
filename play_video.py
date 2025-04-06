import cv2
cap = cv2.VideoCapture('video_1.mp4')
while True:
    r,frame = cap.read()
    if r==True:
        frame=cv2.resize(frame,(500,500))
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
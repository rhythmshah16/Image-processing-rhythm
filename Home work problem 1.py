import cv2

cap = cv2.VideoCapture(0)

while True:
    x,frame = cap.read()

    frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow('image',frame)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break
import cv2
import time
cap = cv2.VideoCapture(0)
counter = 0

while True:
    x,frame = cap.read()
    counter +=1
    flipped = cv2.flip(frame,-1)

    if counter %4 == 0:
        cv2.imshow('img',flipped)
    else:
         cv2.imshow('img',frame)

    if counter == 13:
        print('3 cycles succesfully completed')
        cap.release()
        cv2.destroyAllWindows()
       

    if cv2.waitKey(1500) & 0xff == ord('q'):
        break

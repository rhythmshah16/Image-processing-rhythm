import cv2

cap = cv2.VideoCapture(0)

counter = 0

val = int(input('enter a number'))

while True:
    x,frame = cap.read()
    counter +=1
    if counter %val == 0:
        flipped = cv2.flip(frame,-1)
        cv2.imshow('image',flipped)

    else:
        cv2.imshow('image',frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
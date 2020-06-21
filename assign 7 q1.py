
import cv2
import numpy as np 

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Frame')
cv2.createTrackbar('H','Frame',0,180,nothing)
cv2.createTrackbar('S','Frame',0,255,nothing)
cv2.createTrackbar('V','Frame',0,255,nothing)

while True:
    x,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('H','Frame')
    s = cv2.getTrackbarPos('S','Frame')
    v = cv2.getTrackbarPos('V','Frame')

    lower_bound = np.array([h,s,v])
    upper_bound = np.array([180,255,255])

    mask_final= cv2.inRange(hsv,lower_bound,upper_bound)
    res = cv2.bitwise_and(frame,frame,mask=mask_final)

    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask_final)
    cv2.imshow('Output',res)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
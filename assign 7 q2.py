import cv2
import numpy as np



frame=cv2.imread('paper.jpg')

width = int(frame.shape[1] / 3)
height = int(frame.shape[0] / 3)
dim = (width, height)
size_change = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
hsv=cv2.cvtColor(size_change,cv2.COLOR_BGR2HSV)
cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.namedWindow('transformed',cv2.WINDOW_NORMAL)
lower_bound=np.array([8,2,111])
upper_bound=np.array([85,48,247])

maskfinal= cv2.inRange(hsv,lower_bound,upper_bound)

res=cv2.bitwise_and(size_change,size_change,mask=maskfinal)

contours_searched,hierarchy=cv2.findContours(maskfinal,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

areas=[cv2.contourArea(c) for c in contours_searched]

max_index=np.argmax(areas)

max_contour=contours_searched[max_index]

x,y,w,h=cv2.boundingRect(max_contour)

perimeter=cv2.arcLength(max_contour,True)

ROI=cv2.approxPolyDP(max_contour,0.01*perimeter,True)

arr1=np.array([ROI[1],ROI[0],ROI[2],ROI[3]],np.float32)
arr2=np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)

perspective = cv2.getPerspectiveTransform(arr1,arr2)
transformed = cv2.warpPerspective(size_change,perspective,(500,500))

cv2.drawContours(size_change,[ROI],-1,(255,0,0),15)

cv2.imshow('original',size_change)
cv2.imshow('Transformed',transformed)
cv2.waitKey(0)
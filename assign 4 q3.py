import cv2
import numpy as np 
img = cv2.imread('B99.JPG')
def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)
pt_1 = np.array([[1137,139],[1413,136],[1415,641],[1135,639]],np.float32)
pt_2 = np.array([[0,0],[500,0],[500,600],[0,600]],np.float32)
perspective_img = cv2.getPerspectiveTransform(pt_1,pt_2)
wrapped_img = cv2.warpPerspective(img,perspective_img,(500,600))
cv2.imshow('frame',img)
cv2.imshow('wrapped',wrapped_img)
cv2.waitKey(0)
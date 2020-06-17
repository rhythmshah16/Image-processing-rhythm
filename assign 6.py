import cv2
import numpy as np 

while True:
    img = cv2.imread('B99.jpg')
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5))
    erode = cv2.erode(img_gray,kernel)
    dilate = cv2.dilate(img_gray,kernel)
    closing = cv2.morphologyEx(img_gray,cv2.MORPH_CLOSE,kernel)
    canny = cv2.Canny(img_gray,60,255)
    cv2.imshow('image',img)
    cv2.imshow('edge',canny)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()

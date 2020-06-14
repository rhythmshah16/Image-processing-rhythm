import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
i = False
j = False

def mouse(event,x,y,flags,param):
    global pts,i,j
    if event == cv2.EVENT_LBUTTONDOWN:
        if i == False:
            pts = [(x,y)]
            i = True
        elif j== False:
            pts.append((x,y))
            j = True
        if len(pts) == 2:
            ay,by,cy,dy = pts[0][1],pts[1][1],pts[0][0],pts[1][0]
            cropped= frame[ay:by,cy:dy]
            cv2 .imwrite('template img.jpg',cropped)

            
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)
while True:
    x,frame = cap.read()
    template = cv2 .imread('template img.jpg')
    if i== True  and j==True:
        cv2 .imshow('template',template)
        template_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        w = template_gray.shape[1]
        h = template_gray.shape[0]
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res=cv2.matchTemplate(frame_gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc=np.where(res>=0.8)
        for x,y in zip(*loc[::-1]):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(frame,'object',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

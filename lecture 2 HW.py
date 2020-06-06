import cv2
img = cv2.imread('B99.jpg')
print(img.shape)
x = int(input('enter the first number that is displayed'))
y = int(input('enter the second number that is dispalyed'))

cv2.line(img,(0,0),(x,y),(0,0,255),4)

cv2.imshow('image',img)

cv2.waitKey(0)
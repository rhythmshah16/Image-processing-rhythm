import cv2
cap = cv2.VideoCapture(0)

counter = 0

while True:
    x,frame = cap.read()
    cv2.imshow('image',frame)


    img_name = "img_{}.jpg".format(counter)
    cv2.imwrite(img_name, frame)

    counter += 1

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
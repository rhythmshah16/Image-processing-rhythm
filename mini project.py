import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk
import pytesseract
from pytesseract import Output
import os
import cv2
import numpy as np

root = tk.Tk()
og_img=np.zeros((),np.uint8)
pts=[]

# function #
def open_button_clicked():
	global og_img
	filename=filedialog.askopenfilename(initialdir='/users/desktop/',title='select an image',filetypes =(('JPG','*jpg'),('all files','*.*')))
	og_img=cv2.imread(filename)
	cv2.imshow('Image',og_img)
	cv2.waitKey(0)

def mouse(event,x,y,flags,param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append(x)
        pts.append(y)

def manualcrop_button_clicked():
    global cropped
    while True:
        img=np.copy(og_img)
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image",mouse)
        cv2.imshow("Image",img)
        if len(pts)==4:
            cropped=img[pts[1]:pts[3],pts[0]:pts[2]]
            cv2.imshow("Cropped",cropped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
	
def blur_button_clicked():
	img=np.copy(og_img)
	global gaussianblur
	img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gaussianblur=cv2.GaussianBlur(img_gray,(25,25),2)
	cv2.imshow('Image',gaussianblur)

def ocr_button_clicked():
    global img1
    img1=np.copy(og_img)

    data=pytesseract.image_to_data(img1,output_type=Output.DICT)
    no_word=len(data['text'])
    for i in range(no_word):
        if int(data['conf'][i])>50:
            x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
            
            cv2.imshow('img',img1)
            cv2.waitKey(100)

def autocrop_button_clicked():
    global transformed
    img = np.copy(og_img)
    ratio = img.shape[1]/img.shape[0]
	height = int (1100/ratio)
    TransformedImage = cv2.resize(img,(1100,height))
    img_gray = cv2.cvtColor(TransformedImage,cv2.COLOR_BGR2GRAY)
    adaptive = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,55,3)
    canny = cv2.Canny(adaptive,150,250)

    contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area = [cv2.contourArea(x) for x in contours]
    max_index = np.argmax(area)
    max_contour = contours[max_index]
    perimeter = cv2.arcLength(max_contour,True)
    region = cv2.approxPolyDP(max_contour,0.01*perimeter,True)


    if len(region) == 4:
        cv2.drawContours(TransformedImage,[region],-1,(255,0,0),10)
        lst = [region[0],region[3],region[1],region[2]]
        pt1 = np.array(lst,np.float32)
        pt2 = np.array([(0, 0), (600, 0), (0, 600), (600, 600)],np.float32)

        perspective = cv2.getPerspectiveTransform(pt1,pt2)
        transformed = cv2.warpPerspective(TransformedImage, perspective, (600,600))    

        cv2.imshow('Warped Image',transformed)
        cv2.waitKey(0)

def show_text_button_clicked():
    textbox = tk.Frame(frame,bg='#FDFFD6')
    textbox.place(x=300,y=300)

    text =Text(textbox,bg='#FDFFD6')
    text.insert('1.0',"text box works!!")
    text.pack()


canvas=tk.Canvas(root,height=800,width=800,bg='green')
canvas.pack()
Frame =tk.Frame(canvas,bg='white')
Frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

#buttons#	


open_button=tk.Button(Frame,text='open button',bg='blue',padx=8,pady=8,command=open_button_clicked)
open_button.pack()
open_button.place(x=2,y=50)

manualcrop_button=tk.Button(Frame,text='manual crop',bg='blue',padx=8,pady=8,command=manualcrop_button_clicked)
manualcrop_button.pack()
manualcrop_button.place(x=2,y=210)

blur_button=tk.Button(Frame,text='blur',bg='blue',padx=8,pady=8,command=blur_button_clicked)
blur_button.pack()
blur_button.place(x=2,y=130)

ocr_button=tk.Button(Frame,text='ocr',bg='blue',padx=8,pady=8,command=ocr_button_clicked)
ocr_button.pack()
ocr_button.place(x=600,y=50)

autocrop_button=tk.Button(Frame,text='auto crop',bg='blue',padx=8,pady=8,command=auto_button_clicked)
autocrop_button.pack()
autocrop_button.place(x=600,y=130)

text_button =tk.Button(Frame,text='show text',bg='blue',padx=8,pady=8,command=show_text_button_clicked)
text_button.pack()
text_button.place(x=600,y=210)
root.mainloop()
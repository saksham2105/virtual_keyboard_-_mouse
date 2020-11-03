import cv2 as cv 
import numpy as np 
import imutils
import json
import pyautogui
import time
cam = cv.VideoCapture(0)
arr=[]
nums=["1","2","3","4","5","6","7","8","9","0"]
row1=["Q","W","E","R","T","Y","U","I","O","P"]
row2=["A","S","D","F","G","H","J","K","L"]
row3=["Z","X","C","V","B","N","M"]
row4=["space","enter","backspace","shift"]
row5=["left","up","down","right"]
row6=["volumeup","volumedown","volumemute"]
x=10
y=20
for i in range(0,10):
    data={}
    data["x"]=x
    data["y"]=y
    data["w"]=100
    data["h"]=80
    data["value"]=nums[i]
    arr.append(data)
    x=x+100
y=100
x=10
for i in range(0,10):
    data={}
    data["x"]=x
    data["y"]=y
    data["w"]=100
    data["h"]=80
    data["value"]=row1[i]
    arr.append(data)
    x=x+100
x=110
y=180
for i in range(0,9):
    data={}
    data["x"]=x
    data["y"]=y
    data["w"]=100
    data["h"]=80
    data["value"]=row2[i]
    arr.append(data)
    x=x+100
x=210
y=260
for i in range(0,7):
    data={}
    data["x"]=x
    data["y"]=y
    data["w"]=100
    data["h"]=80
    data["value"]=row3[i]
    arr.append(data)
    x=x+100
x=110
y=340
data={}
data["x"]=x
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row4[0]
arr.append(data)
data={}
data["x"]=310
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row4[1]
arr.append(data)
data={}
data["x"]=510
data["y"]=340
data["w"]=250
data["h"]=80
data["value"]=row4[2]
arr.append(data)
data={}
data["x"]=760
data["y"]=340
data["w"]=200
data["h"]=80
data["value"]=row4[3]
arr.append(data)
x=110
y=420
data={}
data["x"]=x
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row5[0]
arr.append(data)
data={}
data["x"]=310
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row5[1]
arr.append(data)
data={}
data["x"]=510
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row5[2]
arr.append(data)
data={}
data["x"]=710
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row5[3]
arr.append(data)
x=10
y=500
data={}
data["x"]=x
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row6[0]
arr.append(data)
data={}
data["x"]=210
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row6[1]
arr.append(data)
data={}
data["x"]=410
data["y"]=y
data["w"]=200
data["h"]=80
data["value"]=row6[2]
arr.append(data)

json_string=json.dumps(arr)
json_data=json.loads(json_string)
#print(json_data)
while(1):
    ret,img = cam.read()
    img = cv.GaussianBlur(img,(5,5),0)
    img=imutils.resize(img,width=1030,height=700)
    height,width=img.shape[:2]
    x=10
    y=20
    for i in range(0,10):
        cv.rectangle(img,(x,y),(x+100,y+80),(0,255,255),2)
        cv.putText(img,nums[i],(x+50,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
        x=x+100
    y=100
    x=10
    for i in range(0,10):
        cv.rectangle(img,(x,y),(x+100,y+80),(0,255,255),2)
        cv.putText(img,row1[i],(x+50,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
        x=x+100
    x=110
    y=180
    for i in range(0,9):
        cv.rectangle(img,(x,y),(x+100,y+80),(0,255,255),2)
        cv.putText(img,row2[i],(x+50,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
        x=x+100
   
    x=210
    y=260
    for i in range(0,7):
        cv.rectangle(img,(x,y),(x+100,y+80),(0,255,255),2)
        cv.putText(img,row3[i],(x+50,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
        x=x+100
    x=110
    y=340
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row4[0],(x+70,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=310
    y=340
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row4[1],(x+70,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=510
    y=340
    cv.rectangle(img,(x,y),(x+250,y+80),(0,255,255),2)
    cv.putText(img,row4[2],(x+70,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=760
    y=340
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row4[3],(x+70,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=110
    y=420
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row5[0],(x+100,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=310
    y=420
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row5[1],(x+100,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=510
    y=420
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row5[2],(x+100,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=710
    y=420
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,row5[3],(x+100,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=10
    y=500
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,"V+",(x+60,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=210
    y=500
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,"V-",(x+60,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)
    x=410
    y=500
    cv.rectangle(img,(x,y),(x+200,y+80),(0,255,255),2)
    cv.putText(img,"Vmute",(x+60,y+40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA,False)

    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_img,np.array([65,60,60]),np.array([80,255,255]))
    mask_open = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((5,5)))
    mask_close = cv.morphologyEx(mask_open,cv.MORPH_CLOSE,np.ones((20,20)))
    mask_final = mask_close
    conts,_ = cv.findContours(mask_final.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(img,conts,-1,(255,0,0),3)
    if(len(conts)==1):
        x,y,w,h = cv.boundingRect(conts[0])
        cx = round(x+w/2)
        cy = round(y+h/2)
        cv.circle(img,(cx,cy),20,(0,0,255),2)
        word=""
        for i in range(len(json_data)):
            if cx>=int(json_data[i]["x"]) and cx<=int(json_data[i]["x"])+int(json_data[i]["w"]) and cy>=int(json_data[i]["y"]) and cy<=int(json_data[i]["y"])+int(json_data[i]["h"]):
                word=json_data[i]["value"]
        #print(word)
        pyautogui.press(word)
        #pyautogui.PAUSE=2.5
        #time.sleep(1)

    cv.imshow("cam",img)
    cv.waitKey(10)
    
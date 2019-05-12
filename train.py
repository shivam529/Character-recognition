import cv2
from PIL import Image
import numpy as np
import math
import sys
from scipy import misc
from scipy import fftpack,ndimage
import cv2
from copy import deepcopy



    



temp_image=cv2.imread("training_chars.png")


gray = cv2.cvtColor(temp_image, cv2.COLOR_BGR2GRAY)
temp=deepcopy(gray)
binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 5, 2)



contours, _ = cv2.findContours(image=binary,
                               mode=cv2.RETR_EXTERNAL,
                               method=cv2.CHAIN_APPROX_SIMPLE)

rects=[]
for cnt in contours:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    
    if w >= 5 and (h >= 25 and h <= 50):
        rects.append((x,y,w,h))
        
rects=sorted(rects,key=lambda x:x[1])
ctr=200
for (x,y,w,h) in rects:
    ctr+=1
    print(x,y)
    cv2.rectangle(temp_image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("b",temp_image)
    cv2.waitKey(400)
    check=temp[y-2:y+h+2,x-2:x+w+2]
    check=cv2.resize(check,(30,30))
    check=cv2.adaptiveThreshold(check,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,11,2)
    check_invert=cv2.adaptiveThreshold(check,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,11,2)

    M1= cv2.moments(check_invert)
    cx1= int(M1['m10']/M1['m00'])
    cy1 = int(M1['m01']/M1['m00'])
    print(cx1,cy1)
    rows,cols =check.shape
    tx=15-cx1
    ty=15-cy1
    M = np.float32([[1,0,tx],[0,1,ty]])
    dstt = cv2.warpAffine(check,M,(cols,rows),borderMode=cv2.BORDER_CONSTANT, 
    borderValue=255)

    cv2.imshow("c",check)
    cv2.imshow("centered",dstt)
    cv2.imwrite("image"+str(ctr)+".png",check)
    cv2.waitKey(400)

cv2.waitKey()

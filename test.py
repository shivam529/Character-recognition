
import numpy as np
import sys
import cv2
from copy import deepcopy
import label_image as classify


## Image to be Detected

temp_image=cv2.imread("test2.png")

## Image Gray_Scaled

gray = cv2.cvtColor(temp_image, cv2.COLOR_BGR2GRAY)

## Keeping a copy to be later used

temp=deepcopy(gray)

## binary image

binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 5, 2)




## Finding comtours for enclosing digits

contours, _ = cv2.findContours(image=binary,
                               mode=cv2.RETR_EXTERNAL,
                               method=cv2.CHAIN_APPROX_SIMPLE)
## Finding enclosing rectangles for all the Digits

rects=[]
for cnt in contours:
   
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    
    if w >= 5 and (h >= 25 and h <= 40):
        rects.append((x,y,w,h))
        
rects=sorted(rects,key=lambda x:x[1])
for (x,y,w,h) in rects:
    cv2.rectangle(temp_image,(x,y),(x+w,y+h),(0,255,0),2)
    
    check=temp[y-4:y+h+4,x-4:x+w+4]
    ## resizing image to standard as in training images( size 30 x30 and number centered in the 30x30 box)
    
    check=cv2.resize(check,(30,30))
    check=cv2.adaptiveThreshold(check,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,11,2)
    check_invert=cv2.adaptiveThreshold(check,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,11,2)
    ## Finding center of mass of each digit image and Centering them "dstt" is the final digit image after all the processing to be classified
    
    M1= cv2.moments(check_invert)
    cx1= int(M1['m10']/M1['m00'])
    cy1 = int(M1['m01']/M1['m00'])
    rows,cols =check.shape
    tx=15-cx1
    ty=15-cy1
    M = np.float32([[1,0,tx],[0,1,ty]])
    dstt = cv2.warpAffine(check,M,(cols,rows),borderMode=cv2.BORDER_CONSTANT, 
    borderValue=255)

    ## the image required by tensorflow is in bytes,hence the conversion below
    
    success, encoded_image = cv2.imencode('.png', dstt)
    content2 = encoded_image.tobytes()
    label_retrieved,lab=classify.get(content2)
    cv2.putText(temp_image,str(label_retrieved), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),thickness=1)
    cv2.imshow("test_image",temp_image)
    cv2.waitKey(400)
    cv2.imwrite("test2_results.png",temp_image)
   




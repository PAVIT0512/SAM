from ultralytics import YOLO
import cv2 
import math
import numpy as np


def boxdetection(frame):
    model = YOLO("./Coordinate/best files/best.pt")
    results = model.predict(frame)
    result = results[0]
    min_dist = 1406
    x,y,x_,y_=0,0,0,0
    output=[]
    for box in result.boxes:
        x1, y1, x2, y2 = [
            round(x) for x in box.xyxy[0].tolist()
        ]
        if y1>44:
            center=[int((x1+x2)/2),int((y1+y2)/2)]
            if (x2-x1)>100 or (y2-y1)>100:
                # cv2.rectangle(frame,(x1, y1),(x2,y2),(0,0,255),2)
                # cv2.putText(frame,str(center),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
                if center[0]+center[1]<min_dist:
                    min_dist=center[0]+center[1] 
                    x,y,x_,y_=x1,y1,x2,y2

    # cv2.putText(frame, str(line), (x_, y_), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 255, 255), 2, cv2.LINE_4) 
    image=frame[y:y_,x:x_]
    cv2.rectangle(frame,(x,y),(x_,y_),(0,255,0),2) 
    cv2.imshow('Image',frame)
    cv2.destroyAllWindows()
    center=[int((x+x_)/2),int((y+y_)/2)]
    return center


# image=cv2.imread('00004.png')
# print(boxdetection(image))
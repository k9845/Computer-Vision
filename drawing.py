import cv2
import numpy as np


framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)

mycolors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 19, 156, 255],
            [57, 76, 0, 100, 255, 255],
            []]

mycolorvalue =[[51,153, 255],    ###BGR
               [255, 0, 255],
               [0, 255, 0]]

mypoints = []  ##[x, y, colorid]


def findColour(img, mycolors):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for colors in mycolors:
        lower = np.array(colors[0:3])
        upper = np.array(colors[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        x, y = getContour(mask)
        cv2.circle(imgResult, (x,y), 10, mycolorvalue[count], cv2.FILLED)
        if x !=0 and y != 0:
            newpoints.append([x,y,count])
        count += 1
        #cv2.imshow(str(colors[0]), mask)
    return newpoints

def getContour(img):
    contours, hierarchy = cv2.findContours(
        img, 
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )
    x, y, w, h =  0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(mypoints, mycolorvalue):
    for point in mypoints:
        cv2.circle(imgResult, 
                    (point[0], point[1]), 
                    10, 
                    mycolorvalue[point[2]], 
                    cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoint = findColour(img, mycolors, mycolorvalue)
    if len(newpoint) != 0:
        for newp in newpoint:
            mypoints.append(newp)
            drawOnCanvas(mypoints, mycolorvalue)      
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

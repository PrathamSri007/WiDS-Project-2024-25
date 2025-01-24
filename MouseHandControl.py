import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import mouse
from win32api import GetSystemMetrics

screen_width =GetSystemMetrics(0)   # used to get screen width of system
screen_height = GetSystemMetrics(1) # used to get screen height of system

def indexUp():
    if landmarkList[8][2] < landmarkList[6][2] :
        return True # returns true is index finger is help up
    return False

def middleUp():
    if landmarkList[12][2] < landmarkList[10][2] :
        return True # returns true is middle finger is help up
    return False

cap = cv2.VideoCapture(0)

frame_width = 640
frame_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
# cap.set(cv2.CAP_PROP_FPS, 30)


pTime = 0
detector = htm.handDetector(max_hands=1, detectionCon=0.8, trackCon=0.6)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    landmarkList = detector.findPosition(img, draw=False)

    if(len(landmarkList) != 0):
        x1, y1 = landmarkList[8][1], landmarkList[8][2]
        x2, y2 = landmarkList[12][1], landmarkList[12][2]
        
        cv2.circle(img, (x1,y1), 10, (0, 0, 255), cv2.FILLED)

        # get the current location of your mouse
        position = mouse.get_position()
        mouse_x, mouse_y = position[0], position[1]

        # new mouse positions as per index finger location
        newpos_x = screen_width - screen_width/frame_width * x1 
        newpos_y = screen_height/frame_height * y1

        if indexUp():
            print('UP', landmarkList[8][2], landmarkList[6][2])
            mouse.drag(mouse_x, mouse_y, newpos_x, newpos_y, absolute=True, duration=0.1) # drags the cursor
        
        if indexUp() and middleUp():
            cv2.circle(img, (x2,y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 3)
            length = math.hypot(x1-x2, y1-y2)

            #click
            if length < 20 :
                mouse.click('left') # imitates left mouse click when index and middle fingers touch being held up
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    img = cv2.flip(img,1)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3) 
        
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
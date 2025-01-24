import cv2
import time
import numpy as np
import HandTrackingModule as htm # HandTrackingModule imported
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #using pycaw library (Credits: AndreMiras)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
volBar = 400


cap = cv2.VideoCapture(0)

# sets camera frame dimensions
frame_width = 640
frame_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
# cap.set(cv2.CAP_PROP_FPS, 30)


pTime = 0
detector = htm.handDetector(max_hands=1)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    landmarkList = detector.findPosition(img, draw=False)

    if(len(landmarkList) != 0):
        x1, y1 = landmarkList[4][1], landmarkList[4][2] # returns position for thumb tip
        x2, y2 = landmarkList[8][1], landmarkList[8][2] # returns position for index tip
        
        cv2.circle(img, (x1,y1), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 3)

        length = math.hypot(x1-x2, y1-y2) # calculating distance between thumb and index tip
        
        vol = np.interp(length, [50, 200], [minVol, maxVol]) # scaling volume acording to length
        volBar = np.interp(length, [50, 200], [150, 400]) # scaling the displayed volume bar according to the length
        volume.SetMasterVolumeLevel(vol, None) # sets system master volume to vol

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 255), 3)
    cv2.rectangle(img, (50, 550-int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED) #volume bar displayed


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    img = cv2.flip(img,1) # flips image to show selfie view
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3) #fps displayed
        
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows() #closes additional windows opened
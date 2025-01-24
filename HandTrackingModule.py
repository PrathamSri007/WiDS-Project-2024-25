### This is the Hand Tracking Module that I created for implementation of CV in this project ### 

import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, max_hands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands                              
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, 1, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    # locating hands in the image or the frame of a video stream
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img)
        if results.multi_hand_landmarks:
            for handLdmrks in results.multi_hand_landmarks:
                if draw: # draws the connecting lines between the 21 hand landmarks
                    self.mpDraw.draw_landmarks(img, handLdmrks, self.mpHands.HAND_CONNECTIONS)
        return img                    
    
    # function to return the location (in pixels) of the hand landmarks identified
    def findPosition(self, img, handNo=0, draw=True):
        ldmrkList = []
        results = self.hands.process(img)
        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[handNo]
            for id, ldmrk in enumerate(myHand.landmark):
                h, w, _ = img.shape
                cx, cy = int(ldmrk.x*w), int(ldmrk.y*h)
                ldmrkList.append([id,cx,cy])
                if (id == 8 and draw): #index finger tip
                    cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)
        return ldmrkList


def main():
    pTime = 0
    cTime = 0

    # using webcam for inputting video stream
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        ldmrkList = detector.findPosition(img)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3) 
        
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == 27: #exit if the Esc key is pressed 
            break


# main is called if the module is directly executed
if __name__ == "__main__":
    main()
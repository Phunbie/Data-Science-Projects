# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 05:43:21 2022

@author: FBI
"""

import cv2
import mediapipe as mp
import pyautogui as pa
import time
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.1)
mpDraw = mp.solutions.drawing_utils

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        hand_lm_list = []
        for handLms in results.multi_hand_landmarks:
            for ide,lm in enumerate(handLms.landmark):
                #print(ide,lm)
                h,w,c =img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                hand_lm_list.append(cx)
            
                
                    #print(ide,cx,cy)
                
               # if ide == 4:
                   # cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            #mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            position= hand_lm_list[0]-hand_lm_list[4]
            if position < -80:
                pa.keyDown('left')
                time.sleep(3)
                pa.keyUp("left")
            elif position > 60:
                pa.keyDown('right')
                time.sleep(3)
                pa.keyUp("right")
            else:
                print('normal')
                
            
    #cv2.imshow('image',img)
    cv2.waitKey(1)
                
    
    
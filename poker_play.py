# -*- coding: utf-8 -*-
import numpy as np 
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
import cv2
import imutils
from shapedetector import ShapeDetector


printscreen_pil = ImageGrab.grab(bbox=(0,40,800,640))
printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
cv2.imshow('window',printscreen_numpy)
clone = printscreen_numpy


#verificar cartas da mão
roi = clone[320:400,280:380]
cv2.imshow('ROI',roi)
cv2.waitKey(0)

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",gray)
cv2.waitKey(0)


thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Image",thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


for c in cnts:
    bb = cv2.boundingRect(c)
    
    if bb[2]>20:
        #c = c.astype("float")
        #c = c.astype("int")
        #cv2.drawContours(roi, [c], -1, (0,255,0),2)
        

        #cv2.imshow("Image",roi)
        
        card = roi[bb[1]:bb[1]+bb[3],bb[0]:bb[0]+bb[2]]
        cv2.imshow("card",card)

        #aqui podemos rodar o modelo e adicionar em uma lista de cartas da mão

        cv2.waitKey(0)


#verificar cartas do flop
flop = clone[200:300,180:380]
cv2.imshow('Flop',flop)
cv2.waitKey(0)

gray_flop = cv2.cvtColor(flop, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image_gray_flop",gray_flop)
cv2.waitKey(0)


thresh_flop = cv2.threshold(gray_flop, 180, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Image_flop",thresh_flop)
cv2.waitKey(0)

cnts_flop = cv2.findContours(thresh_flop.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_flop = imutils.grab_contours(cnts_flop)


for c in cnts_flop:
    bb = cv2.boundingRect(c)
    
    if bb[2]>20:
        #c = c.astype("float")
        #c = c.astype("int")
        #cv2.drawContours(flop, [c], -1, (0,255,0),2)
        
        
        #cv2.imshow("Image_end",flop)
        
        card_flop = flop[bb[1]:bb[1]+bb[3],bb[0]:bb[0]+bb[2]]
        cv2.imshow("card_flop",card_flop)

        #aqui podemos rodar o modelo e adicionar em uma lista de cartas da mão

        cv2.waitKey(0)


if cv2.waitKey(50) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


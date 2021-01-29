# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:28:14 2021

@author: Axolotech
"""
import cv2 as cv 
import numpy as np
bgr = cv.imread("analitica.png")
canal1 = bgr[:,:,0]
canal2 = bgr[:,:,1]
canal3 = bgr[:,:,2]
canales = [canal1,canal2,canal3]
cv.imshow("bgr",np.hstack(canales))
cv.imshow("original",bgr)
rgb = cv.cvtColor(bgr,cv.COLOR_BGR2RGB)
canal1 = rgb[:,:,0]
canal2 = rgb[:,:,1]
canal3 = rgb[:,:,2]
canales = [canal1,canal2,canal3]
cv.imshow("RGB",np.hstack(canales))
cv.waitKey(0)
cv.destroyAllWindows()
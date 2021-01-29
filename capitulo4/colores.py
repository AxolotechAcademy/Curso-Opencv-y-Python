# -*- coding: utf-8 -*-
"""

@author: Axolotech
"""
import cv2 as cv 
import numpy as np

bgr = np.zeros((300,300,3),dtype=np.uint8)
bgr[:,:,:] = (230,0,120)
cv.imshow("color",bgr)
cv.waitKey(0)
cv.destroyAllWindows()

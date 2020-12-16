# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 as cv
import numpy as np
import os
def manejo_de_imagen():
    imagen = cv.imread("paisajeLago.jpg",0)
    cv.imshow("imagen",imagen)
    cv.imwrite("imagen_grises.jpg",imagen)
    cv.waitKey(0)
    cv.destroyAllWindows()

manejo_de_imagen()
    

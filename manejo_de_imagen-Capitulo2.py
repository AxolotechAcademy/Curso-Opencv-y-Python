# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 as cv

def manejo_de_imagen():
    imagen = cv.imread("paisajeLago.jpg",0)
    cv.imshow("paisaje",imagen)
    cv.imwrite("paisajeGrises.jpg",imagen)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
manejo_de_imagen()

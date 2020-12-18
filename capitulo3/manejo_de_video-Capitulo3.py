# -*- coding: utf-8 -*-
"""
@author: Axolotech
"""
import cv2 as cv

def manejo_de_video():
    video = cv.VideoCapture(0)
    salida = cv.VideoWriter("salida.mp4",cv.VideoWriter_fourcc(*'XVID'),30.0,(640,480))
    while(video.isOpened()):
        ret,frame = video.read()
        if ret == True:
            cv.imshow("stream",frame)
            salida.write(frame)
            if cv.waitKey(1) & 0xFF == ord('x'):
                break
        else:
            break
    video.release()
    salida.release()
    cv.destroyAllWindows()

def reproducir_video():
    video = cv.VideoCapture("salida.mp4")
    while(video.isOpened()):
        ret,frame = video.read()
        if ret == True:
            cv.imshow("stream",frame)
            if cv.waitKey(30) & 0xFF == ord('x'):
                break
        else:
            break
    video.release()
    cv.destroyAllWindows()
    
    

manejo_de_video()
reproducir_video()
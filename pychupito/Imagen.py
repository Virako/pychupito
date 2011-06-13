#!/usr/bin/env python
#-*- coding:utf-8 -*-


from opencv.highgui import cvCreateFileCapture, cvQueryFrame, cvSaveImage, cvCreateCameraCapture, cvReleaseCapture
from opencv.cv import cvCloneImage, CV_GRAY2RGB


class Imagen:

    def __init__(self):
        pass
    
    def crear_imagen(self, nombre_imagen):
        captura = cvCreateCameraCapture(0)
        imagen = cvQueryFrame(captura)
        cvSaveImage("imagenes/%s.png" %nombre_imagen, imagen)
        cvReleaseCapture(captura)
        
        

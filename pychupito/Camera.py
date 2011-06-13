#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    camera.py
#       
#    Copyright 2010 Victor Ramirez <virako.9@gmail.com>
#       
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



from opencv.highgui import *
from opencv.cv import *
from opencv import *
import os


class Camera:
    """ Clase para trabajar con las cámaras que estén conectadas al ordenador"""
    def __init__(self):
        self.name_cameras = []
        self.capture = None
    
    def check_name_cameras(self):
        """Función que devuelve los nombres de las camaras conectadas"""
        # Linux
        self.name_cameras = []
        if os.name == "posix": # al menos se que es un sistema compatible con UNIX
            list_dir = os.listdir("/dev")
            for d in list_dir:
                if d.__contains__("video"):
                    self.name_cameras.append(d) 
            return self.name_cameras
        else:
            print _("no funciona, estamos trabajando en ello")
            return self.name_cameras
        
    def open_camera(self, num):
        """Devuelve la captura de la cámara"""
        n = int(self.name_cameras[num][5:])
        self.capture = cvCreateCameraCapture(n)

    def get_frame(self):
        """Devuelve un frame de la captura"""
        return cvQueryFrame( self.capture )
        
    def close_camera(self):
        """Cierra la cámara abierta"""
        cvReleaseCapture( self.capture )
        

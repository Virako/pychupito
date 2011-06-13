#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    video.py
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


class Video:
    """ Clase para abrir videos"""
    def __init__(self):
        self.capture = None
    
    def open_video(self, path): # TODO falla aqui por que si
        """Devuelve la captura del video"""
        self.capture = cvCreateFileCapture(path)
                
    def get_frame(self):
        """Devuelve un frame de la captura"""
        return cvQueryFrame( self.capture )
        
    def close_video(self):
        """Cierra la cámara abierta"""
        cvReleaseCapture( self.capture )
        

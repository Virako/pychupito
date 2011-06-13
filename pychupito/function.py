#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    function.py
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



import gtk
from opencv.cv import *
from opencv.highgui import *

def convert_opencv2gtk(image):
    """Función que convierte una imágen de opencv en una imagen gtk """
    color = cvCreateImage(cvSize(image.width, image.height), IPL_DEPTH_8U, image.nChannels)
    cvConvertImage(image, color, CV_CVTIMG_SWAP_RB ) # convertimos imagen bgr a rgb
    pix = gtk.gdk.pixbuf_new_from_data (color.imageData, \
     gtk.gdk.COLORSPACE_RGB, False, color.depth, color.width, \
      color.height, color.widthStep)
    return pix

def convert_opencv_gray2gtk(image):
    """Función que convierte una imágen de opencv en una imagen gtk """
    color = cvCreateImage(cvSize(image.width, image.height), IPL_DEPTH_8U, 3)
    cvCvtColor(image, color, CV_GRAY2RGB)
    pix = gtk.gdk.pixbuf_new_from_data (color.imageData, \
     gtk.gdk.COLORSPACE_RGB, False, color.depth, color.width, \
      color.height, color.widthStep)
    return pix


def load_image_no_webcam():
    return cvLoadImage("images/no_webcam.png", CV_LOAD_IMAGE_COLOR)


def change_size_image(image, size=(200,150)):
    new_image = cvCreateImage(cvSize(200,150), image.depth, image.nChannels)
    cvResize(image, new_image, CV_INTER_NN)
    return new_image
    

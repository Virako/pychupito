#!/usr/bin/python
#-*- coding:utf-8 -*-


import os
import gtk

import gtk.glade
import gobject
from opencv.highgui import *
from opencv.cv import *
from opencv import *

from function import *
from Camera import Camera
from video import Video
from Borrachos import Borrachos
from Borracho import Borracho

class Main():
    """Clase principal """

    def __init__(self):
        self.camera = Camera()
        self.borracho_actual = None
        self.indice = 0
        
        # cargamos el archivo creado con glade
        self.gladefile = "pychupito/gui/chupiventana.glade"
        self.glade = gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        
        #cargamos las variables
        self.window = self.glade.get_object("chupiventana")
        self.image_add = self.glade.get_object("image_add")
        self.image_delete = self.glade.get_object("image_delete")
        #self.image_drink = self.glade.get_object("image_drink")
        
        self.button_add = self.glade.get_object("button_add")
        self.button_delete = self.glade.get_object("button_delete")
        self.button_previous = self.glade.get_object("button_previous")
        self.button_next = self.glade.get_object("button_next")
        #self.button_drink = self.glade.get_object("button_drink")
        
        # conectamos las señales
        self.glade.connect_signals(self)
        
        # modificamos las variables para mostrar o no los botones
        #self.window.set_icon_from_file("icono.png")
        self.window.set_title("PyChupito")
        self.button_previous.set_sensitive(False)
        self.button_next.set_sensitive(False)
        self.button_delete.set_sensitive(False)
        #self.button_drink.set_sensitive(False)
        
        # mostramos la cámara en la imagen de la izquierda
        self.camera.check_name_cameras()
        self.camera.open_camera(0)
        
        # creamos una especie de while
        self.refresh = gobject.timeout_add(50, self.update) # Bucle video 
        
        # creamos una lista de borrachos
        self.borrachos = Borrachos()
        
        # mostramos la ventana
        self.window.show()
        
        
    # callback 
    def button_add_clicked(self, widget):
        borracho = self.borrachos.agregar_borracho()
        nombre_imagen = borracho.agregar_imagen()
        
        frame = self.camera.get_frame()
        save = cvCloneImage(frame)
        try: cvSaveImage("imagenes/%s.png" %nombre_imagen, save)
        except: print "no se ha podido guardar la imagen"
        
        if len(self.borrachos.lista_borrachos) == 1:
            self.button_previous.set_sensitive(True)
            self.button_next.set_sensitive(True)
            self.button_delete.set_sensitive(True)
            #self.button_drink.set_sensitive(True)
        
        self.borracho_actual = self.borrachos.lista_borrachos[self.indice%self.borrachos.numero_borrachos]   
        nombre_imagen = self.borracho_actual.lista_imagenes[-1]
        imagen_borracho = cvLoadImage("imagenes/%s.png" %nombre_imagen)
        resized = change_size_image(imagen_borracho, (150, 100))
        self.load_image_delete(resized)
        
    
    def button_previous_clicked(self, widget):
        self.indice -= 1
        self.borracho_actual = self.borrachos.lista_borrachos[self.indice%self.borrachos.numero_borrachos]
        nombre_imagen = self.borracho_actual.lista_imagenes[-1]
        imagen_borracho = cvLoadImage("imagenes/%s.png" %nombre_imagen)
        resized = change_size_image(imagen_borracho, (150, 100))
        self.load_image_delete(resized)

        
    def button_next_clicked(self, widget):
        self.indice += 1
        self.borracho_actual = self.borrachos.lista_borrachos[self.indice%self.borrachos.numero_borrachos]   
        nombre_imagen = self.borracho_actual.lista_imagenes[-1]
        imagen_borracho = cvLoadImage("imagenes/%s.png" %nombre_imagen)
        resized = change_size_image(imagen_borracho, (150, 100))
        self.load_image_delete(resized)
                     
    def button_delete_clicked(self, widget):
        self.borrachos.eliminar_borracho(self.borracho_actual)
        self.indice -= 1
        self.borracho_actual = self.borrachos.lista_borrachos[self.indice%self.borrachos.numero_borrachos]
        nombre_imagen = self.borracho_actual.lista_imagenes[-1]
        imagen_borracho = cvLoadImage("imagenes/%s.png" %nombre_imagen)
        resized = change_size_image(imagen_borracho, (150, 100))
        self.load_image_delete(resized)
        
        if not self.borrachos.numero_borrachos:
            self.button_previous.set_sensitive(False)
            self.button_next.set_sensitive(False)
            self.button_delete.set_sensitive(False)
            self.button_drink.set_sensitive(False)
    
    def button_drink_clicked(self, widget):
        if not self.borrachos.numero_borrachos:
            print "TODO: MOSTRAR LA CARA DE ALGO GRACIOSO"
        elif self.borrachos.numero_borrachos > 1:
            borracho_aleatorio = self.borrachos.seleccionar_borracho_aleatorio()
            nombre_imagen = borracho_aleatorio.lista_imagenes[-1]
            print nombre_imagen
            imagen_borracho = cvLoadImage("imagenes/%s.png" %nombre_imagen)
            resized = change_size_image(imagen_borracho)
            self.load_image_drink(resized)
        else:
            print "Para jugar tu solo no lo uses "
            
    def gtk_main_quit(self, widget):
        """Funcion que es llamada cuando queremos cerramos la ventana. """
        gtk.main_quit()
        exit()
    
    
    # metodos 
    def load_image_add(self, image):
        """Nos carga una imagen en la parte izquierda de la pantalla. 
        @param image: imagen a cargar.
        @type image: L{IplImage}"""
        pix_buf = convert_opencv2gtk(image)
        self.image_add.set_from_pixbuf(pix_buf)
    
    def load_image_delete(self, image):
        """Nos carga una imagen en la parte derecha de la pantalla. 
        @param image: imagen a cargar.
        @type image: L{IplImage}"""
        pix_buf = convert_opencv2gtk(image)
        self.image_delete.set_from_pixbuf(pix_buf)
    
    def load_image_drink(self, image):
        """Comprueba si la ventana de configuración está abierta. 
        @return: True si la configuración se ha creado correctamente, 
         False en caso contrario.
        @rtype: C{bool}"""
        pix_buf = convert_opencv2gtk(image)
        self.image_drink.set_from_pixbuf(pix_buf)

    def update(self):
        """Función llamada por un bucle cada cierto tiempo que nos actualiza
         la cámara y el video mediante frame y los muesta por pantalla.
         @return: Devuelve True siempre que exista frame de una cámara o 
          un video, y False en caso de no encontrarlo.
         @rtype: C{bool}
         """
                
        if self.camera.capture == None:
            return False
        
        frame = self.camera.get_frame()
        resized = change_size_image(frame)
        self.load_image_add(resized)

        #if len(self.photos) >= 1: 
        #    self.load_image_delete(self.photos[self.pointer])
        #if self.pointer != -1 and self.rand != None: 
        #    self.load_image_delete(self.rand)
        #    print "Entro"
            
        return True
    
        
if __name__ == '__main__':
    Main()
    gtk.main()
        

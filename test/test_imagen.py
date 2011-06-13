#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import sys
sys.path.insert(0,"../")

import unittest

from pychupito.Borracho import Borracho
from pychupito.Borrachos import Borrachos
from pychupito.Imagen import Imagen
from pychupito.Camera import Camera

    
class Test_imagen(unittest.TestCase):

    def setUp(self):
        self.borracho1 = Borracho()
        self.borracho2 = Borracho()
        self.borrachos = Borrachos()
        self.imagen1 = Imagen()
        
    def tearDown(self):
        pass     
    ## Test de carga de imágenes
    
    def test_crear_imagen(self):
        self.assertFalse(self.imagen1 == None)
        
    
    def test_guardar_imagen_y_comprobar_que_el_tamanyo_es_mayor_que_cero(self):
        nombre_imagen = "ima1"
        self.imagen1.crear_imagen(nombre_imagen)
        self.assertTrue(os.path.exists("imagenes/%s.png" %(nombre_imagen)) and \
         os.path.exists("imagenes/%s.png" %(nombre_imagen)) > 0)
    
    def _test_eliminar_imagenes_de_borracho_eliminado(self):
        # Añadimos dos imagenes al borracho1
        nombre_imagen = str(self.borracho1.id_borracho) + "_" + \
                           str(len(self.borracho1.lista_imagenes))
        self.borracho1.agregar_imagen(nombre_imagen)
        self.imagen1.crear_imagen(nombre_imagen)
        
        nombre_imagen = str(self.borracho2.id_borracho) + "_" + \
                           str(len(self.borracho2.lista_imagenes))
        self.borracho1.agregar_imagen(nombre_imagen)
        self.imagen1.crear_imagen(nombre_imagen)
        
        # creamos cadena que guarde el comienzo del nombre de las fotos
        str_borracho = str(self.borracho1.id_borracho) + "_"
       
        existe = False
        for filename in os.listdir("imagenes"):
            if filename.find(str_borracho) == 0:
                existe = True
                break
        self.assertFalse(existe)
        
        
    ## Test de imagen en borrachos
    
    def _test_seleccionar_foto_de_borracho_correcta(self):
        
        # Primero creamos 2 borrachos, uno con dos fotos y otro con una
        nombre_imagen = str(self.borracho1.id_borracho) + "_" + \
                           str(len(self.borracho1.lista_imagenes))
        self.borracho1.agregar_imagen(nombre_imagen)
        self.imagen1.crear_imagen(nombre_imagen)
        
        nombre_imagen = str(self.borracho2.id_borracho) + "_" + \
                           str(len(self.borracho2.lista_imagenes))
        self.borracho2.agregar_imagen(nombre_imagen)
        self.imagen1.crear_imagen(nombre_imagen)
        
        nombre_imagen = str(self.borracho1.id_borracho) + "_" + \
                           str(len(self.borracho1.lista_imagenes))
        self.borracho1.agregar_imagen(nombre_imagen)
        self.imagen1.crear_imagen(nombre_imagen)
        
        # Agregamos cada borracho a borrachos
        self.borrachos.agregar_borracho(self.borracho1)
        self.borrachos.agregar_borracho(self.borracho2)
        
        # Ahora buscamos un borracho aleatorio
        imagen_seleccionada = self.borrachos.seleccionar_imagen_aleatoria()
        
        existe = False
        for borracho in self.borrachos.lista_borrachos:
            if imagen_seleccionada == borracho.lista_imagenes[-1]:
                existe = True
        self.assertTrue(existe)
        
        

if __name__ == '__main__':
    unittest.main()

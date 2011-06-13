#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
sys.path.insert(0,"../")

import unittest

from pychupito.Borracho import Borracho
from pychupito.Copa import Copa

class Test_borracho(unittest.TestCase):

    def setUp(self):
        self.borracho1 = Borracho()
        self.borracho2 = Borracho()
        self.copa1 = Copa()
        
    def tearDown(self):
        pass 
    
    ## Test de Borracho y Copa    
    def test_borracho_creado(self):
       self.assertFalse(self.borracho1 == None)
       
    def test_el_borracho_creado_a_bebido_cero_copas(self):
        self.assertTrue(self.borracho1.copas_bebidas == 0)
    
    def _test_agregar_nombre_imagen_borracho_a_lista_nombre_imagenes(self):#TODO
        anterior = len(self.borracho1.lista_imagenes)
        self.borracho1.agregar_imagen("1.png")
        posterior = len(self.borracho1.lista_imagenes)
        
    def test_si_borracho_bebe_aumenta_en_uno_las_copas_bebidas(self):
        anteriores = self.borracho1.copas_bebidas
        self.borracho1.bebe_copa()
        posteriores = self.borracho1.copas_bebidas
        self.assertEquals(posteriores - anteriores, 1)
    
        

if __name__ == '__main__':
    unittest.main()

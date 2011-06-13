#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
sys.path.insert(0,"../")

import unittest

from pychupito.Borracho import Borracho
from pychupito.Borrachos import Borrachos

    
class Test_borrachos(unittest.TestCase):

    def setUp(self):
        self.borracho1 = Borracho()
        self.borracho2 = Borracho()
        self.borrachos = Borrachos()
        
    def tearDown(self):
        pass 
            
    ## Test de Borrachos
    def test_crear_lista_de_borrachos(self):
        self.assertFalse(self.borrachos == None)
    
    def test_agregar_borracho(self):
        anteriores = self.borrachos.numero_borrachos
        self.borrachos.agregar_borracho()
        posteriores = self.borrachos.numero_borrachos
        #self.borrachos.eliminar_borracho(self.borracho1)
        self.assertEquals(posteriores - anteriores, 1)
        
    
    def _test_eliminar_borracho(self): #TODO hay que eliminar las imagenes tb
        self.borrachos.agregar_borracho(self.borracho1)
        anteriores = self.borrachos.numero_borrachos
        self.borrachos.eliminar_borracho(self.borracho1)
        posteriores = self.borrachos.numero_borrachos
        self.assertEquals(anteriores - posteriores, 1)
    
        
        

if __name__ == '__main__':
    unittest.main()

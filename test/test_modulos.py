#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import sys
sys.path.insert(0,"../")

import unittest
import time 
import platform

from pychupito.Borracho import Borracho
from pychupito.Borrachos import Borrachos
from pychupito.Copa import Copa
from pychupito.Imagen import Imagen
from pychupito.Camera import Camera


class Test_modulos(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass     
    ## Test para comprobar que cada plataforma tiene un modulo asignado

    def _test_comprueba_que_cada_plataforma_tiene_asignado_un_modulo(self):
        plataformas = ("Linux", "Windows")
        maquinas = ("i686", "armv61")
        modulos = []
        
        for plataforma in plataformas:
            for maquina in maquinas:
                modulos.append(imagen1.seleccionar_modulo(plataforma, maquina))
        
        check = True
        for modulo in modulos:
            pass
        
        
        
        

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Borracho import Borracho
import random

class Borrachos:
    
    def __init__(self):
        self.numero_borrachos = 0
        self.lista_borrachos = []
        self.anterior = -1
     
    def agregar_borracho(self):
        b = Borracho()
        self.lista_borrachos.append(b)
        self.numero_borrachos += 1
        return b
    
    def eliminar_borracho(self, borracho):
        self.lista_borrachos.remove(borracho)
        self.numero_borrachos -= 1
    
    def seleccionar_borracho_aleatorio_sin_repeticion(self):
        """ Por defecto mostramos la última imagen, que debería ser 
            la más desfavorecida"""
        
        actual = random.choice(self.lista_borrachos)
        if self.anterior != actual:
            self.anterior = actual
            print "borracho", actual
            return actual
        else:
            self.seleccionar_borracho_aleatorio_sin_repeticion()

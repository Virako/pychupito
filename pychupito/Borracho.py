#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Borracho:
    """ Objeto que contendrá la información de cada borracho, como el número 
        de copas bebidas y las imágenes. """
    id_borrachos = 0

    def __init__(self):
        Borracho.id_borrachos += 1
        self.id_borracho = Borracho.id_borrachos
        self.copas_bebidas = 0
        self.lista_imagenes = []
        
    def bebe_copa(self):
        self.copas_bebidas += 1
        
    
    def agregar_imagen(self):
        nombre_imagen = self.id_borracho.__str__() + "_" + \
                            len(borracho.lista_imagenes).__str__()
        self.lista_imagenes.append(nombre_imagen)
        return nombre_imagen
    

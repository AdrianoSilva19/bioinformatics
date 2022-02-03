# -*- coding: utf-8 -*-

f"""
Created on Nov 14 04:38:26 2021 

@author: Adriano Silva
"""

from math import pi
class circulo: # podemos colocar o circulo como um quadrado de lado igual ao diametro do circulo, apenas a area é diferente calculada como se o diamtro fosse o lado
    def __init__(self, largura,altura):
        self.altura=altura
        self.largura=largura
    # diametro é igual ao lado de um dos quadrados
    def area(self):
        return pi*((self.largura)/2)**2
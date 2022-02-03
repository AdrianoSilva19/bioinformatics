# -*- coding: utf-8 -*-

f"""
Created on Nov 14 04:38:26 2021 

@author: Adriano Silva
"""


class rectangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.lin = -1
        self.col = -1

    def area(self):
        return self.largura * self.altura

    def rodar_retangulo(self):
        x=self.altura
        y=self.largura
        self.largura = x
        self.altura = y
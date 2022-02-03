# -*- coding: utf-8 -*-

f"""
Created on Nov 14 04:38:26 2021 

@author: Adriano Silva
"""

from poo_circulo import circulo
from poo_retangulo import rectangulo
from poo_superficie import superficie

def teste():
    sup = superficie(largura=500, altura=1000)
    R1 = rectangulo(largura=100, altura=100)
    R2 = rectangulo(largura=100, altura=200)
    R3 = rectangulo(largura=50, altura=100)
    R4 = rectangulo(largura=400, altura=400)
    R5 = rectangulo(largura=200, altura=200)
    '''para conseguir introduzir os circulos considerei o diametro como largura e altura de um quadrado 
        introduzi o circulo como sendo um quadrado mas a area será dada como a area de um circulo'''
    C1 = circulo(largura=100,altura=100)
    C2 = circulo(largura=100,altura=100)
    C3 = circulo(largura=100,altura=100)
    C4 = circulo(largura=50, altura=50)
    print(f"A superficie sup tem de area: {sup.area()}")
    lista=[R1,R2,R3,R4,R5,C1,C2,C3,C4]
    lista_retangulos=[R3,R1,R2,R5,R4]
    lista_circulos=[C4,C2,C3,C1]
    for fig in range(len(lista)-4):
        print(f"O rectangulo {fig+1} tem de area: {lista[fig].area()}")
    for fig in range(5,len(lista)):
        print(f"O circulo {fig-4} tem de area: {lista[fig].area():.2f}")
    # colocação e manuseamento de figuras na superficie
    print(f'Colocar R1: {sup.colocar(R1, lin=10, col=10)}') #vão ter de retornar se houve sucesso
    print(f'Colocar R2: {sup.colocar(R2, lin=70, col=100)}') # isto não deve ser possível
    print(f'Mover R1: {sup.mover(R1, lin=181, col=0)}')
    print(f'Colocar R2: {sup.colocar(R2, lin=70, col=100)}') #isto já deve ser possível
    print(f'Area total ocupada: {sup.sup_ocupacao()}') #área da superfície coberta por figuras
    print(f'Figuras na superficie: {len(sup.lista_fig)}')
    sup.remover()   # temos de remover todas as figuras já colocadas para proceder a colocação do máximo de figuras
    print('!!!!!!!Todas as figuras foram removidas da superficie!!!!!!!')
    print(f'Figuras na superficie: {len(sup.lista_fig)}') # confirmar que não há figuras
    # Para colocar todas as figuras ordenei por ordem decrescente de area
    print(f'Figuras colocadas: {sup.colocar_auto(lista_retangulos,lista_circulos)}')
    print(f'Area total ocupada: {sup.sup_ocupacao():.2f}')


teste()


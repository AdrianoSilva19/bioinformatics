# -*- coding: utf-8 -*-

#Exercício
#Dada uma sequência de números inteiros, pretende-se uma função que crie uma 
#lista sem elementos repetidos a partir dessa sequência, usando um só ciclo 
#(sugestão: use dicionários).

#por listas
def sequencia():
    L=[]
    n=int(input("Quantos valores tem a sequencia? "))
    for i in range(n):
        x=float(input("Introduza o valor "))
        L.append(x)
        if(L.count(x)>1):
            L.remove(x)
    print(L)
#sequencia()

#por dicionário
def sem_repetidos(L):
    dic={}
    for el in L:
        dic[el]=1
    return list(dic.keys()), list(dic.values())
        
def teste_sem_repetidos():
    n = int(input('tamanho da sequencia: '))
    Seq = []
    for i in range (n):
        x = int(input(f'introduza o valor {i+1}: '))
        Seq.append(x)
    print(sem_repetidos(Seq))
#teste_sem_repetidos()
    
#
#
#
#

#inserir valores não repetidos numa lista
def sequenciaNrepetida():
    n=int(input('Tamanho da sequência: '))
    y=0
    L=[]
    while n!=y:
        x=int(input('Introduzir valor: '))
        if ((L.count(x)) == 0):
            L.append(x)
        else:
            L.remove(x)
            L.append(x)
        y=y+1
    print(L)

#sequenciaNrepetida()

def sequenciaNrepetida2():
    L=[]
    n=int(input("Número de valores da sequência: "))
    for i in range(n):
        x=float(input("Introduza um valor:  "))
        L.append(x)
        if(L.count(x)>1):
            L.remove(x)
    print(L)

#sequenciaNrepetida2()
    
#inserir valores não repetidos usando dicionários    
def dic_sem_repetidos(L):
    dic = {}
    for i in L:
        dic[i] = 1 
    return list(dic.keys())
            
def intr_sequencia():
    n = int(input("Número de algarismos da sequência: "))
    Seq = []
    for i in range (n):
        x = float(input("Introduza um número: "))
        Seq.append(x)
    print(dic_sem_repetidos(Seq))
    
#intr_sequencia()

def lista_dic_sem_repetidos():
    n=int(input("Número de elementos da sequência: "))
    lista=[]
    dic={}
    for i in range(n):
        num=int(input("Elemento da sequência: "))
        lista.append(num)    
    for el in lista:
        dic[el]="chave"
    print(list(dic.keys()))

#lista_dic_sem_repetidos()
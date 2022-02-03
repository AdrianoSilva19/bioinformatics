'''Dada uma sequência de números inteiros, ordenar essa sequência:
a) por ordem crescente
b) uma lista sem repetições ( usar dicionarios )'''

lista=[8,2,3,4,2,7,8,9,3,3,4,5,0]

def ordenar(l):
    n=len(l)
    for i in range (0,n -1):
        for j in range(i+1,n):
            if l[j]<l[i]:  # mudar o sinal para ordenar decrescente
                guardar=l[j]
                l[j]=l[i]
                l[i]=guardar
    return l

def procura_binaria(lista,x):
    inf=0
    sup=len(lista)-1
    terminado=False
    encontrado=False
    while not terminado:
        p=int(((sup-inf)+1)/2+inf)
        if lista[p]==x:
            encontrado=True
            terminado=True
        if lista[p]<x:
            inf=p+1
        else:
            sup=p-1
    if encontrado:
        return p
    else:
        return -1


def lista_s_repetidos(lista):
    sem_rep={}
    for num in lista:
        sem_rep[num]=1
    return list(sem_rep.keys())


print(lista_s_repetidos(lista))
x = ordenar(lista)
print(x)
print(procura_binaria(x, 4))


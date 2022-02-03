# Procura sequencial numa lista ordenada
L=[3,1,2,5,6]
def procura_bin(LL, xx):
    inf = 0
    sup = len(LL) - 1
    terminado = False
    encontrado = False
    while not terminado:
        p = int(((sup - inf) + 1) / 2 + inf)
        if LL[p] == xx:
            terminado = True
            encontrado = True
        elif LL[p] < xx:
            inf = p + 1
        else:
            sup = p - 1
        if sup < inf:
            terminado = True
    if encontrado:
        return p
    else:
        return -1
def ordena(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista[j] < lista[i]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    return lista

def teste_procura_bin(lista):
    x = int(input("Elemento a procurar:"))
    lista=ordena((lista))
    pos = procura_bin(lista, x)
    if pos != -1:
        print("%s foi encontrado na posição %d" % (x, pos))
    else:
        print("%s não foi encontrado!" % (x))

teste_procura_bin(L)



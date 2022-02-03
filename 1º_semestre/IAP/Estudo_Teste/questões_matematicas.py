'''1-Dado um número n, calcular o seu factorial

2- desenvolver uma função que recebe uma lista (L) e devolve uma lista com os fatoriais dos numero em L

3-De entre o conjunto de números com 3 algarismos, determinar aqueles que são iguais à
soma dos cubos dos algarismos que os constituem.
Por exemplo: 153 = 1**3+ 5**3+ 3**3

4-Dado um número n, calcular os números de Fibonacci que lhe são inferiores.

5- Pretende-se o desenvolvimento da função fibolista(L) que recebe como parâmetro uma lista L de
números inteiros e retorna uma lista de listas. Cada uma dessas listas contém os números de Fibonacci que são inferiores a L
'''


# 1 - Não pode ser multiplicado por 0 senão vai dar smp zero, o i começa em 5 e vai decrescendo
def fatorial(n : int):
    resultado=1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# 2 - função fatorial L
def fatorial_l(l):
    numeros=l
    lista_fatorial=[]
    for n in numeros:
        resultado=1
        for i in range (1,n+1):
            resultado*=i
        lista_fatorial.append(resultado)
    return  lista_fatorial

# 3 - Recebe uma lista de valores e devolve aqueles em que são o valor do cubo dos constituintes dá o valor do numero
def val_cubo():
    valores=[]
    for n in range(100,1000):
        val=str(n)
        p = val[0]
        s = val[1]
        t = val[2]
        if (int(p)**3 + int(s)**3 + int(t)**3) == int(val):
            valores.append (val)
    return ", ".join(valores)



# 4 - fibonacci é o valor de n multiplicado pelo anterior, numa lista sera smp o ultimo pelo penultimo
def fibonacci(n : int):
    fibs = [0, 1]
    lista = []
    for i in range(2, n + 1):# já la tem os 2 primeiros (0,1)
        fibs.append(fibs[-1] + fibs[-2])
    for num in fibs:
        if num < n:
            lista.append(str(num))
        else:
            break
    return ", ".join(lista)


# 5 - fibonacci com lista de valores
def fibonacci_lst(lista ):
    lista_val=lista
    l=[]
    for n in lista_val:
        fibs = [2,3]
        lista = []
        for i in range(2, n + 1):# já la tem os 2 primeiros (0,1)
            fibs.append(fibs[-1] + fibs[-2])
        for num in fibs:
            if num<n:
                lista.append(num)
        l.append(lista)
    return l




def testagem():
    print(f'Fatorial: \n{fatorial(5)}')
    print(f'Fibonacci: \n{fibonacci(40)}')
    print(f'Lista de fatoriais:\n{fatorial_l([1,2,5,4])}')
    print(f'Conjunto de numeros de três algarismos os quais os constituintes ao cubo dão o seu valor: \n{val_cubo()}')
    print(fibonacci_lst([6,1,0,3]))
testagem()
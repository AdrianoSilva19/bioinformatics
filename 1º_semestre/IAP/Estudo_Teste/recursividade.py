'''função chama-se a si propria mas com valores diferentes, tem de conter um Stop para nao ser infinitamente chamada'''

# fatorial com recursividade

def fatorial(n):
    if n==0:
        return 1
    return n * fatorial(n-1)    # vai adicionando sempre valores de n-1 até ser 0 e adicionar 1

print(fatorial(5))

# multiplicar atraves de somas

def multiply(a,b):
    if a==0 or b==0:
        return 0
    if a==1:
        return b
    else:
        return b + multiply(a-1,b)

print(multiply(5,1))

# função recursiva para multiplos de 3

def somatorio(n):
    if n==1:
        return 1
    else:
        return n + somatorio(n-1)

print(somatorio(3))

# potencia de base 2

def potencia2(n):
    if n == 0:
        return 1
    else:
        return 2 * potencia2(n - 1)

print(potencia2(3))

def pascal(n):
    if n == 1:
        line = [1]
        print(line)
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
    line += [1] #para acrescentar o 1 no final
    print(line)
    return line
pascal(5)

'''1-Pretende-se o desenvolvimento da função somapares(M) que recebe como parâmetro uma matriz M de
números inteiros e retorna o somatório de todos os números pares da Matriz.'''

def somapares(M):
    matriz=M
    soma=0
    for lin in matriz:
        for num in lin:
            if num%2 == 0:
                soma+=num
    return soma

'''Desenvolva um algoritmo que permita calcular o número de dias entre duas datas. Por exemplo
considerando as datas (2019, 1, 1) e (2019, 1, 11) o valor obtido deveria ser 10. Para facilitar pode considerar a
existência de uma biblioteca para processamento de datas (no caso do python seria: from datetime import date)'''

from datetime import date

def diferenca_datas():
    d1 = date(int(input('year date 1: ')),int(input('month date 1: ')),int(input('day date 1: ')))
    d2 = date(int(input('year date 2: ')), int(input('month date 2: ')), int(input('day date 2: ')))
    print(f'As datas têm diferença de {abs(d1-d2).days} dias')  # valor absoluto


'''3 - Desenvolva a função ContaLetras(ficheiro) que recebe como parâmetro o nome
de um ficheiro e escreve uma lista das letras existentes no ficheiro e a quantidade de vezes
que cada letra se repete. Só devem ser contadas as letras, sendo ignorado o fato de estarem na
forma de maiúsculas, minúsculas ou acentuadas.
Por exemplo considerando o seguinte conteúdo de um ficheiro: “O objetivo deste módulo é
introduzir a metodologia que deve ser seguida quando se pretende resolver 1 problema.”, o
resultado deveria ser qualquer coisa do género do apresentado na figura ao lado'''

def check_freq(ficheiro):
    freq = {}
    texto= open(ficheiro, encoding='utf-8').read()
    texto = texto.replace(" ", "")
    texto = texto.replace("\n", "")
    texto = texto.replace(".", "")
    texto = texto.replace("!", "")
    texto = texto.replace("?", "")
    texto = texto.replace(",", "")
    texto = texto.replace(";", "")
    for palavra in texto.split():
        for l in palavra:
            freq[l] = palavra.count(l)
    return freq
print(check_freq("frase.txt"))


'''4 - Pretende-se uma função em que dado uma tabela desenhe o correspondente
gráfico de barras. A tabela será dada por uma lista de tuplos, em que o primeiro
elemento do tuplo corresponde à coluna e o segundo elemento corresponde ao valor. O
gráfico resultante não deverá ter colunas com mais do que 10 carateres (se houver
valores superiores terá de ser feito um ajuste de escala). Por exemplo, dada a tabela
[(‘A’,3),(‘B’,1),(‘C’,4),(‘D’,5),(‘E’,2),(‘F’,3)] devia aparecer no terminal um gráfico
semelhante ao apresentado na figura ao lado'''

lista = [('A', 3), ('B', 1), ('C', 4), ('D', 5), ('E', 2), ('F', 3)]


def grafico_barras(lista):
    coluna = []
    val = []
    for t in lista:
        c, v = t[0], t[1]
        coluna.append(c)
        val.append(v)
    # print(coluna)
    # print(val)
    mat_zero = [[0 for c in range(len(coluna))] for l in range(max(val))]
    for i in range(max(val)):
        for v in range(len(coluna)):
            for c in range(val[v]):
                mat_zero[-1 - c][v] = "#"

    return mat_zero


def print_grafico(mat):
    decrescente = []
    for c in range(1, len(mat) + 1):
        decrescente.append(c)
    decrescente = decrescente[::-1]
    for l in range(len(mat)):
        string = f"{decrescente[l]} ! "
        for c in mat[l]:
            string += f"{c} "
        print(string)


print_grafico(grafico_barras(lista))

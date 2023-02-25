'''
Created on 29/11/2015

@author: valves
'''

from tracemalloc import stop
from Stack import Stack

class IlluminatiEngine:
    
    def __init__(self):
        self.linhas = 0
        self.colunas = 0
        self.tabuleiro = [] #matriz que representa o puzzle illuminati
        self.tabuleiro_inicial = []
        self.stack_jogada = Stack()
    
    def ler_tabuleiro_ficheiro(self, filename):
        '''
        Cria nova instancia do jogo
        :param filename: nome do ficheiro a ler
        '''
        try:
            ficheiro = open(filename, "r")
            lines = ficheiro.readlines()
            dim = lines[0].strip('\n').split(' ')  # obter os dois numeros da dimensao do puzzle, retirando o '\n' 
            self.linhas = int(dim[0])  # retirar o numero de linhas
            self.colunas = int(dim[1])  # retirar o numero de colunas
            del lines[0]  # remover primeira linha da lista de linhas pois ja nao precisamos
            for line in lines:
                self.tabuleiro.append(line.split())
            return self.tabuleiro
        except:
            print("Erro: na leitura do tabuleiro")
        else:
            self.ficheiro.close()
        return self.tabuleiro
    
    def getlinhas(self):
        '''
        Chama a variavel self.linhas para ser usada por outras classes
        '''
        return self.linhas
    
    def getcolunas(self):
        '''
        Chama a variavel self.colunas para ser usada por outras classes
        '''
        return self.colunas
    
    def gettabuleiro(self):
        '''
        Chama a variavel self.tabuleiro para ser usada por outras classes
        '''
        return self.tabuleiro

    def settabuleiro_inicial (self, t):
        '''
        Usa o valor de outra classe para modificar o valor do self.tabuleiro_inicial
        :param t: tabuleiro devolvido de outra classe
        '''
        self.tabuleiro_inicial = t

    def settabuleiro (self, x, l, c):
        '''
        Usa o valor de outra classe para alterar o valor do self.tabuleiro

        :param x: simbolo da lampada '@'
        :param l: linha a colocar
        :param c: coluna a colocar
        '''
        self.tabuleiro[l][c] = x

    def printpuzzle(self):
        '''
        Imprime o puzzle na consola de modo a acompanhar visualmente o jogo
        '''
        for linha in self.tabuleiro:
            for simbolo in linha:
                print(simbolo,end=" ")
            print()

    def jogada (self, tabuleiro):
        '''
        Insere o valor tabuleiro na Stack stack_jogada
        :param tabuleiro: Tabuleiro que se quer guardar
        '''
        self.stack_jogada.push(tabuleiro)

    def pontos (self, l, c):
        '''
        Função que permite verificar quais são as casas onde não se pode jogar

        :param l: linha do tabuleiro
        :param:c: coluna do tabuleiro
        '''
        tabuleiro=self.tabuleiro 
        L=[]
        for i in range(l):
            for j in range(c):
                if tabuleiro[i][j] != '-': 
                    L.append((i,j))
        return L

    def dentro_tabuleiro (self, l, c):
        '''
        Função que verifica se a casa definida pelo utilizador se encontra dentro dos limites do tabuleiro

        :param l: linha da casa
        :param c: coluna da casa
        '''
        if l < 0 or l >= self.linhas:
            dentro = False
        elif c < 0 or c >= self.colunas:
            dentro = False
        else:
            dentro = True
        return dentro

    def lampadas_vizinhas (self, linha, coluna,simbolo):
        '''
        Devolve o número lâmpadas ("@") que se encontram em casas vizinhas a uma determinada casa.
        Parâmetros:
            - linha: inteiro correspondente ao índice da linha onde está a casa à volta da qual se quer ver o nº de casas
            - Coluna: inteiro correspondente ao índice da coluna onde está a casa à volta da qual se quer ver o nº de casas
        Retorna: inteiro correspondente ao número de lâmpadas
        '''
        cont = 0
        t = self.tabuleiro
        if self.dentro_tabuleiro(linha - 1, coluna) and t[linha - 1][coluna] == simbolo:  # Se houver lâmpada em cima da casa
            cont += 1
        if self.dentro_tabuleiro(linha + 1, coluna) and t[linha + 1][coluna] == simbolo:  # Se houver lâmpada em baixo da casa
            cont += 1
        if self.dentro_tabuleiro(linha, coluna - 1) and t[linha][coluna - 1] == simbolo:  # Se houver lâmpada à esquerda da casa
            cont += 1
        if self.dentro_tabuleiro(linha, coluna + 1) and t[linha][coluna + 1] == simbolo:  # Se houver lâmpada à direita da casa
            cont += 1
        return cont

    def vizinhanca (self, l, c):
        t = self.tabuleiro
        possivel = True
        lista_restricao = ['0', '1', '2', '3', '4']
        if self.dentro_tabuleiro(l, c + 1) and  t[l][c + 1] in lista_restricao:
            valor = int(t[l][c + 1])
            if self.lampadas_vizinhas(l, c + 1,'@') >= valor:
                possivel = False

        if self.dentro_tabuleiro(l, c - 1) and t[l][c - 1] in lista_restricao:
            valor = int(t[l][c - 1])
            if self.lampadas_vizinhas(l, c - 1,'@') >= valor:
                possivel = False
        
        if self.dentro_tabuleiro(l + 1, c) and t[l + 1][c] in lista_restricao:
            valor = int(t[l + 1][c])
            if self.lampadas_vizinhas(l + 1, c,'@') >= valor:
                possivel = False

        if self.dentro_tabuleiro(l - 1, c) and t[l - 1][c] in lista_restricao:
            valor = int(t[l - 1][c])
            if self.lampadas_vizinhas(l - 1, c,'@') >= valor:
                possivel = False
        return possivel

    
    def casas_bloqueadas(self):
        lista_restricao=["0","1","2","3","4"]
        t=self.tabuleiro
        pintou=False
        for lin in range (self.colunas):
            for col in range (self.linhas):
                if self.dentro_tabuleiro(lin,col) and t[lin][col] in lista_restricao:
                    valor=int(t[lin][col])
                    if self.lampadas_vizinhas(lin,col,'@') >= valor:
                        if self.dentro_tabuleiro(lin+1,col) and t[lin+1][col]=='-':
                            t[lin+1][col]='.'
                            pintou=True
                        if self.dentro_tabuleiro(lin-1,col) and t[lin-1][col]=='-':
                            t[lin-1][col]='.'
                            pintou=True
                        if self.dentro_tabuleiro(lin,col+1) and t[lin][col+1]=='-':
                            t[lin][col+1]='.'
                            pintou=True
                        if self.dentro_tabuleiro(lin,col-1) and t[lin][col-1]=='-' :
                            t[lin][col-1]='.'
                            pintou=True
        return pintou
        
    def colocar_auto(self):
        lista_restricao=["0","1","2","3","4"]
        t=self.tabuleiro
        for lin in range (self.colunas+1):
            for col in range (self.linhas+1):
                if self.dentro_tabuleiro(lin,col) and t[lin][col] in lista_restricao:
                    valor=int(t[lin][col])
                    if valor >= self.lampadas_vizinhas(lin,col,'-'):  
                        if valor>self.lampadas_vizinhas(lin,col,'@') and self.dentro_tabuleiro(lin+1,col) and t[lin+1][col]=='-' and (valor-self.lampadas_vizinhas(lin,col,'@')==self.lampadas_vizinhas(lin,col,'-')):
                            t[lin+1][col]='@'
                            self.iluminar(lin+1,col)
                        if valor>self.lampadas_vizinhas(lin,col,'@') and self.dentro_tabuleiro(lin-1,col) and t[lin-1][col]=='-' and (valor-self.lampadas_vizinhas(lin,col,'@')==self.lampadas_vizinhas(lin,col,'-')):
                            t[lin-1][col]='@'
                            self.iluminar(lin-1,col)
                        if valor>self.lampadas_vizinhas(lin,col,'@') and self.dentro_tabuleiro(lin,col+1) and t[lin][col+1]=='-' and (valor-self.lampadas_vizinhas(lin,col,'@')==self.lampadas_vizinhas(lin,col,'-')):
                            t[lin][col+1]='@'
                            self.iluminar(lin,col+1)
                        if valor>self.lampadas_vizinhas(lin,col,'@') and self.dentro_tabuleiro(lin,col-1) and t[lin][col-1]=='-' and (valor-self.lampadas_vizinhas(lin,col,'@')==self.lampadas_vizinhas(lin,col,'-')):
                            t[lin][col-1]='@'
                            self.iluminar(lin,col-1)


    def ver_lampadas(self,l,c):
        '''
        Verifica que não existe nenhuma lampada na mesma linha e coluna da casa onde queremos colocar a nossa
        :param l: linha da casa
        :param c: coluna da casa
        '''
        t = self.tabuleiro
        encontrada = False
        lista_restricoes = ['0', '1', '2', '3', '4', 'x']
        for col in range(self.linhas): # percorre a linha para esquerda
            if self.dentro_tabuleiro(l,c-col):
                if t[l][c-col ] == '@':
                    encontrada = True
                #elif t[l][c-col] != "o":
                #    continue
                elif t[l][c-col] in lista_restricoes:
                    break

        for col in range(self.linhas): #percore linha para direita
            if self.dentro_tabuleiro(l,c+col):
                if t[l][c+col]=='@':
                    encontrada = True
                #elif t[l][c+col]!="o":
                #    continue
                elif t[l][c+col] in lista_restricoes:
                    break

        for lin in range(self.colunas): # percorre coluna
            if self.dentro_tabuleiro(l-lin,c):
                if t[l-lin][c]=='@':
                    encontrada = True
                #elif t[l-lin][c]!="o":
                #    continue
                elif t[l-lin][c] in lista_restricoes:
                    break

        for lin in range(self.colunas):     
            if self.dentro_tabuleiro(l+lin,c):
                if t[l+lin][c]=='@':
                    encontrada = True
                #elif t[l+lin][c] != "o":
                #    continue
                elif t[l+lin][c] in lista_restricoes:
                    break
        return encontrada
        
    
    def iluminar (self, l, c):
        '''
        Função que ilumina as casas passíveis de serem iluminadas por uma lampada
        :param l: linha
        :param c: coluna
        '''
        lista_restricao = ['0', '1', '2', '3', '4', 'x']
        t = self.tabuleiro
        for col in range(1,self.linhas+1): # percorre a coluna para cima
            if self.dentro_tabuleiro(l,c-col):
                if t[l][c-col]=='-':
                    t[l][c-col]='o'
                elif t[l][c-col]=='o':
                    t[l][c-col]='o'
                elif t[l][c-col]=='.':
                    t[l][c-col]='o'
                elif t[l][c-col] in lista_restricao:
                    break
        for col in range(1,self.linhas+1): # percorre a coluna para baixo
            if self.dentro_tabuleiro(l,c+col):
                if t[l][c+col]=='-':
                    t[l][c+col]='o'
                elif t[l][c+col]=='o':
                    t[l][c+col]='o'
                elif t[l][c+col]=='.':
                    t[l][c+col]='o'
                elif t[l][c+col] in lista_restricao:
                    break

        for lin in range(1,self.colunas+1): # percorre linha para esquerda
            if self.dentro_tabuleiro(l-lin,c):
                if t[l-lin][c]=='-':
                    t[l-lin][c] = "o"
                elif t[l-lin][c]=='o':
                    t[l-lin][c] = "o"
                elif t[l-lin][c]=='.':
                    t[l-lin][c] = "o"
                elif t[l-lin][c] in lista_restricao:
                    break

        for lin in range(1,self.colunas+1): # percorre linha para direita
            if self.dentro_tabuleiro(l+lin,c):
                if t[l+lin][c]=='-':
                    t[l+lin][c] = "o"
                if t[l+lin][c]=='o':
                    t[l+lin][c] = "o"
                if t[l+lin][c]=='.':
                    t[l+lin][c] = "o"
                elif t[l+lin][c] in lista_restricao:
                    break
    
    def desiluminar (self, l, c):
        '''
        Função que desilumina as casas iluminadas por uma lampada que vai ser retirada
        :param l: linha da lampada
        :param c: coluna da lampada
        '''
        lista_restricoes = ['0', '1', '2', '3', '4', 'x']
        t = self.tabuleiro
        for col in range(1,self.linhas+1): # percorre linha para a esquerda
            if self.dentro_tabuleiro(l,c-col) == True and self.ver_lampadas(l, c - col) == False:
                if t[l][c-col] == 'o':
                    t[l][c-col] = '-'
                elif t[l][c-col] in lista_restricoes:
                    break
            elif self.ver_lampadas(l, c - col) == True:
                continue

        for col in range(1,self.linhas+1): # percorre a linha para direita
            if self.dentro_tabuleiro(l,c+col) == True and self.ver_lampadas (l, c + col) == False:
                if t[l][c+col]=='o':
                    t[l][c+col]='-'
                elif t[l][c+col] in lista_restricoes:
                    break
            elif self.ver_lampadas (l, c + col) == True:
                continue

        for lin in range(1,self.colunas+1): # percorre coluna para cima
            if self.dentro_tabuleiro(l-lin,c) == True and self.ver_lampadas(l - lin, c) == False:
                if t[l-lin][c]=='o':
                    t[l-lin][c] = "-"
                elif t[l-lin][c] in lista_restricoes:
                    break
            elif self.ver_lampadas(l - lin, c) == True:
                continue

        for lin in range(1,self.colunas+1): # percorre coluna para baixo
            if self.dentro_tabuleiro(l+lin,c) == True and self.ver_lampadas(l + lin, c) == False:
                if t[l+lin][c]=='o':
                    t[l+lin][c] = "-"
                elif t[l+lin][c] in lista_restricoes:
                    break
            elif self.ver_lampadas(l + lin, c) == True:
                continue
    

    def coloca(self,l,c): # já vem comprovado que está dentro do tabuleiro
        '''
        Coloca uma lampada na casa atual
        :param l: linha correspondente a casa atual
        :param c: coluna correspondente a casa atual
        :param g: g apenas é diferente de "F" quando se chama este modulo para gerar um tabuleiro
        '''
        t = self.tabuleiro
        casa = t[l][c]
        colocada = False
        comprovado = self.ver_lampadas(l,c)  # comprovar se não existe nenhuma lampada
        possivel = self.vizinhanca(l, c)
        if casa == "-" and comprovado == False and possivel == True: #and self.vizinhanca == True:   #Apenas pode colocar simbolos quando a casa atual é "."
            # comprovar que não existe nenhuma lampada na linha e coluna.
            t[l][c] = "@"
            colocada = True
            self.iluminar(l,c)
        return colocada


    
    def lampada_obrigatoria(self):
        '''Precorre a matriz e comprova se um determinado ponto apenas pode ser iluminado se uma casa estiver com lampada'''
        t=self.tabuleiro
        for lin in range (self.colunas):
            for col in range (self.linhas):
                if t[lin][col] == '.':
                    if self.ver_casa_vazia(lin,col) != False:
                        coordenada=self.ver_casa_vazia(lin,col)[0]
                        self.coloca(coordenada[0],coordenada[1])
                else:
                    continue       

    
    def ver_casa_vazia(self,l,c):
        '''
        Verifica quantas casas vazias existem na mesma linha e coluna da casa com um ponto
        :param l: linha da casa
        :param c: coluna da casa
        '''
        t = self.tabuleiro
        encontrada = False
        lista_coordenadas=[]
        lista_restricoes = ['0', '1', '2', '3', '4', 'x']
        for col in range(self.linhas): # percorre a linha para esquerda
            if self.dentro_tabuleiro(l,c-col):
                if t[l][c-col ] == '-':
                    lista_coordenadas.append((l,c-col))
                #elif t[l][c-col] != "o":
                #    continue
                elif t[l][c-col] in lista_restricoes:
                    break

        for col in range(self.linhas): #percore linha para direita
            if self.dentro_tabuleiro(l,c+col):
                if t[l][c+col]=='-':
                    lista_coordenadas.append((l,c+col))
                #elif t[l][c+col]!="o":
                #    continue
                elif t[l][c+col] in lista_restricoes:
                    break

        for lin in range(self.colunas): # percorre coluna
            if self.dentro_tabuleiro(l-lin,c):
                if t[l-lin][c]=='-':
                    lista_coordenadas.append((l-lin,c))
                #elif t[l-lin][c]!="o":
                #    continue
                elif t[l-lin][c] in lista_restricoes:
                    break

        for lin in range(self.colunas):     
            if self.dentro_tabuleiro(l+lin,c):
                if t[l+lin][c]=='-':
                    lista_coordenadas.append((l+lin,c))
                #elif t[l+lin][c] != "o":
                #    continue
                elif t[l+lin][c] in lista_restricoes:
                    break
        if len(lista_coordenadas)==1:
            return lista_coordenadas
        else:
            return False



    def unica_casa(self):
        t=self.tabuleiro
        for lin in range (self.colunas+1):
            for col in range (self.linhas+1):
                if self.dentro_tabuleiro(lin,col) and t[lin][col] == '-':
                    print('chegou aqui')
                    if self.ver_unica_casa_vazia(lin,col)==False:
                        print('chegou')
                        self.coloca(lin,col)
                else:
                    continue



    def ver_unica_casa_vazia(self,l,c):
        '''
        Verifica quantas casas vazias existem na mesma linha e coluna da casa com um ponto
        :param l: linha da casa
        :param c: coluna da casa
        '''
        t = self.tabuleiro
        encontrada = False
        lista_restricoes = ['0', '1', '2', '3', '4', 'x']
        for col in range(1,self.linhas): # percorre a linha para esquerda
            if self.dentro_tabuleiro(l,c-col):
                if t[l][c-col ] == '-':
                    print('esquerda')
                    print(t[l][c-col ])
                    encontrada=True
                #elif t[l][c-col] != "o":
                #    continue
                elif t[l][c-col] in lista_restricoes:
                    break

        for col in range(1,self.linhas): #percore linha para direita
            if self.dentro_tabuleiro(l,c+col):
                if t[l][c+col]=='-':
                    print('direita')
                    print(t[l][c+col ])
                    encontrada=True
                #elif t[l][c+col]!="o":
                #    continue
                elif t[l][c+col] in lista_restricoes:
                    break

        for lin in range(1,self.colunas): # percorre coluna
            if self.dentro_tabuleiro(l-lin,c):
                if t[l-lin][c]=='-':
                    print('cima')
                    print(t[l-lin][c ])
                    encontrada=True
                #elif t[l-lin][c]!="o":
                #    continue
                elif t[l-lin][c] in lista_restricoes:
                    break

        for lin in range(1,self.colunas):     
            if self.dentro_tabuleiro(l+lin,c):
                if t[l+lin][c]=='-':
                    encontrada=True
                    print('baixo')
                    print(t[l+lin][c ])
                #elif t[l+lin][c] != "o":
                #    continue
                elif t[l+lin][c] in lista_restricoes:
                    break
        return encontrada



    def eliminar_lampada(self, l, c):
        t = self.tabuleiro
        t[l][c] = '-'

        return t

    def undo_jogada (self):
        '''
        Remove o último valor da Stack stack_jogada e mostra o valor do topo
        '''
        '''self.stack_jogada.pop()  # retirar o ultimo tabuleiro de jogo adicionado do histórico
        if not self.stack_jogada.is_empty():  # se o historico não estiver vazio, o tabuleiro anterior passa a ser o novo tabuleiro
            self.tabuleiro = self.stack_jogada.top()
            return True
        else:  # se o historico ficou vazio, o tabuleiro fica uma matriz vazia
            self.tabuleiro = []
            self.colunas = 0
            self.linhas = 0
            return False'''
        try:
            self.stack_jogada.pop()
            self.tabuleiro = self.stack_jogada.top()
        except:
            print('Não há mais jogadas para reverter.')

    def winner(self):
        dim = self.linhas * self.colunas
        t = self.tabuleiro
        count = 0
        winner = False
        for l in t:
            for c in l:
                if c != '-':
                    count += 1
        if count == dim:
            print('Winner')
            winner = True
        else:
            pass
        
        return winner
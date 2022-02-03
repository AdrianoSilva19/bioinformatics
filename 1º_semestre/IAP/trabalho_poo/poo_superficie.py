# -*- coding: utf-8 -*-

f"""
Created on Nov 13 04:38:26 2021 

@author: Adriano Silva
"""

class superficie:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.lista_fig = []
        pass

    def ponto_dentro_sup(self, lin, col, dim):  # função que verifica se os vertices estão dentro da superficie
        (li, ci, lf, cf) = dim  # dimensão da superficie (0,0,altura,largura)
        if lin < li or lin > lf or col < ci or col > cf:  # caso um dos vertices for maior que o limite superior e inferior das linhas e colunas, esse vertice está fora da superficie
            return False
        else:
            return True

    def ponto_cruza_fig(self, lin, col,
                        dim):  # função que verifica se o vertice se cruza com os das figuras já existentes
        (li, ci, lf, cf) = dim
        if lin > li and lin < lf and col > ci and col < cf:
            return True
        else:
            return False

    def fig_dentro(self, figura, lin, col):
        dim = (0, 0, self.altura,
               self.largura)  # coordenadas da superficie que correspondem à altura (linha) e largura (coluna)
        if self.ponto_dentro_sup(lin, col, dim) and self.ponto_dentro_sup(lin + figura.altura, col,
                                                                          dim) and self.ponto_dentro_sup(lin,
                                                                                                         col + figura.largura,
                                                                                                         dim) and self.ponto_dentro_sup(
                lin + figura.altura, col + figura.largura, dim):  # verificar se todos os vertices dentro da superficie
            return True
        return False

    def sobrepoe(self, figura, lin, col, fig):
        dim = (fig.lin, fig.col, fig.lin + fig.altura,
               fig.col + fig.largura)  # ( vertice cima esquerda; vertice cima direita, vertice baixo esquerda, vertice baixo direita) da figura que já lá está
        # chamar a ponto dentro com linnha coluna como coordenadas onde queremos inserir, e as coordenadas das que estão inseridas
        if self.ponto_cruza_fig(lin, col, dim) or self.ponto_cruza_fig(lin + figura.altura, col,
                                                                       dim) or self.ponto_cruza_fig(lin,
                                                                                                    col + figura.largura,
                                                                                                    dim) or self.ponto_cruza_fig(
                lin + figura.altura, col + figura.largura, dim):
            return True
        return False

    def fig_nao_sobrepoe(self, figura, lin, col):
        for fig in self.lista_fig:  # para cada figura já colocada temos de ver se as coordenadas da nova figura não se sobrepõe
            if self.sobrepoe(figura, lin, col, fig):
                return False  # basta sobrepor a uma para sair
        return True  # não sobrepoe a nenhuma

    def colocar(self, figura, lin, col):
        # validar se cai dentro da superficie
        if self.fig_dentro(figura, lin, col):
            resultado = True
            if self.fig_nao_sobrepoe(figura, lin,
                                     col):  # caso esteja dentro da superficie temos de validar que não se sobrepõe
                resultado = True
                figura.lin = lin
                figura.col = col
                self.lista_fig.append(figura)
            else:
                resultado = False
        else:
            resultado = False
        if resultado == True:
            return 'Figura colocada com sucesso'
        if resultado == False:
            return 'Figura impossivel de colocar'

    def mover(self, figura, lin, col):  # função retira a figura e volta a colocar com as novas coordenadas
        self.lista_fig.remove(figura)
        self.colocar(figura, lin, col)
        return 'A figura indicada foi movida com sucesso'

    def rodar(self, figura, lin, col):
        # primeiro temos de remover essa figura caso exista na superficie, depois alterar a sua linha pela coluna e mandar colocar outra vez
        self.lista_fig.remove(figura)
        rodou_colocou = False
        figura.rodar_retangulo()
        if self.colocar(figura, lin, col):
            rodou_colocou = True
        return rodou_colocou

    def sup_ocupacao(self):
        soma = 0
        for fig in self.lista_fig:
            soma += fig.area()  # vai buscar a area de cada figura á sua class?
        return soma

    def area(self):
        return self.largura * self.altura

    # função que remove todos as figuras da superficice
    def remover(self):
        self.lista_fig.clear()

    def colocar_auto(self, lista_retang, lista_circ):
        # se colocarmos todos os retangulos alinhados encostados ao lado esquerdo da altura estes cabem todos numa fila
        # os circulos ficam com o restante espaço da superficie junto ao lado direito da altura
        # apenas é necessario rodar os retangulos e apenas quando estes não cabem
        sucesso=False
        for fig in lista_retang:
            for x in range(0, self.altura):
                if self.colocar(fig, x, 0):
                    sucesso = True
                    break
                if not self.colocar(fig, x, 0):
                    if self.rodar(fig, x, 0):
                        sucesso = True
                        break
                if sucesso:
                    break
        for fig in lista_circ:
            for x in range(0, self.altura):
                if self.colocar(fig, x, 400):
                    sucesso = True
                    break
                if sucesso:
                    break
        return len(self.lista_fig)

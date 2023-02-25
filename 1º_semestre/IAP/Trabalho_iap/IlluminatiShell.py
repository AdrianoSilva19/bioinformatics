# -*- coding:utf-8 -*-

from cmd import Cmd
from IlluminatiWindow import IlluminatiWindow
from IlluminatiEngine import IlluminatiEngine
import copy

class IlluminatiShell(Cmd):
    intro = 'Illuminati shell.   Escreva help ou ? para listar os comandos.\n'
    prompt = 'Illuminati> '
    
    def do_mostrar(self, arg):
        " -  comando mostrar que leva como parâmetro o nome de um ficheiro..: mr <nome_ficheiro> \n" \
        " -  opcionalmente pode colocar um segundo parametro com o tamanho da casa..: mr <nome_ficheiro> <tamanho>\n" 
        lista_arg = arg.split()
        try:
            lista_arg = arg.split()
            eng.ler_tabuleiro_ficheiro(lista_arg[0])
            global janela  # pois pretendo atribuir um valor a um identificador global
            if janela is not None:
                del janela  # invoca o metodo destruidor de instancia __del__()
            janela = IlluminatiWindow(40, eng.getlinhas(), eng.getcolunas())
            janela.mostraJanela(eng.gettabuleiro())
        except:
            print("Erro: ao mostrar o puzzle")
                          
    def do_carregar(self, arg):
        " -  comando carregar que leva como parâmetro o nome de um ficheiro..: cr <nome_ficheiro> \n"
        '''
        Comando que serve para carregar um puzzle para a memória.
        '''
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 1: #se receber apenas um argumento
                eng.ler_tabuleiro_ficheiro(lista_arg[0])
                tab = copy.deepcopy (eng.gettabuleiro()) #faz uma copia do tabuleiro na memória
                eng.jogada (tab) #guarda o tabuleiro inicial na stack
                eng.printpuzzle()
            else:
                print('Número de argumentos inválido')
        except:
            print('Erro: não foi possivel carregar o puzzle')
        self.ver_auto()
       
    def do_gravar (self, arg):
        " -  comando gravar que leva como parâmetro o nome de um ficheiro..: gr <nome_ficheiro> \n"
        '''
        Comando que serve para gravar o jogo.
        '''
        try:
            tabuleiro = eng.gettabuleiro()
            ficheiro = open (arg, 'w', encoding = 'utf-8') #gravar o ficheiro com encoding utf-8
            linhas = len(tabuleiro)
            colunas = len(tabuleiro[0])
            ficheiro.write (str(linhas) + ' ' + str(colunas)) #a primeira linha do ficheiro corresponde ao numero de linhas e colunas
            ficheiro.write ('\n')
            for linha in tabuleiro: #guarda cada elemento de uma linha separado por espaços e as linhas separadas por \n
                for coluna in linha:
                    ficheiro.write(str(coluna))
                    ficheiro.write(' ')
                ficheiro.write('\n')
        except IOError as error:
            print('Erro: Falha ao gravar o puzzle.', error)
        else:
            print('O seu puzzle foi gravado com sucesso')
            ficheiro.close() #fechar o ficheiro que foi escrito, importante

    def do_jogar(self, arg):
        " -  comando jogar que leva como parâmetro dois inteiros indicando linha e coluna..: jogar <linha> <coluna> \n"
        '''
        Comando que joga uma lampada na linha e coluna pretendida
        '''
        try:
            tabuleiro = eng.gettabuleiro()
            linhas = int(eng.getlinhas())
            colunas = int(eng.getcolunas())
            jogada = False
            lista_arg = arg.split(' ') #separa os argumentos para poderem ser lidos
            pontos_possiveis = eng.pontos(linhas, colunas) #chama uma função 'possivel' do Engine que verifica quais são as casas que não estão vazias
            if len(lista_arg) != 2:
                print('Quantidade inválida de argumentos')
            else:
                simbolo = '@' #simbolo de lampada a inserir
                l = int(lista_arg[0]) - 1 #linha onde colocar lampada
                c = int(lista_arg[1]) - 1 #coluna onde colocar lampada
                if (l, c) in pontos_possiveis: #verificar se o tuplo linha,coluna se encontra bloqueado ou não
                    if tabuleiro[l][c] == '@':
                        eng.eliminar_lampada(l, c)
                        eng.desiluminar(l, c)
                    else:
                        print('Casa bloqueada')
                else:
                    dentro = eng.dentro_tabuleiro(l, c) #verifica se está dentro do tabuleiro a casa escolhida
                    if not dentro:
                        print('Casa fora dos limites do tabuleiro!')
                    else:
                        coloca = eng.coloca(l, c)
                        if coloca:
                            eng.settabuleiro (simbolo, l, c)
                            jogada = True
                        else:
                            print('Não colocada')

            if jogada == True:
                eng.printpuzzle()
                # self.do_ver()
                tab = copy.deepcopy(tabuleiro) #guarda o tabuleiro na memoria
                eng.jogada(tab) #guarda a jogada para mais tarde, se quiser, reverter com o comando undo
                eng.winner()
            else:
                eng.printpuzzle()
        except:
            print('Erro: não foi possível efetuar a sua jogada!')

        self.ver_auto()
    
    
    def do_est1(self, arg):
        " -  comando que coloca as lampadas há volta de casas com restrições certas \n"
        eng.colocar_auto()
        self.ver_auto()
        eng.printpuzzle()
    
    
    def do_est3(self, arg):
        " -  comando que ilumina casas que não podem de alguma forma levar uma lampada \n"
        casas_vazias=eng.casas_bloqueadas()
        self.ver_auto()
        eng.printpuzzle()

    def do_est4(self, arg):
        " -  comando que implementa um passo da estratégia 4 \n" 
        
        

        
        pass
    
    def do_est5(self, arg):
        " -  comando que implementa um passo da estratégia 5 \n" 
        eng.lampada_obrigatoria()
        self.ver_auto()
        eng.printpuzzle()
    
    def do_est6(self, arg):
        " -  comando que implementa um passo da estratégia 5 \n" 
        eng.unica_casa()
        self.ver_auto()
        eng.printpuzzle()
    
    def do_undo(self, arg):
        " -  comando para retroceder as jogadas: undo \n" 
        '''
        Comando que serve para refazer a ultima jogada retrocedendo.
        '''
        try:
            eng.undo_jogada()
            eng.printpuzzle()
        except:
            print('Não foi possível reverter a jogada.')
        self.ver_auto()
 
    def do_resolve(self, arg):
        " -  comando para resolver automaticamente o puzzle \n"        
        pass

    def ver_auto (self):
        " -  comando para ver o puzzle em ambiente gráfico \n"
        '''
        Comando que serve para ver o tabuleiro no estado de jogo atual em ambiente gráfico
        '''
        try:
            global janela
            if janela is not None:
                del janela
            janela = IlluminatiWindow(40, eng.getlinhas(), eng.getcolunas())
            janela.mostraJanela(eng.gettabuleiro())
        except:
            print('Erro: não foi possível mostrar o puzzle')

    def do_ver (self, arg):
        " -  comando para ver o puzzle em ambiente gráfico \n"
        '''
        Comando que serve para ver o tabuleiro no estado de jogo atual em ambiente gráfico
        '''
        try:
            global janela
            if janela is not None:
                del janela
            janela = IlluminatiWindow(40, eng.getlinhas(), eng.getcolunas())
            janela.mostraJanela(eng.gettabuleiro())
        except:
            print('Erro: não foi possível mostrar o puzzle')

    def do_quit(self, arg):
        "Sair do Illuminati: quit"
        '''
        Comando que permite ao user sair do jogo
        '''
        print('Obrigado por ter utilizado o Illuminati, espero que se tenha divertido!')
        return True




if __name__ == '__main__':
    eng = IlluminatiEngine()
    janela = None
    sh = IlluminatiShell()
    sh.cmdloop()

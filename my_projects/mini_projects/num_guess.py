# adivinhar um numero entre 0 e 100
# 10 tentativas
# o jogo dar dicas se é acima ou abaixo
# contar as tentativas, descontar 10 por cada tentativa a pontuacao inicial de 100

import random

class GUESS_NUM:
    def __init__(self):
        self.numero=0
        self.adivinha=0
        self.tentativas=1
        pass
    

    def jogar(self):
        self.numero= random.randint(0,100)
        self.comprovar()
        self.check()

    def comprovar(self):
        self.adivinha=int(input('Primeira tentativa: '))
        self.acima_abaixo(self.adivinha)
        while self.tentativas<10 and self.numero != self.adivinha:
            self.adivinha=int(input(f'Tentativa {self.tentativas + 1}: '))
            self.tentativas+=1
            self.acima_abaixo(self.adivinha)
        
    def check(self):
        if self.tentativas==10 and self.numero != self.adivinha:
            print('\nGastaste todas as tentativas!!\nNão levas pontuação.')
        if self.numero==self.adivinha:
            print(f'\nParabens adivinhaste o numero!!!!! \nA sua pontuação foi de {100-(self.tentativas*10)} pontos')


    def acima_abaixo(self,adivinha):
        '''funcao que indica se a adivinha é inferior ou superior ao numero '''
        if adivinha > self.numero:
            print('Tente com um numero menor.')
        if adivinha < self.numero:
            print('Tente com um numero maior.')


from cmd import Cmd
import num_guess as x


class Mini_GameShell(Cmd):
    intro = 'Mini Games shell.   Escreva help ou ? para listar os comandos.\n'
    prompt = 'Mini Games> '

    def do_jogar(self, arg):
        "Comando que permite escolher o jogo que quer jogar, selecione uma das opções.\nOpções: num_guess, hang_man "
        if arg == "num_guess":   
            jogo=x.GUESS_NUM()
            jogo.jogar()
        if arg == "hang_man":
            pass

    def do_quit(self, arg):
        "Sair da Sala de jogos: quit"
        '''
        Comando que permite ao user sair do jogo
        '''
        print('É o que É!!!!')
        return True

if __name__ == '__main__':
    sh = Mini_GameShell()
    sh.cmdloop()

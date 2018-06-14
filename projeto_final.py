import time, os

class Partida:
    def __init__(self):

        self.tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

        self.player = 'X'

        self.PlayerVSPlayer()

    def Imprime(self):
        print("")
        print("\t\t      |     |     ")
        print("\t\t   {}  |  {}  |  {} ".format(self.tabuleiro[6], self.tabuleiro[7], self.tabuleiro[8]))
        print("\t\t _____|_____|_____")
        print("\t\t      |     |     ")
        print("\t\t   {}  |  {}  |  {} ".format (self.tabuleiro[3], self.tabuleiro[4], self.tabuleiro[5]))
        print("\t\t _____|_____|_____")
        print("\t\t      |     |     ")
        print("\t\t   {}  |  {}  |  {} ".format(self.tabuleiro[0], self.tabuleiro[1], self.tabuleiro[2]))
        print("\t\t      |     |     ")
        print("")

    def CondVitoria(self):
        # checa linhas
        for i in range(3):
            if len(set(self.tabuleiro[i * 3:i * 3 + 3])) is 1 and self.tabuleiro[i * 3] is not '-': return True
        # checa colunas
        for i in range(3):
            if (self.tabuleiro[i] is self.tabuleiro[i + 3]) and (self.tabuleiro[i] is self.tabuleiro[i + 6]) and self.tabuleiro[i] is not '-':
                return True
        # checa diagonais
        if self.tabuleiro[0] is self.tabuleiro[4] and self.tabuleiro[4] is self.tabuleiro[8] and self.tabuleiro[4] is not '-':
            return True
        if self.tabuleiro[2] is self.tabuleiro[4] and self.tabuleiro[4] is self.tabuleiro[6] and self.tabuleiro[4] is not '-':
            return True
        return False


    def ProximaJogada(self, proximojogador):

        if len(set(self.tabuleiro)) == 1: return 0, 4

        self.proximojogador = 'X' if self.player == 'O' else 'O'
        if self.CondVitoria():
            if self.player is 'X':
                return -1, -1
            else:
                return 1, -1
        res_list = []  # lista com os resultados
        c = self.tabuleiro.count('-')  # contador de espaços vazios
        if c is 0:
            return 0, -1
        _list = []  # list com as posições onde '-' aparece
        for i in range(len(self.tabuleiro)):
            if self.tabuleiro[i] == '-':
                _list.append(i)
        for i in _list:
            self.tabuleiro[i] = self.player
            ret, move = self.ProximaJogada(proximojogador)
            res_list.append(ret)
            self.tabuleiro[i] = '-'
        if self.player is 'X':
            maxele = max(res_list)
            return maxele, _list[res_list.index(maxele)]
        else:
            minele = min(res_list)
            return minele, _list[res_list.index(minele)]


    def PlayerVSPlayer(self):

        self.Imprime()
        while True:
            while True:
                try:

                    self.jogada = int(input('Jogador com o {}, digite a sua jogada:'.format( self.player)))
                    if self.jogada <= 9:
                        self.WaitClear(2)
                        break
                    else:
                        print('\033[31mValor invalido! Tente novamente\033[m')
                        continue
                except ValueError:
                    print("\033[31mValor Invalido!\033[m")

            if self.tabuleiro[self.jogada - 1] == '-':
                self.tabuleiro[self.jogada - 1] = self.player
                self.Imprime()

            else:
                print('\033[31mJogada invalida, casa ocupada, tente novamente\033[m')
                self.WaitClear(2)
                continue

            self.vitoria = self.CondVitoria()

            if self.vitoria:
                if self.player == 'O':
                    print("\033[35mO jogador com a 'O' ganhou!\033[m\n\n\n")
                else:
                    print("\033[35mO jogador com o 'X' ganhou!\033[m\n\n\n")
                break

            if self.player == 'X':
                self.player = 'O'

            else:
                self.player = 'X'

            if self.tabuleiro.count('-') == 0 and self.vitoria == False:
                print('\033[35mDeu empate!!!\033[m\n\n\n\n')
                break

    def WaitClear(self, sleep_time):
        time.sleep(sleep_time)
        os.system("clear")

#classe de controle
class Menu:

    def __init__(self):
        self.m = {'1': self.Comandos,
                  '2': self.Iniciar,
                  '3': self.Exit}

        self.EXIT = '3'

        self.Control()

    def Iniciar(self):

        self.Partida = Partida()

    def Comandos(self):

        self.WaitClear(4)
        print("")
        print("Esse jogo trata-se de um \033[4;34mjogo da velha\033[m de dois players")
        self.WaitClear(4)
        print('Jogue usando as posicoes do seu teclado: ')
        print("")
        print("\t\t      |     |     ")
        print("\t\t   7  |  8  |  9  ")
        print("\t\t _____|_____|_____")
        print("\t\t      |     |     ")
        print("\t\t   4  |  5  |  6  ")
        print("\t\t _____|_____|_____")
        print("\t\t      |     |     ")
        print("\t\t   1  |  2  |  3  ")
        print("\t\t      |     |     ")

        self.WaitClear(4)

    def Exit(self):
        print("\033[31mBYE BYE!\033[31m")

    def Show(self):
        print('\033[4;30;44mBEM VINDO AO JOGO DA VELHA!!!\033[m')
        option = input("1. Comandos \n" +
                       "2. Jogar \n" +
                       "3. Sair \n")
        return option

    def Control(self):
        option = self.Show()

        while option != self.EXIT:
            try:

                self.m[option]()

            except KeyError:
                print("\033[31mOPCAO INVALIDA!!\033[m")
                self.WaitClear(3)

            option = self.Show()

        self.Exit()

    def WaitClear(self, sleep_time):
        time.sleep(sleep_time)
        os.system("clear")

if __name__ == '__main__':
    Menu()
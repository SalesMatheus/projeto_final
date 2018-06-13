def imprime(tabuleiro):
    print("")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format (tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print("\t\t      |     |     ")
    print("")

def CondVitoria(tabuleiro):
    # checa linhas
    for i in range(3):
        if len(set(tabuleiro[i * 3:i * 3 + 3])) is 1 and tabuleiro[i * 3] is not '-': return True
    # checa colunas
    for i in range(3):
        if (tabuleiro[i] is tabuleiro[i + 3]) and (tabuleiro[i] is tabuleiro[i + 6]) and tabuleiro[i] is not '-':
            return True
    # checa diagonais
    if tabuleiro[0] is tabuleiro[4] and tabuleiro[4] is tabuleiro[8] and tabuleiro[4] is not '-':
        return True
    if tabuleiro[2] is tabuleiro[4] and tabuleiro[4] is tabuleiro[6] and tabuleiro[4] is not '-':
        return True
    return False


def proximaJogada(tabuleiro, player):
    if len(set(tabuleiro)) == 1: return 0, 4

    proximoJogador = 'X' if player == 'O' else 'O'
    if CondVitoria(tabuleiro):
        if player is 'X':
            return -1, -1
        else:
            return 1, -1
    res_list = []  # lista com os resultados
    c = tabuleiro.count('-')  # contador de espaços vazios
    if c is 0:
        return 0, -1
    _list = []  # list com as posições onde '-' aparece
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == '-':
            _list.append(i)
    for i in _list:
        tabuleiro[i] = player
        ret, move = proximaJogada(tabuleiro, proximoJogador)
        res_list.append(ret)
        tabuleiro[i] = '-'
    if player is 'X':
        maxele = max(res_list)
        return maxele, _list[res_list.index(maxele)]
    else:
        minele = min(res_list)
        return minele, _list[res_list.index(minele)]

def PlayerVSPlayer(player, tabuleiro):
    imprime(tabuleiro)
    while True:
        while True:
            try:
                jogada = int(input('Jogador com o {}, digite a sua jogada:'.format(player)))
                if jogada <= 9:
                    break
                else:
                    print('Valor invalido! Tente novamente')
                    continue
            except ValueError:
                print("Valor Inválido!")

        if tabuleiro[jogada - 1] == '-':
            tabuleiro[jogada - 1] = player
            imprime(tabuleiro)

        else:
            print('Jogada invalida, casa ocupada, tente novamente\n')
            continue

        vitoria = CondVitoria(tabuleiro)

        if vitoria == True:
            if player == 'O':
                print("O jogador com o a 'O' ganhou!")
            else:
                print("O jogador com o 'X' ganhou!")
            break

        if player == 'X':
            player = 'O'

        else:
            player = 'X'

        if tabuleiro.count('-') == 0 and vitoria == False:
            print('Deu empate!!!\n')
            break

def menu():
    player = 'X'
    print("")
    print('\t\tJogue usando as posicoes: ')
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
    print("")
    print('\t\tE as letras X e O\n')
    #time.sleep(1)

    while True:
        tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        escolha = input(
            'Escolha um modo de jogo:\n1 - Jogar\n2 - Nao fazer nada\n3 - Sair\n\n')
        if escolha == '1':
            PlayerVSPlayer(player, tabuleiro)
        elif escolha == '2':
            pass
        elif escolha == '3':
            print('Fim de jogo')
            #time.sleep(1)
            print('Adeus!!!')
            quit()
        else:
            print('Opcao invalida!\n')
            continue


menu()def imprime(tabuleiro):
    print("")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format (tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   {}  |  {}  |  {} ".format(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print("\t\t      |     |     ")
    print("")

def CondVitoria(tabuleiro):
    # checa linhas
    for i in range(3):
        if len(set(tabuleiro[i * 3:i * 3 + 3])) is 1 and tabuleiro[i * 3] is not '-': return True
    # checa colunas
    for i in range(3):
        if (tabuleiro[i] is tabuleiro[i + 3]) and (tabuleiro[i] is tabuleiro[i + 6]) and tabuleiro[i] is not '-':
            return True
    # checa diagonais
    if tabuleiro[0] is tabuleiro[4] and tabuleiro[4] is tabuleiro[8] and tabuleiro[4] is not '-':
        return True
    if tabuleiro[2] is tabuleiro[4] and tabuleiro[4] is tabuleiro[6] and tabuleiro[4] is not '-':
        return True
    return False


def proximaJogada(tabuleiro, player):
    if len(set(tabuleiro)) == 1: return 0, 4

    proximoJogador = 'X' if player == 'O' else 'O'
    if CondVitoria(tabuleiro):
        if player is 'X':
            return -1, -1
        else:
            return 1, -1
    res_list = []  # lista com os resultados
    c = tabuleiro.count('-')  # contador de espaços vazios
    if c is 0:
        return 0, -1
    _list = []  # list com as posições onde '-' aparece
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == '-':
            _list.append(i)
    for i in _list:
        tabuleiro[i] = player
        ret, move = proximaJogada(tabuleiro, proximoJogador)
        res_list.append(ret)
        tabuleiro[i] = '-'
    if player is 'X':
        maxele = max(res_list)
        return maxele, _list[res_list.index(maxele)]
    else:
        minele = min(res_list)
        return minele, _list[res_list.index(minele)]

def PlayerVSPlayer(player, tabuleiro):
    imprime(tabuleiro)
    while True:
        while True:
            try:
                jogada = int(input('Jogador com o {}, digite a sua jogada:'.format(player)))
                if jogada <= 9:
                    break
                else:
                    print('Valor invalido! Tente novamente')
                    continue
            except ValueError:
                print("Valor Inválido!")

        if tabuleiro[jogada - 1] == '-':
            tabuleiro[jogada - 1] = player
            imprime(tabuleiro)

        else:
            print('Jogada invalida, casa ocupada, tente novamente\n')
            continue

        vitoria = CondVitoria(tabuleiro)

        if vitoria == True:
            if player == 'O':
                print("O jogador com o a 'O' ganhou!")
            else:
                print("O jogador com o 'X' ganhou!")
            break

        if player == 'X':
            player = 'O'

        else:
            player = 'X'

        if tabuleiro.count('-') == 0 and vitoria == False:
            print('Deu empate!!!\n')
            break

def menu():
    player = 'X'
    print("")
    print('\t\tJogue usando as posicoes: ')
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
    print("")
    print('\t\tE as letras X e O\n')
    #time.sleep(1)

    while True:
        tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        escolha = input(
            'Escolha um modo de jogo:\n1 - Jogar\n2 - Nao fazer nada\n3 - Sair\n\n')
        if escolha == '1':
            PlayerVSPlayer(player, tabuleiro)
        elif escolha == '2':
            pass
        elif escolha == '3':
            print('Fim de jogo')
            #time.sleep(1)
            print('Adeus!!!')
            quit()
        else:
            print('Opcao invalida!\n')
            continue


menu()
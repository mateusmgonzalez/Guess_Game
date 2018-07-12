import random

#-------------------------------------------------------------------------------
# Funções utilizadas pelo programa 
#-------------------------------------------------------------------------------

# função que verifica filas com fechamento iminente.
# caso não encontre uma:
#      retorna zero
# caso contrário:
#      retorna a casa que bloqueia o fechamento
#-------------------------------------------------------------------------------
def fechamentoIminente(oponente):
    global pesosFilas

    if oponente == 'X': jogador = 'O'
    else:               jogador = 'X'
    
    # verifica fechamento iminente nas linhas
    # e retorna a casa que bloqueia o fechamento
    for linha in lins:
        if linha.count(oponente) == 2 and linha.count(jogador) == 0:
            lin_idx = lins.index(linha) + 1
            col_idx = linha.index(' ') + 1
            casa = lin_idx*10 + col_idx
            # pesosFilas[casa][0] = 0
            return casa

    # verifica fechamento iminente nas colunas e
    # retorna casa que bloqueia o fechamento
    for coluna in cols:
        if coluna.count(oponente) == 2 and coluna.count(jogador) == 0:
            lin_idx = coluna.index(' ') + 1
            col_idx = cols.index(coluna) + 1
            casa = lin_idx*10 + col_idx
            # pesosFilas[casa][0] = 0
            return casa

    # verifica fechamento iminente nas diagonais e
    # retorna casa que bloqueia o fechamento
    for diagonal in dgns:
        if diagonal.count(oponente) == 2 and diagonal.count(jogador) == 0:
            dgn_idx = dgns.index(diagonal) + 1
            lin_idx = diagonal.index(' ') + 1
            if dgn_idx == 1:
                col_idx = lin_idx
            else:
                col_idx = 4 - lin_idx
            casa = lin_idx*10 + col_idx
            # pesosFilas[casa][0] = 0
            return casa

    # retorna zero se não houver fechamento iminente
    return 0

def reponderaTabuleiro():
    global pesosFilas
    
    for casa in casasDisponíveis:
        peso  = pesosFilas[casa][0]
        filas = pesosFilas[casa][1]
        for fila in filas:
            if 'X' in fila: pesosFilas[casa][0] = peso - 1

# função que seleciona a melhor casa para jogada do computador
#-------------------------------------------------------------------------------
def melhorCasa():
    # procura casa do tabuleiro com o maior peso
    maiorPeso = 0
    for casa in casasDisponíveis:
        peso  = pesosFilas[casa][0]
        if peso > maiorPeso: maiorPeso = peso
    pesosFilas[casa][0] = maiorPeso
    return casa
    
# função que atualiza a estrutura de dados que representa as filas de fechamento
#-------------------------------------------------------------------------------
def atualizaFilas():
    global lins, cols, dgns
    
    lins = [linha for linha in tabuleiro]

    cols = [
            [tabuleiro[linha][0] for linha in range(3)], \
            [tabuleiro[linha][1] for linha in range(3)], \
            [tabuleiro[linha][2] for linha in range(3)]  \
           ]

    dgns = [
            [tabuleiro[linha][linha]  for linha in range(3)],
            [tabuleiro[linha][coluna] for linha in range(3)
                                          for coluna in range(3)
                                              if (linha+coluna) == 2]
           ]

    return(lins + cols + dgns)
# função que apresenta jogo ao usuário
#-------------------------------------------------------------------------------
def apresentaJogo():
    print(2*'\n')
    print('Nesta implementação do Jogo da Velha, as casas do tabuleiro são numeradas da seguinte forma: \n\n' \
          ' 11 | 12 | 13 \n' \
          '----+----+----\n' \
          ' 21 | 22 | 23 \n' \
          '----+----+----\n' \
          ' 31 | 32 | 33 \n')
    print('Ao fazer seu lance, indique em qual dessas casas você quer jogar.')
    
# função que exibe o tabuleiro
#-------------------------------------------------------------------------------
def exibeTabuleiro():
    print()
    print(' ' + tabuleiro[0][0] + ' |' + ' ' + tabuleiro[0][1] + ' |' + ' ' + tabuleiro[0][2] + ' \n' \
          '---+---+---\n' \
          ' ' + tabuleiro[1][0] + ' |' + ' ' + tabuleiro[1][1] + ' |' + ' ' + tabuleiro[1][2] + ' \n' \
          '---+---+---\n' \
          ' ' + tabuleiro[2][0] + ' |' + ' ' + tabuleiro[2][1] + ' |' + ' ' + tabuleiro[2][2] + ' \n' )
    
# função que verifica o fechamento do jogo
#-------------------------------------------------------------------------------
def verificaFechamento():

    # atualiza a estrutura de dados que representa as filas de fechamento
    filas = atualizaFilas()

    # seta indicador de fechamento
    for fila in filas:
        if fila in fechamentos:
            status = True
            break
    else: status = False

    return status

# função que obtém e processa lance do jogador
#-------------------------------------------------------------------------------
def processaLanceJogador():
    global jogada, tabuleiro, pesos

    # contabiliza jogada do jogador
    jogada += 1

    # exibe lista de casas disponíveis
    #print('\nNo momento, o tabuleiro está com as seguintes casas disponíveis:\n', \
    #     casasDisponíveis, '\n')

    # obtém lance do jogador
    while True:
        try:
            casa = int(input('Em qual delas você quer jogar? '))
            if casa not in casasDisponíveis:
                raise ValueError
            else:
                # elimina casa escolhida da relação das casas disponíveis
                casasDisponíveis.remove(casa)
                break
        except ValueError:
            print('Você digitou um valor inválido ou uma casa já ocupada. Tente novamente.\n')

    # atualiza tabuleiro
    tabuleiro[casa//10-1][casa%10-1] = 'X'

# função que obtém lance do computador
#-------------------------------------------------------------------------------
def processaLanceComputador():
    global jogada, filas
    
    # contabiliza jogada do computador
    jogada += 1
    # verifica fechamento iminente do computador
    casa = fechamentoIminente('O')
    # verifica fechamento iminente do jogador
    if casa == 0:
        casa = fechamentoIminente('X')
    # se não fechou, escolhe casa com maior peso
    if casa == 0:
        casa = melhorCasa()
    # elimina casa escolhida da relação das casas disponíveis
    casasDisponíveis.remove(casa)
    # atualiza tabuleiro
    tabuleiro[casa//10-1][casa%10-1] = 'O'

#-------------------------------------------------------------------------------
# Corpo do programa
#-------------------------------------------------------------------------------

def main():
    global tabuleiro, fechamentos, casasDisponíveis, pesosFilas, jogada, fechou, terminar
    # inicializa a estrutura de dados que representa o tabuleiro
    tabuleiro = [[' ']*3, [' ']*3, [' ']*3]

    # inicializa a estrutura de dados que representa os padrões de fechamento
    fechamentos = [3*['X'], 3*['O']]

    # cria lista de casas disponíveis para lance
    casasDisponíveis = [i*10+j for i in range(1,4) \
                                   for j in range(1,4)]

    # inicializa e atualiza as filas
    atualizaFilas()
    # inicializa a estrutura de dados que contém os pesos iniciais de cada casa
    pesosFilas = { 11: [3, [lins[0], cols[0], dgns[0]]],
                   12: [2, [lins[0], cols[1]]],
                   13: [3, [lins[0], cols[2], dgns[1]]],
                   21: [2, [lins[1], cols[0]]],
                   22: [4, [lins[1], cols[1], dgns[0], dgns[1]]],
                   23: [2, [lins[1], cols[2]]],
                   31: [3, [lins[2], cols[0], dgns[1]]],
                   32: [2, [lins[2], cols[1]]],
                   33: [3, [lins[2], cols[2], dgns[0]]]
                 }

    # seta a condição de encerramento do jogo
    jogada, fechou = 0, False
    terminar = (jogada == 9) or (fechou == True)

    # apresenta jogo ao jogador
    apresentaJogo()

    # enquanto não terminar
    while (not terminar):
        # processa jogada do jogador
        processaLanceJogador()
        # verifica Fechamento
        fechou = verificaFechamento()
        # atualiza sinalizador de encerramento do jogo
        terminar = (jogada == 9) or fechou == True
        # se for para terminar:
        if terminar:
            # exibe tabuleiro
            exibeTabuleiro()
            # termina o jogo
            break
        # atualiza pesos das casas do tabuleiro
        pesos = reponderaTabuleiro()
        # processa jogada do computador
        processaLanceComputador()
        # verifica Fechamento
        fechou = verificaFechamento()
        # atualiza sinalizador de encerramento do jogo
        terminar = (jogada == 9) or fechou == True
        # exibe tabuleiro
        exibeTabuleiro()

    # em caso de fechamento, verifica vencedor e emite mensagem correspondente:
    if fechou:
       # se o vencedor for o jogador:
        if jogada in [1, 3, 5, 7, 9]:
           # emite mensagem de congratulação:
            print('Parabéns, você venceu!')
       # se o vencedor for o computador:
        else:
           # emite mensagem de zoação:
            print('Você é um pato!')
    # se a partida não fechou, emite mensagem de empate
    else:
        print('Deu velha !')

main()

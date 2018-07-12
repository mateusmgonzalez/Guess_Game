import random

#-------------------------------------------------------------------------------
# Funções utilizadas pelo programa 
#-------------------------------------------------------------------------------

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

    # seta indicador de fechamento
    for fila in filas:
        if fila in fechamentos:
            status = True
            break
    else:
        status = False

    return status

# função que obtém e processa lance do jogador
#-------------------------------------------------------------------------------
def processaLanceJogador():
    global filas, jogada, tabuleiro

    # contabiliza jogada do jogador
    jogada += 1

    # exibe lista de casas disponíveis
    print('\nNo momento, o tabuleiro está com as seguintes casas disponíveis:\n', \
          casasDisponíveis, '\n')

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

    # atualiza a estrutura de dados que representa as filas de fechamento
    filas = atualizaFilas()

# função que obtém lance do computador
#-------------------------------------------------------------------------------
def processaLanceComputador():
    global jogada, filas
    
    # contabiliza jogada do computador
    jogada += 1
    # gera lance do computador
    casa = random.choice(casasDisponíveis)
    # elimina casa escolhida da relação das casas disponíveis
    casasDisponíveis.remove(casa)
    # atualiza tabuleiro
    tabuleiro[casa//10-1][casa%10-1] = 'O'
    # atualiza a estrutura de dados que representa as filas de fechamento
    filas = atualizaFilas()

# inicializa a estrutura de dados que representa o tabuleiro
tabuleiro = [[' ']*3, [' ']*3, [' ']*3]

# define e inicializa a estrutura de dados que representa os padrões de fechamento
fechamentos = [3*['X'], 3*['O']]

# cria lista de casas disponíveis para lance
casasDisponíveis = [i*10+j for i in range(1,4) \
                               for j in range(1,4) \
                                   if tabuleiro[i-1][j-1] == ' ']

# inicializa a estrutura de dados que representa as filas de fechamento
filas = atualizaFilas()

# seta a condição de encerramento do jogo
jogada, fechou = 0, False
terminar = (jogada == 9) or (fechou == True)

#-------------------------------------------------------------------------------
# Corpo do programa
#-------------------------------------------------------------------------------
def main():
   # apresenta jogo ao jogador
    apresentaJogo()
    global tabuleiro, fechamentos, casasDisponíveis, pesosFilas, jogada, fechou, terminar
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
       

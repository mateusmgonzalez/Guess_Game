# apresente jogo ao usuário
print('Você tem 10 chances de acertar o número que eu estou pensando.')
print('Trata-se de um valor entre 1 e 100. Então, vamos lá!')
print()

# gere número-alvo entre 1 e 100
from random import randint
alvo = randint(1, 100)
# inicializa indicador de acerto
acertou = False
lista =[]
# repita 10 vezes:
contador = 0
while contador < 10:
          # obtenha palpite do usuário
      while True:
            try:
                  palpite = int(input('Entre o seu palpite: '))
                  for i in range(len(lista)):
                        if palpite == lista[i]:
                              print("Este numero já foi digitado")
                              raise ValueError
                        
                  if palpite < 1 or palpite > 100:
                        raise ValueError
                  break
            except ValueError:
                  print('Palpite inválido. Tente outra vez!')
      
      lista.append(palpite)
      # verificação do palpite
      if contador == 0:    
            if (abs(alvo - palpite) <= 3 and alvo != palpite):
                  print("Muito quente")
            elif (abs(alvo - palpite) >= 4 and abs(alvo - palpite) <= 6):
                  print("Quente")
            elif (abs(alvo - palpite) >= 7 and abs(alvo - palpite) <= 10 ):
                  print("Frio")
            elif (abs(alvo - palpite) > 10):
                  print("Muito Frio")
             
      if contador > 0:
            distancia_anterior = abs(alvo - lista[contador - 1])
            distancia_atual = abs(alvo - lista[contador])
             #o anterior está Fervendo
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                        print("Seu palpite continua muito quente")
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        print( "OOps, seu palpite deu uma esfriada mas ainda está quente")
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        print("OOps, seu palpite agora ficou frio!")
                  else :
                        print("OOps, seu palpite agora ficou muito frio!")
            #o anterior é muito quente
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                        print("Seu palpite continua muito quente")
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        print( "OOps, seu palpite deu uma esfriada mas ainda está quente")
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        print("OOps, seu palpite agora ficou frio!")
                  else :
                        print("OOps, seu palpite agora ficou muito frio!")
            
            #anterior é quente           
            elif (distancia_anterior >= 4 and distancia_anterior <= 6 and alvo != palpite):
                  if(distancia_atual<= 3):
                        print("OOps, seu palpite deu uma esquentada e agora está muito quente!")
                  elif (distancia_atual >= 4 and diatancia_atual <= 6):
                        if (distancia_anterior > distancia_atual):
                              print ("Teu palpite está se aproximando mais continua quente!")
                        else:
                              print( "Seu palpite acabou se afastando, mas continua quente!")
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        print("OOps, seu palpite deu uma esfriada e agora ficou frio!")
                  else :
                        print("OOps, seu palpite agora ficou muito frio!")
             #o anterior é morno
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                        print("Seu palpite continua muito quente")
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        print( "OOps, seu palpite deu uma esfriada mas ainda está quente")
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        print("OOps, seu palpite agora ficou frio!")
                  else :
                        print("OOps, seu palpite agora ficou muito frio!")
            #anterior é frio
            elif (distancia_anterior >= 7 and distancia_anterior <= 10 and alvo != palpite):
                  if(distancia_atual<= 3):
                        print("OOps, seu palpite deu uma esquentada e agora está muito quente!")
                  elif (distancia_atual >= 4 and distancia_atual <= 6):
                        print( "Seu palpite deu uma esquentada e agora está quente!")
                  elif(distancia_atual >= 7 and distancia_atual <= 10 ):
                        if (distancia_anterior > distancia_atual):
                              print ("Teu palpite está se aproximando mais continua frio!")
                        else:
                              print( "Seu palpite acabou se afastando, mas continua frio!")
                        
                  else :
                        print("OOps, seu palpite deu uma esfriada e agora ficou muito frio!")
            #anterior é muito frio
            elif (distancia_anterior > 10 and alvo != palpite):
                  if(distancia_atual <= 3):
                        print("OOps, seu palpite deu uma esquentada e agora está muito quente!")
                  elif (distancia_atual >= 4 and distancia_atual <= 6):
                        print( "Seu palpite deu uma esquentada e agora está quente!")
                  elif(distancia_atual >= 7 and distancia_atual <= 10 ):
                        print("OOps, seu palpite deu uma esquentadinha mas ainda está frio!")
                  else :
                        if (distancia_anterior > distancia_atual):
                              print ("Teu palpite está se aproximando mais continua muito frio!")
                        else:
                              print( "Seu palpite acabou se afastando, mas continua muito frio!")
            if (distancia_anterior < distancia_atual):
                  print( "Está se aproximando")
            else:
                  print("Agora se afastou")
            
                  
      contador = contador + 1
    # se palpite atingiu o alvo:
    #   atualize indicador de acerto
    #   encerre o jogo
    # senão:
    #   comunique erro ao usuário
      if palpite == alvo:
            # atualize indicador de acerto
            acertou = True
            # encerre o jogo
            break
      else:
            # comunique erro ao usuário
            print('Errou! Tente novamente.' \
                  'Você ainda tem ', 10-contador, ' tentativa(s).')
            print(40*'-'+ '\n')
# encerre o jogo
if acertou: # comunique sucesso ao usuário
    print('Parabéns!\n' \
          'Você acertou o número após ', contador, ' tentativa(s).')
else: # comunique fracasso ao usuário
    print('Infelizmente, você fracassou.\n' \
          'O número pensado era: ', alvo, ' \n' \
          'Quem sabe a próxima vez!')
                          
print('Até breve') # emita saudação final

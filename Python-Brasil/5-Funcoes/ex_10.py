# -*- coding: utf-8 -*-
"""
10 - Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador 
lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, 
você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na 
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira 
jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo 
agora é continuar jogando os dados até tirar este número novamente. Você 
perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""

def dados():
    #Função que simula dois dados
    import random as rd

    resultado = int(rd.uniform(1,6))
    return(resultado)


def craps():
    #Função do jogo
    
    print('\n CRAPS!')
    
    parar = 'N'
    jogada = 1
    while(parar == 'N'):
    
        saida = input('\n Aperte qualquer tecla para realizar a {}° jogada \n ... -> '.format(jogada))
        
        #Jogando os dados e verificando os resultados
        dado_01 = dados()
        dado_02 = dados()
        soma_dados = dado_01 + dado_02
        
        if(jogada == 1 and soma_dados in [7, 11]):
            print('Natural')
            print('Você ganhou!!!')
            print('Resultado dos dados: {} e {}'.format(dado_01, dado_02))
            parar = 'S'
        elif(jogada == 1 and soma_dados in [2, 3, 12]):
            print('Craps')
            print('Você perdeu!!!')
            print('Resultado dos dados: {} e {}'.format(dado_01, dado_02))
            parar = 'S'
        elif(soma_dados in [4,5,6,8,9,10]):
            print('Ponto')
            print('Resultado dos dados: {} e {}'.format(dado_01, dado_02))
            primeira_soma = soma_dados
            parar = 'N'
        elif(jogada >= 2 and soma_dados == 7):
            print('Craps')
            print('Você perdeu!!!')
            print('Resultado dos dados: {} e {}'.format(dado_01, dado_02))
            parar = 'S'
        elif(jogada >= 2 and soma_dados == primeira_soma):
            print('Craps')
            print('Você ganhou!!!')
            print('Resultado dos dados: {} e {}'.format(dado_01, dado_02))
            print('Tentativa {} '.format(jogada))
            parar = 'S'
            
        #Incremental da variável jogada
        jogada += 1

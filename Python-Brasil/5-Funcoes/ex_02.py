# -*- coding: utf-8 -*-
"""
2 - Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro 
imprima até a n-ésima linha.
"""
def serie_horizontal(numero):
    #Função que imprime uma lista na horizontal
    
    #Verificando se o conteúdo digitado é um número
    try:
        numero = int(numero)        
    except ValueError:
        print('\n O valor inputado deve ser do tipo inteiro')
    else:
        #Gerando os resultados
        for col in range(1, numero+1):
            print('{} '.format(col), end = '')


def serie_mista(lin):
    #Função que imprime uma lista na vertical
    
    #Verificando se o conteúdo digitado é um número
    try:
        numero = int(lin)        
    except ValueError:
        print('\n O valor inputado deve ser do tipo inteiro')
    else:
        for lin in range(1, lin+1):
            print('')
            serie_horizontal(lin)


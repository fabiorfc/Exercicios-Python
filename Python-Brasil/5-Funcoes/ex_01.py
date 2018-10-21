# -*- coding: utf-8 -*-
"""
1 - Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro 
e imprima até a n-ésima linha.
"""
def serie(numero):
    
    #Verificando se o conteúdo digitado é um número
    try:
        numero = int(numero)        
    except ValueError:
        print('\n O valor inputado deve ser do tipo inteiro')
    else:
        #Gerando os resultados
        for x in range(1, numero+1):
            print('')
            print('{} '.format(x) * x)
    
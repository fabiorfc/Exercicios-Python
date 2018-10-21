# -*- coding: utf-8 -*-
"""
9 - Reverso do número. Faça uma função que retorne o reverso de um número 
inteiro informado. Por exemplo: 127 -> 721.
"""

def reverso(numero):
    #Função que imprime o número reverso do digitado
    
    try:
        numero = int(numero)
    except ValueError:
        print('\n O valor digitado deve ser numérico')
    else:
        numero = str(numero)
        
        numero_invertido = ''
        #Loop para inverter o número digitado
        for x in range(len(numero)-1, -1, -1):
            numero_invertido = numero_invertido + numero[x]
        
        numero_invertido = int(numero_invertido)
        return(numero_invertido)
# -*- coding: utf-8 -*-
"""
8 - Faça uma função que informe a quantidade de dígitos de um determinado 
número inteiro informado.
"""

def qtd_digitos(numero):
    #Função que retorna a quantidade de dígitos que compõe o número inteiro digitado
    
    try:
        numero = int(numero)
    except ValueError:
        print('\n O valor digitado deve ser numérico e inteiro')
    else:
        numero = str(numero)
        dimensao = len(numero)
        return('Número inserido: {}. Quantidade de dígitos: {}'.format(numero,dimensao))
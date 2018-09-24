# -*- coding: utf-8 -*-
"""
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
ou negativo.
"""
valor = float(input('Digite um valor numérico: '))
if( valor < 0  ):
    print('O valor digitado é negativo')
elif( valor > 0 ):
    print('O valor é positivo')
else:
    print('O valor é igual a zero')

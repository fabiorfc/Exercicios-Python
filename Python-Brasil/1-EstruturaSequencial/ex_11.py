# -*- coding: utf-8 -*-
"""
11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e 
mostre:
    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.
"""
#Inputando os dados
inteiro_01 = int(input('Insira o 1° inteiro: '))
inteiro_02 = int(input('Insira o 2° inteiro: '))
real = float(input('Insira o 1° inteiro: '))
#Efetuando os cálculos
calculo_01 = inteiro_01 * inteiro_02
calculo_02 = 3 * inteiro_01 + real
calculo_03 = real ** 3
#Imprimindo o resultado final
print('Cálculo 1: {}'.format(calculo_01))
print('Cálculo 1: {}'.format(calculo_02))
print('Cálculo 1: {}'.format(calculo_03))
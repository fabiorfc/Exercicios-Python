# -*- coding: utf-8 -*-
"""
8 - Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
numero_01 = float(input('Digite o valor da 1° compra: '))
numero_02 = float(input('Digite o valor da 2° compra: '))
numero_03 = float(input('Digite o valor da 3° compra: '))

if(numero_01 == numero_02 == numero_03):
    print('Você pode comprar qualquer um dos 3 produtos')
if(numero_01 == numero_02):
    if(numero_01 < numero_03):
        print('Você deve comprar o primeiro produto')
    else:
        print('Você deve comprar o terceiro produto')
if(numero_01 == numero_03):
    if(numero_01 < numero_02):
        print('Você deve comprar o primeiro produto')
    else:
        print('Você deve comprar o segundo produto')        
if(numero_02 == numero_03):
    if(numero_02 < numero_01):
        print('Você deve comprar o segundo produto')
    else:
        print('Você deve comprar o primeiro produto')        
else:
    if(numero_01 < numero_02 < numero_03):
        print('Você deve comprar o primeiro produto')
    elif(numero_01 < numero_03 < numero_02):
        print('Você deve comprar o primeiro produto')
    elif(numero_02 < numero_01 < numero_03):
        print('Você deve comprar o segundo produto')
    elif(numero_02 < numero_03 < numero_01):
        print('Você deve comprar o segundo produto')
    elif(numero_03 < numero_01 < numero_02):
        print('Você deve comprar o terceiro produto')
    elif(numero_03 < numero_02 < numero_01):
       print('Você deve comprar o terceiro produto')
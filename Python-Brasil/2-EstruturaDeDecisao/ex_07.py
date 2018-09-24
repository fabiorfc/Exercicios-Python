# -*- coding: utf-8 -*-
"""
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero_01 = float(input('Digite o 1° número: '))
numero_02 = float(input('Digite o 2° número: '))
numero_03 = float(input('Digite o 3° número: '))

if(numero_01 == numero_02 == numero_03):
    print('Todos os números são iguais')
if(numero_01 == numero_02):
    if(numero_01 < numero_03):
        print('O maior valor é {}'.format(numero_03))
        print('O menor valor é {}'.format(numero_01))
    else:
        print('O maior valor é {}'.format(numero_01))
        print('O menor valor é {}'.format(numero_03))
if(numero_01 == numero_03):
    if(numero_01 < numero_02):
        print('O maior valor é {}'.format(numero_02))
        print('O menor valor é {}'.format(numero_01))
    else:
        print('O maior valor é {}'.format(numero_01))
        print('O menor valor é {}'.format(numero_02))
if(numero_02 == numero_03):
    if(numero_02 < numero_01):
        print('O maior valor é {}'.format(numero_03))
        print('O menor valor é {}'.format(numero_02))
    else:
        print('O maior valor é {}'.format(numero_02))
        print('O menor valor é {}'.format(numero_03))
else:
    if(numero_01 < numero_02 < numero_03):
        print('O maior valor é {}'.format(numero_03))
        print('O menor valor é {}'.format(numero_01))
    elif(numero_01 < numero_03 < numero_02):
        print('O maior valor é {}'.format(numero_02))
        print('O menor valor é {}'.format(numero_01))
    elif(numero_02 < numero_01 < numero_03):
        print('O maior valor é {}'.format(numero_03))
        print('O menor valor é {}'.format(numero_02))        
    elif(numero_02 < numero_03 < numero_01):
        print('O maior valor é {}'.format(numero_01))
        print('O menor valor é {}'.format(numero_02))        
    elif(numero_03 < numero_01 < numero_02):
        print('O maior valor é {}'.format(numero_02))
        print('O menor valor é {}'.format(numero_03))
    elif(numero_03 < numero_02 < numero_01):
        print('O maior valor é {}'.format(numero_01))
        print('O menor valor é {}'.format(numero_03))
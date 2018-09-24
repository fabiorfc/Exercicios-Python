# -*- coding: utf-8 -*-
"""
6 - Faça um Programa que leia três números e mostre o maior deles.
"""
numero_01 = float(input('Digite o 1° número: '))
numero_02 = float(input('Digite o 2° número: '))
numero_03 = float(input('Digite o 3° número: '))

if(numero_01 >= numero_02):
    if(numero_01 >= numero_03):
        print('O maior número é {}'.format(numero_01))
if(numero_02 >= numero_03):
    if(numero_02 >= numero_01):
        print('O maior número é {}'.format(numero_02))
if(numero_03 >= numero_02):
    if(numero_03 >= numero_01):
        print('O maior número é {}'.format(numero_03))

# -*- coding: utf-8 -*-
"""
1 - Faça um Programa que peça dois números e imprima o maior deles.
"""
numero_01 = float(input('Digite um número qualquer: '))
numero_02 = float(input('Digite outro número qualquer: '))
if ( numero_01 > numero_02 ):
    print('O número de maior valor é o: {}'.format(numero_01))
elif ( numero_01 < numero_02 ):
    print('O número de maior valor é o: {}'.format(numero_02))
else:
    print('Os números digitados são iguais. Seus valores são: {}'.format(numero_01))

# -*- coding: utf-8 -*-
"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
nota_01 = float(input('Digite a 1° nota: '))
nota_02 = float(input('Digite a 2° nota: '))
nota_03 = float(input('Digite a 3° nota: '))
nota_04 = float(input('Digite a 4° nota: '))

media = (nota_01 + nota_02 + nota_03 + nota_04)/4

print('A média obtida foi: {}'.format(media))
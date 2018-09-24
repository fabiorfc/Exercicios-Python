# -*- coding: utf-8 -*-
"""
6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
#import da library
import math
raio = float(input('Digite o valor do raio do círculo: '))
area = math.pi * raio * raio
print('O valor da área é: {}'.format(area))
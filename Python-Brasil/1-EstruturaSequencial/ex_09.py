# -*- coding: utf-8 -*-
"""
9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e 
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""
temperatura_f = float(input('Informe o valor da temperatura em °F: '))
temperatura_c = round(5 * (temperatura_f-32) / 9, 1)
print('O valor da temperatura em °C é: {}'.format(temperatura_c))
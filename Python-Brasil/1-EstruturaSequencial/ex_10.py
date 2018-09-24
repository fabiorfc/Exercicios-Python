# -*- coding: utf-8 -*-
"""
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e
mostre em graus Farenheit.
"""
temperatura_c = float(input('Informe o valor da temperatura em °C: '))
temperatura_f = round((temperatura_c * 9 / 5) + 32, 1)
print('O valor da temperatura em °F é: {}'.format(temperatura_f))
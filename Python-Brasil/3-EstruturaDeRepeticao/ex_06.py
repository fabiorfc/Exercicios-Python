# -*- coding: utf-8 -*-
"""
6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do 
outro. Depois modifique o programa para que ele mostre os números um ao lado 
do outro.
"""
numeros = []
print('Impressão número 1:')
for x in range(0, 20):
    print(x)
    numeros.append(x)
print('Impressão número 2:')
print(numeros)

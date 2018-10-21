# -*- coding: utf-8 -*-
"""
13 - Faça um programa que peça dois números, base e expoente, calcule e mostre 
o primeiro número elevado ao segundo número. Não utilize a função de potência 
da linguagem.
"""
#Coletando os dados
base = float(input('Informe o valor da base: '))
expoente = int(input('Informe o valor do expoente: '))

#Efetuando os cálculos
base_final = base
for x in range(1, expoente):
    base_final = base_final*base
    print('{} elevado a {} = {}'.format(base, expoente, base_final))


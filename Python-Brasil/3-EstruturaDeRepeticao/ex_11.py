# -*- coding: utf-8 -*-
"""
11 - Altere o programa anterior para mostrar no final a soma dos números.
"""
#Input dos dados
numero_01 = int(input('Informe o primeiro número inteiro: '))
numero_02 = int(input('Informe o segundo número inteiro: '))

#Criando e imprimindo os números
intervalo = range(numero_01+1, numero_02)
print('\n Números: ')
for x in intervalo:
    print(x)
print('\n A soma dos números acima é: {}'.format(sum(intervalo)))
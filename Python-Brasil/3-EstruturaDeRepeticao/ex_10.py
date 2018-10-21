# -*- coding: utf-8 -*-
"""
10 - Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.
"""
#Input dos dados
numero_01 = int(input('Informe o primeiro número inteiro: '))
numero_02 = int(input('Informe o segundo número inteiro: '))

#Criando e imprimindo os números
intervalo = range(numero_01+1, numero_02)
for x in intervalo:
    print(x)
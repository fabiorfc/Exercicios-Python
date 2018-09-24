# -*- coding: utf-8 -*-
"""
09) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e 
mostre a soma dos quadrados dos elementos do vetor.
"""

def ex_09():
    #Declarando o vetor, inputando os dados e fazendo os cálculos
    vetor = []
    for i in range(1,11):
        numero = float(input('Digite o {}° de 10 números: '.format(i)))
        quadrado = numero ** 2
        vetor.append(quadrado)
    soma = sum(vetor)
    #Print dos resultados
    print('A soma dos quadrados dos valores inputados é: {}'.format(vetores))
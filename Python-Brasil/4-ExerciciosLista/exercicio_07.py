# -*- coding: utf-8 -*-
"""
7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números.
"""
def exercicio_07(vetor):
    import numpy as np
    #Cálculo da soma
    soma = sum(vetor)
    #Cálculo do produto
    produto = 1
    for i in range(0,5):
        produto = vetor[i] * produto
    #Print dos resultados
    print('Os numéros inseridos foram: {}'.format(vetor))
    print('Soma: {}'.format(soma))
    print('Produto: {}'.format(produto))

#Teste da função
exercicio_07([1, 2, 4, 5, 6])
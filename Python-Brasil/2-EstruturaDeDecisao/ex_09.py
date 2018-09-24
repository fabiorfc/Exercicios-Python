# -*- coding: utf-8 -*-
"""
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
#Inserção dos valores numéricos
numero_01 = float(input('Insira o 1° número: '))
numero_02 = float(input('Insira o 2° número: '))
numero_03 = float(input('Insira o 3° número: '))
lista = [numero_01, numero_02, numero_03]
#Looping para ordenar
"""
Algoritmo do tipo Bublle Sort
link: https://www.tutorialspoint.com/python/python_sorting_algorithms.htm
"""
for iter_num in range(len(lista)-1, 0, -1):
    for x in range(iter_num):
        if(lista[x] > lista[x+1]):
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
print('Ordenando os valores, temos: {}'.format(lista))


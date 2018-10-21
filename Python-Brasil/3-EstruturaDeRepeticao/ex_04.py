# -*- coding: utf-8 -*-
"""
4 - Supondo que a população de um país A seja da ordem de 80.000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200.000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
escreva o número de anos necessários para que a população do país A ultrapasse 
ou iguale a população do país B, mantidas as taxas de crescimento.
"""
#Inserindo os valores iniciais
pop_a = 80000
pop_b = 200000
ano = 0
#Executando o cálculo
while(pop_a <= pop_b):
    pop_a = pop_a * (1.03)
    pop_b = pop_b * (1.015)
    ano += 1
print('A população do país A alcançará a população do país B em {} anos.'.format(ano))
# -*- coding: utf-8 -*-
"""
    3 - Nome na vertical. Faça um programa que solicite o nome do usuário e 
imprima-o na vertical.
        F
        U
        L
        A
        N
        O
"""

def nome_na_vertical():
    
    nome = input('Digite seu nome: ')
    nome = nome.upper()
    
    for i in range(0, len(nome)):
        print(nome[i])



# -*- coding: utf-8 -*-
"""
    2 - Nome ao contrário em maiúsculas. Faça um programa que permita ao 
usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para 
frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar 
o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""
def nome_inverso():
    
    print('Digite seu nome')
    nome = input('Você pode digitar caracteres maiúsculos ou minúsculos: ')
    nome = nome.lower()
    
    nome_inverso = ''
    for i in range(len(nome) - 1, -1, -1):
        nome_inverso += nome[i]
    
    nome_inverso = nome_inverso.upper()
    return(nome_inverso)
    
# -*- coding: utf-8 -*-
"""
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input('Digite uma letra qualquer')
letra = upper(letra)
vogais = ['A','E','I','O','U']
if( letra in vogais ):
    print('A letra digitada é uma vogal')
else:
    print('A letra digitada é uma consoante')
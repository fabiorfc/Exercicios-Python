# -*- coding: utf-8 -*-
"""
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = input('Informe a letra correspondente ao sexo: ')
if( letra == 'F' ):
    print('{} - Feminino'.format(letra))
elif( letra == 'M' ):
    print('{} - Masculino'.format(letra))
else:
    print('Sexo inválido')

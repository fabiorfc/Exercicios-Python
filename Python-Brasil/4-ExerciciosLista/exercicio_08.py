# -*- coding: utf-8 -*-
"""
8) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
"""
def exercicio_08():    
    #Inputando as alturas
    alturas = []
    for i in range(1,6):
        altura = float(input('Ditige a {}° altura: '.format(i)))
        alturas.append(altura)
    #Inputando as idades
    idades = []
    for i in range(1,6):
        idade = float(input('Ditige a {}° idade: '.format(i)))
        idades.append(idade)
    #Invertendo as alturas e idades
    idades_invertidas  = [i for i in reversed(idades)]
    alturas_invertidas = [i for i in reversed(alturas)]
    
    print('As alturas digitadas, em ordem inversa foram:')
    print('Idades invertidas: {}'.format(idades_invertidas))
    print('Alturas invertidas: {}'.format(alturas_invertidas))
    
#Teste da função
exercicio_08()



# -*- coding: utf-8 -*-
"""
6) Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno, imprima o número de alunos com 
média maior ou igual a 7.0.
"""

def exercicio_06():
    
    #Importando as libraries para calcular as médias
    import numpy as np
    
    #Pedindo as notas dos alunos
    print('Digite as notas separados por com vírgula')
    aluno_01 = input('Digite as notas do 1o aluno: ')
    aluno_01 = [float(x) for x in aluno_01.split(',')]
    
    aluno_02 = input('Digite as notas do 2o aluno: ')
    aluno_02 = [float(x) for x in aluno_02.split(',')]

    aluno_03 = input('Digite as notas do 3o aluno: ')
    aluno_03 = [float(x) for x in aluno_03.split(',')]
    
    aluno_04 = input('Digite as notas do 4o aluno: ')
    aluno_04 = [float(x) for x in aluno_04.split(',')]
    
    aluno_05 = input('Digite as notas do 5o aluno: ')
    aluno_05 = [float(x) for x in aluno_05.split(',')]
    
    aluno_06 = input('Digite as notas do 6o aluno: ')
    aluno_06 = [float(x) for x in aluno_06.split(',')]
    
    aluno_07 = input('Digite as notas do 7o aluno: ')
    aluno_07 = [float(x) for x in aluno_07.split(',')]
    
    aluno_08 = input('Digite as notas do 8o aluno: ')
    aluno_08 = [float(x) for x in aluno_08.split(',')]
    
    aluno_09 = input('Digite as notas do 9o aluno: ')
    aluno_09 = [float(x) for x in aluno_09.split(',')]
    
    aluno_10 = input('Digite as notas do 10o aluno: ')
    aluno_10 = [float(x) for x in aluno_10.split(',')]

    #Calculando as medias
    media_01 = np.mean(aluno_01)
    media_02 = np.mean(aluno_02)
    media_03 = np.mean(aluno_03)
    media_04 = np.mean(aluno_04)
    media_05 = np.mean(aluno_05)
    media_06 = np.mean(aluno_06)
    media_07 = np.mean(aluno_07)
    media_08 = np.mean(aluno_08)
    media_09 = np.mean(aluno_09)
    media_10 = np.mean(aluno_10)

    #Concatenando as médias
    medias = [media_01, media_02, media_03, media_04, media_05, media_06, 
              media_07, media_08, media_09, media_10]
              
    #Contando as notas acima de 7
    contador = 0
    for i in range(0, 10):
        if medias[i] >= 7.0:
            contador += 1
    #Imprimindo os resultados
    print('Existem {} alunos acima da média'.format(contador))
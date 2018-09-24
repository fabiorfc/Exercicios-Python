# -*- coding: utf-8 -*-
""""
4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes.
""""
def exercicio_04(vetor):
    #Convertendo todas as strings em minúsculo    
    vetor = [x.lower() for x in vetor]  
    
    #Criando vetor com vogais
    vogais = ['a','e','i','o','u']
    
    #Loop para contar a quantidade de vogais 
    contador = 0
    consoantes = []
    for i in range(0, len(vetor)):
        if vetor[i] not in vogais:
            contador += 1
            consoantes.append(vetor[i])
            
    #Imprimindo os resultados
    print('Existem {} consoantes no vetor inserido'.format(contador))
    print('As consoantes inseridas sâo: {}'.format(consoantes))
# -*- coding: utf-8 -*-
"""
5 - Altere o programa anterior permitindo ao usuário informar as populações e 
as taxas de crescimento iniciais. Valide a entrada e permita repetir a 
operação.
"""
repetir = 'S'
while(repetir.upper() == 'S'):

    #Inserindo os valores iniciais
    pop_a = float(input('Qual a população inicial do país A: '))
    taxa_a = float(input('Insira a taxa de crescimento do país A (%): '))
    pop_b = float(input('Qual a população inicial do país B: '))
    taxa_b = float(input('Insira a taxa de crescimento do país B (%): '))
    ano = 0
    
    #Executando o cálculo
    while(pop_a <= pop_b):
        pop_a = pop_a * (1 + taxa_a/100)
        pop_b = pop_b * (1 + taxa_b/100)
        ano += 1
        if(ano > 1000):
            break
    
    #Laço para evitar um loop infinito
    if(ano > 1000):
        print('\n Mesmo depois de 1.000 anos a população de A nunca atingirá a de B')
        break
        
    #Solicitando a repetição
    print('\n A população do país A alcançará a população do país B em {} anos.'.format(ano))
    print('\n Repetir')
    print('\n S - Sim')
    print('\n N - Não')
    repetir = input('\n Desejar fazer uma nova simulação? ')




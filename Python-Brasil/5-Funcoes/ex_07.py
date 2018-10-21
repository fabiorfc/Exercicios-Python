# -*- coding: utf-8 -*-
"""
7 - Faça um programa que use a função valorPagamento para determinar o valor 
a ser pago por uma prestação de uma conta. O programa deverá solicitar ao 
usuário o valor da prestação e o número de dias em atraso e passar estes 
valores para a função valorPagamento, que calculará o valor a ser pago e 
devolverá este valor ao programa que a chamou. O programa deverá então exibir 
o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir 
outro valor de prestação e assim continuar até que seja informado um valor 
igual a zero para a prestação. Neste momento o programa deverá ser encerrado, 
exibindo o relatório do dia, que conterá a quantidade e o valor total de 
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte 
forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver 
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""

def valor_pagamento(valor, atraso):
    #Função que recebe os valores de prestação e dias de atraso
    
    if(atraso == 0):
        valor_final = valor
    else:
        valor_final = valor * (1.03 + atraso * 0.001)
    return(valor_final)


def relatorio_diario():
    #Função que gera o relatório geral

    #Importando o pandas para gerar o resultado final
    import pandas as pd

    #Definindo os valores e objetos que serão utilizados na função
    valores = []
    valor = 1
    
    #Loop de execução da função
    while(not valor == 0):

        #Verificação dos resultados digitados pelo usuário
        valor = input('Digite o valor da prestação: ')
        atraso = input('Informe a quantidade de dias de atraso: ')    
    
        try:
            valor = float(valor)
            atraso = float(atraso)
        except ValueError:
            print('\n Os valores inputados de valor e atraso devem ser numéricos')
        else:
            #Cálculo da prestação
            valor_final = valor_pagamento(valor, atraso)
            print(valor_final)
            valores.append(valor_final)
    
    resultado = {'Prestação':[x for x in range(1, len(valores))] ,'Valores':valores[:-1]}
    df = pd.DataFrame(data = resultado, index = None)
    print('\n Resulatório final: \n')
    print(df.to_string(index = False))

    


# -*- coding: utf-8 -*-
"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o 
INSS e 5% para o sindicato, faça um programa que nos dê:
    a) salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.
    e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
    
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
        
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
valor_hora = float(input('Informe o valor da hora trabalhada: '))
total_horas = float(input('Informe quantas horas você trabalha no mês: '))
#Efetuando os cálculos
salario_bruto = valor_hora * total_horas
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto * 0.76
#Imprimindo os resultados
print('Dados da remuneração: ')
print('Salário bruto: R$ {}'.format(salario_bruto))
print('Desconto do IR: R$ {}'.format(ir))
print('Desconto do INSS: R$ {}'.format(inss))
print('Desconto do sindicato: R$ {}'.format(sindicato))
print('Salário líquido: R$ {}'.format(salario_liquido))
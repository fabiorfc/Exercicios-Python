# -*- coding: utf-8 -*-
"""
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para desenvolver o programa que calculará os 
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
seguinte critério, baseado no salário atual:
    * salários até R$ 280,00 (incluindo) : aumento de 20%
    * salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    * salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    * salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser 
    realizado, informe na tela:
    * salário antes do reajuste;
    * percentual de aumento aplicado;
    * valor do aumento;
    * novo salário, após o aumento.
"""

salario = float(input('Informe o valor do seu salário: '))
#Atribuindo o valor do reajuste
if(salario <= 280):
    aumento = 0.20
elif(salario > 280 and salario <= 700):
    aumento = 0.15
elif(salario > 700 and salario <= 1500):
    aumento = 0.10
elif(salario > 1500):
    aumento = 0.05
#Calculando o reajuste
reajustado = salario * (1 + aumento)
#Resultados
print('Salário anterior ao reajuste: {}'.format(salario))
print('Percentual de reajuste aplicado: {}%'.format(aumento*100))
print('Você terá um aumento de: {}'.format(round(reajustado - salario, 1)))
print('Salário após o aumento: {}'.format(round(reajustado, 1)))
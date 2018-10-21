# -*- coding: utf-8 -*-
"""
3 - Faça um programa que leia e valide as seguintes informações:
    * Nome: maior que 3 caracteres;
    * Idade: entre 0 e 150;
    * Salário: maior que zero;
    * Sexo: 'f' ou 'm';
    * Estado Civil: 's', 'c', 'v', 'd';
"""
# === Nome
nome = input('Informe seu nome: ')
while(len(nome) < 3):
    print('\n O nome deve ter mais que 3 caracteres')
    nome = input('Informe seu nome: ')    
# === Idade
idade = float(input('Idade: '))
while(idade<0 or idade>150):
    print('\n A idade deve estar entre 0 e 150 anos')
    idade = float(input('Idade: '))
# === Salário
salario = float(input('Salário: '))
while(salario<0):
    print('\n O salário deve ser maior ou igual a zero')
    salario = float(input('Idade: '))
# === Sexo
sexo = input('sexo: ')
while(sexo not in ['m','f'] ):
    print('\n O sexo deve ser "m" para masculino e "f" para feminino')
    sexo = input('sexo: ')
# === Estado civil
estado_civil = input('Estado Civil: ')
while(estado_civil not in ['s','c','v','d']):
    print('\n O estado civil deve ser "s", "c", "v" ou "d"')
    estado_civil = float(input('Estado Civil: '))
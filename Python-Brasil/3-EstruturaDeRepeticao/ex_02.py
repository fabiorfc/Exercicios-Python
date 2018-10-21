# -*- coding: utf-8 -*-
"""
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a 
pedir as informações.
"""
user = input('Informe o nome do Usuário: ')
senha = input('Informe senha: ')
while(user == senha):
    print('\n A senha deve ser diferente do nome do usuário')
    user = input('Informe o nome do Usuário: ')
    senha = input('Informe senha: ')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. 
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade 
    dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Get_nome(self):
        return self.nome
    
    def Get_idade(self):
        return self.idade
    
    def Get_peso(self):
        return self.peso
    
    def Get_altura(self):
        return self.altura
    
    def Envelhecer(self, anos):
        
        if self.idade < 21:
            self.altura = self.altura + anos*0.5

        self.idade = self.idade + anos
        
    def Engordar(self, peso_adicional):
        self.peso = self.peso + peso_adicional

    def Crescer(self, crescimento):
        self.altura = self.altura + crescimento
        
    def Emagrecer(self, emagrecimento):
        self.peso = self.peso - emagrecimento

# Testando a classe
fabio = Pessoa(nome = 'Fabio', idade = 18, peso = 90, altura = 185)

print("Nome: {}".format(fabio.Get_nome()))
print("Altura: {}".format(fabio.Get_altura()))
print("Peso: {}".format(fabio.Get_peso()))
print("Idade: {} \n".format(fabio.Get_idade()))

# Teste dos métodos
fabio.Envelhecer(3)
fabio.Engordar(5)
fabio.Crescer(7)

print("Depois de um tempo, {} terá:".format(fabio.Get_nome()))
print("Nome: {}".format(fabio.Get_nome()))
print("Altura: {}".format(fabio.Get_altura()))
print("Peso: {}".format(fabio.Get_peso()))
print("Idade: {} \n".format(fabio.Get_idade()))

fabio.Emagrecer(10)

print("Depois de mais um tempo, {} terá:".format(fabio.Get_nome()))
print("Nome: {}".format(fabio.Get_nome()))
print("Altura: {}".format(fabio.Get_altura()))
print("Peso: {}".format(fabio.Get_peso()))
print("Idade: {}".format(fabio.Get_idade()))

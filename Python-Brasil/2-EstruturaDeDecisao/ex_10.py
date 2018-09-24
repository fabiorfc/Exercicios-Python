# -*- coding: utf-8 -*-
"""
10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print('Qual turno você trabalha?')
print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')
turno = input('Turno: ')
if(turno == 'M'):
    print('Bom dia!')
elif(turno == 'V'):
    print('Boa tarde!')
elif(turno == 'N'):
    print('Boa noite!')
else:
    print('Houve algo errado. Você deve digitar umas das opções')
    print('M - Matutino')
    print('V - Vespertino')
    print('N - Noturno')
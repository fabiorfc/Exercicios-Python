# -*- coding: utf-8 -*-
"""
6 - Faça um programa que converta da notação de 24 horas para a notação de 
12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada 
é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a 
conversão e uma para a saída. Registre a informação A.M./P.M. como um valor 
‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá 
um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que 
permita que o usuário repita esse cálculo para novos valores de entrada todas 
as vezes que desejar.
"""


def conversor_hora(hora):
    #Função que converte o sistema de 24 horas para 12
    
    #Conversão
    if(hora > 12):
        hora = hora - 12
    else:
        hora = hora
    return(hora)



def atribuicao_am_pm(hora):
    #Função que retorna o período do dia    

    #Atribuição e retorno do período
    if(hora < 12):
        periodo = 'AM'
    else:
        periodo = 'PM'
    return(periodo)


def conversor(hora, minuto):
    #Função que faz a conversão completa de hora para minutos
    
    #Verificação dos valores inputados
    try:
        hora = int(hora)
        minuto = int(minuto)
    except ValueError:
        print('\n Os valores de horas e minutos devem ser numéricos')
    else:
        if(not (0 <= hora < 24 and 0 <= minuto < 60)):
            print('\n Os valores de Hora e Minutos devem estar entre 0 e 24 para horas e de 0 a 60 para minutos')
        else:            
            #Conversão da hora
            hora_convertida = conversor_hora(hora)
            periodo = atribuicao_am_pm(hora)
            #Conversão dos minutos
            if(0 <= minuto <= 9):
                minuto = '0{}'.format(minuto)
            else:
                minuto = minuto               
            return('{}:{} {}'.format(hora_convertida, minuto, periodo))


def conversor_am_pm():
    #Função que solicita o horário ao usuário

    #Estrutura de repetição
    repetir = 'S'
    while(repetir == 'S'):

        hora = input('Informe a hora: ')
        minuto = input('Informe os minutos: ')
        print(conversor(hora, minuto))
        
        #Verificando se o usuário deseja repetir a operação
        print('\n Deseja repetir a operação? ')
        print('S - Sim')
        print('N - Não')
        repetir = input('')
        repetir = repetir.upper()
        
        while(repetir not in ['S', 'N']):
            print('\n Deseja repetir a operação? ')
            print('S - Sim')
            print('N - Não')
            repetir = input('\n ->')
            repetir = repetir.upper()
                
                









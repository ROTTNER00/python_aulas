'''
Autor: Felipe Rottner Rodrigues
Data: 17/06/2024
Versão: 1.0
Descrição: Faça um programa que receba o número  do mês e apresente ele
           por extenso:
           Sem utilizar condicional!
'''
#=====================================================================================
num_digitado = 0
num_digitado = int(input('Digite um número do mês:'))
mes = [
    '',
    'Janeiro!',
    'Fevereiro!',
    'Março!',
    'Abril!',
    'Maio',
    'Junho!',
    'Julho!',
    'Agosto!',
    'Setembro!',
    'Outubro!',
    'Novembro!',
    'Dezembro!'
]
print(mes[num_digitado])


'''
Autor: Felipe Rottner Rodrigues
Data: 14/06/2024
Versão: 1.0
Descrição: Fça um programa que receba o número da chamada dos alunos
           do curso de python no período noturno do SENAI 115 e 
           apresenta o seu nome
'''
#=====================================================================================
alunos_python_senai = [
    'Luana',
    'Gustavo',
    'Danielle',
    'Felipe',
    'João',
    'Thiago',
    'Vitor',
    'José',
    'Arthur',
    'Pedro',
    'Mauricio',
    'Davi',
    'Kawan',
    'Andrey',
    'Lucas',
    'Diego',
    'João',
    'Ana',
    'Vinicius',
    'Adriel',
    'Patrick',
    'Brunão'
]
while True:
    nr_chamada = 0
    nr_chamada = int(input('Digite o número da chamada:'))
    print(alunos_python_senai[nr_chamada])

    continuar = input('Digite S para sair e C para continuar:')
    if continuar == 'S':
        break
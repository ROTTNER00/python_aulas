'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 04/06/2024
Versão: 1.0
Descrição: Descrição : Faça um programa que receba o salário de um funcionário,
                       calcule e mostre o novo salário, sabendo-se que:
                       Salário < R$1000,00 aumento de 25%
                       Salário >= R$1000,00 e < R$2000,00 aumento de 15%
                       Salário >= R$2000,00 aumento de 10%


Fechamento do Comentário
'''
#================================================
#variaveis
salario = 0
#Entrada
salario = float(input("Digite o seu salário:"))
#Processamento
if salario < 1000:
    salario_aumento = salario * 1.25
    print(round(salario_aumento))
elif salario >= 1000 and salario < 2000: #as duas condições tem que ser verdadeiras
    salario_aumento = salario * 1.15
    print(round(salario_aumento))
elif salario >= 2000:
    salario_aumento = salario * 1.10
    print(round(salario_aumento))
#Saída
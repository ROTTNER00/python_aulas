'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 04/06/2024
Versão: 1.0
Descrição: Descrição : Escreva um programa que leia a idade de um individuo e
                       escreva a faixa etária a que pertence, de acordo com a tabela abaixo:

                       Faixa etária      Classificação
                          <12               Criança
                          13 ~ 17           Adolescente
                          18 ~ 59           Adulto


Fechamento do Comentário
'''
#================================================
#variaveis
idade = 0
#Entrada
idade = int(input("Digite o sua idade:"))
#Processamento
if (idade <12):
    sua_idade = 'Criança'
elif(idade >= 13 and idade < 17):
    sua_idade = 'Adolescente'
elif(idade >=18 and idade <59):
    sua_idade = 'Adulto'
else:
    idade('Idade inválida')
#Saída
print('Sua faixa etária é:', sua_idade)

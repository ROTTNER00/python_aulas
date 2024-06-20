'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 04/06/2024
Versão: 1.0
Descrição:             Escreva um programa que leia a velocidade máxima permitida em 
                       uma avenida e velocidade com que o motorista estava dirigindo
                       nela e calcule a multa que uma pessoa vai receber:

                       Velocidade Ultrapassada              Valor da Multa
                       Até 10km/h                            R$50,00
                       11 a 30 km/h                          R$100,00
                       Mais 31 km/h                          R$200,00


Fechamento do Comentário
'''
#================================================
#variaveis
velocidade_maxima = 0
velocidade_motorista = 0
#Entrada
velocidade_maxima = float(input("Insira a velocidade máxima da via:"))
velocidade_motorista = float(input("Insira sua velocidade:"))
diferença = velocidade_motorista - velocidade_maxima
#Processamento
if  diferença <=10  :
    multa = 'R$50,00'
elif diferença  >=11 and diferença <= 30:
    multa = 'R$100,00'
else:
    multa = 'R$200,00'
#Saída
print('A mulda é no valor de: ', multa)
#===========================================================================================
#Autor: Felipe Rottner Rodrigues
#Data: 24/05/20024
#Versão: 1.0 
#Descrição: Faça umalgoritimo que receba a temperatura em 
#           ºC para ºF e K
#           ----------------------------------------------------
#           Exemplo de execução
#           Insira a temperatura em Celsis: 0
#           Fahrenheit: 32ºF
#           Kelvin: 273,15 k 
#===========================================================================================
#Início
#variaveis
celsius = 0 #temperatura em Celsius inserida pelo usuário
fahrenheit = 0 #temperatura em Fahrenheit vinda da conversão
kelvin = 0 #temperatura em Kelvin vinda da conversão
#Entrada
print('Converção de Graus Celsios para Graus Fahrenheit!')
celsius = float(input('Insira a temperatura em graus Celsios: '))
#Processamento
fahrenheit = (celsius * (9 / 5)) + 32
kelvin = celsius + 273.15
#Saída
print(celsius, 'ºC equivalem', fahrenheit, 'ºF')
print(celsius, 'ºC equivalem', kelvin, 'K')
#Fim
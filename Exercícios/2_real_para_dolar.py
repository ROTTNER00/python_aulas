#===========================================================================================
#Autor: Felipe Rottner Rodrigues
#Data: 24/05/20024
#Versão: 1.0 
#Descrição: Faça umalgoritimo que um valor na moeda real (R$)
#           a cotação da conversão REAL para DÓLAR, e apresente
#           a quantidade desse valor em dólar ($)
#           ----------------------------------------------------
#           Exemplo de execução
#           Insira o valor em real: 5000
#           Insira cotação do dia:5
#           R$5000,00 equivale $1000,00
#===========================================================================================
#Início
#variaveis
real = 0 #receber o valor em reais
cotacao = 0#valor da cotação 1 dolar Xreais
dolar = 0 #valor convertido real para dólar
#Entrada
#necessário fazer o casting(conversão de tiipos de dados)
#float <= string
#5000,00 <= '5000'
real = float(input('Insira o valor em reais (R$): '))
cotacao = float(input('Insira a cotação do dia:'))
#Processamento
dolar = real/cotacao
#Saída
print('R$', real,  'equivalem', '$', dolar)
#Fim
#===========================================================================================
#Autor: Felipe Rottner Rodrigues
#Data: 24/05/20024
#Versão: 1.0 
#Descrição: Faça umalgoritimo que receba 5 notas e imprima 
#           a média final do aluno
#           ----------------------------------------------
#           Exemplo de execução
#           Nota 1: 10
#           Nota 2: 10
#           Nota 3: 10
#           Nota 4: 10
#           Nota 5: 10
#           Média final: 10
#===========================================================================================
#Início
#Entrada
#Nota é uma variável
#castinh
nota1 = int(input('Qual é a primeira nota do aluno?'))
nota2 = int (input('Qual é a segunda nota do aluno?'))
nota3 = int (input('Qual é a terceira nota do aluno?'))
nota4 = int (input('Qual é a quarta nota do aluno?'))
nota5 = int (input('Qual é a quinta nota do aluno?'))
#Processamento
#Conta que deve ser feita
media = (nota1 + nota2 + nota3 + nota4 + nota5) /5
#Saída
print('A média do aluno é:', '=', media)
#Fim
'''
Abertura do Comentário

Autor: Felipe Rottner Rodrigues
Data: 28/05/2024
Versão: 1.0
Descrição: Estudos do condicional IF ... ELIF

Fechamento do Comentário
'''
#================================================
#variavel
nota = 0
#Entrada 
nota = int(input('Insira uma nota?'))
#Processamento
if (nota >6):
    print('Aluno aprovado!')
    #Saída
    print(nota)
elif(nota < 4): #else if(nota < 4)
    print('Aluno reprovado!')
else:
    print('Aluno recuperação!')
#================================================
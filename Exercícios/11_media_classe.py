'''
Autor: Felipe Rottner Rodrigues
Data: 11/06/2024
Versão: 1.0
Descrição: Faça um programa que receba duas notas de seis alunos.
           Calcule e mostre:
           A média aritmética das duas notas de cada aluno; e
           A mensagem que está na tabela a seguir:
           Média Aritmética       Mensagem
           Até 3                  Reprovado
           Entre 4 e 7            Exame
           De 8 para cima         Aprovado 

           O total de alunos aprovados;
           O total de alunos exame;
           O total de alunos reprovados;
           A média da classe;        
'''
#================================================================================
aluno = 0
qtdAlunos = 6
alunosAprovados = 0
alunosReprovados = 0
alunosExame = 0
mediaFinal = 0
somaClasse = 0
somaMedia = 0

while aluno < qtdAlunos:
    aluno = aluno + 1 # aluno += 1
    #Aluno x
    nota1 = 0
    nota2 = 0
    media = 0

    #nota1 = float(input("Digite a primeira nota do aluno", aluno, ":"))
    #A letra "f" serve para fazer a interpolação de "Misturar" strings com variáveis
    nota1 = float(input(f"Digite a primeira nota do aluno {aluno}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {aluno}:"))

    #Conta da média
    media = (nota1 + nota2)/2 #10 -> 8 -> 5 -> 10 -> 7 -> 8
    somaMedia = somaMedia + media # 10 -> 18 -> 23 -> 33 -> 40 -> 48
    mediaFinal = round((somaMedia / qtdAlunos),2)
    
    if media <= 3:
        print("Reprovado!")
        alunosReprovados += 1 #alunosReprovados = alunosReprovados + 1
    elif media >= 4 and media <=7:
        print("Exame!")
        alunosExame += 1 #alunosExame = alunosExame + 1
    else:
        print("Aprovado!")
        alunosAprovados += 1 #alunosAprovados = alunosAprovados + 1

print(f"Quantidade de alunos aprovados: {alunosAprovados}")
print(f"Quantidade de alunos reprovados: {alunosReprovados}")
print(f"Quantidade de alunos de exame: {alunosExame}")
print(f"Média da classe: {mediaFinal}")
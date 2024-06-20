#Variaveis
peso = 0
altura = 0
imc = 0
#Entrada
print("Calculo de IMC")
peso = float(input("Insira seu peso em kilogramas (kg):"))
altura = float(input("Insira sua altura em metros(m):"))
#Processamento
imc = peso / (altura * altura)
print("Seu IMC é", imc,"Kg")

if imc >= 16 and imc  <= 16.9:
    print("\nVocê está muito abaixo do peso!")
elif imc >= 17 and imc  <= 18.4:
    print("\nVocê está abaixo do peso!")
elif imc >= 18.5 and imc  <= 24.9:
    print("\nVocê tem o peso ideal!")
elif imc >= 25 and imc  <= 29.9:
    print("\nVocê está acima do peso!")
elif imc >= 30 and imc  <= 34.9:
    print("\nVocê tem obsidade grau 1!")
elif imc >= 35 and imc  <= 40:
    print("\nVocê tem obsidade grau 2!")
else:
    print("\nVocê tem obsidade grau 3!")
#Saída

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43

chute = int(input("Digite o seu numero: "))

print(f"Voçe digitou {chute}")

if (numero_secreto == chute):
    print("você ecertou")
else:
    print("você errou!!!")

print("Fim do jogo")
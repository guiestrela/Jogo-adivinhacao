import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = int(random.randrange(1, 101))
tentativa = 3


for rodada in range(1, tentativa + 1):
    print(f"Tetantativa {rodada} de {tentativa}")
    chute = int(input("Digite um numero entre 1 e 100: "))
    print(f"Voçe digitou {chute}")

    if chute < 1 or chute > 100:
        print(f"O numero {chute} não é valido.. Tente novamente Entre 1 e 100")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("você ecertou")
        break
    else:
        if maior:
            print("Você errou!!!! O seu chute foi maior que o numero secreto")
        elif menor:
            print("Você errou!!! O seu chute foi menor que o numero secreto ")

print("Fim do Jogo!!!")


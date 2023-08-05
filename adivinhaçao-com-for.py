print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43
tentativa = 3
rodada = 1

while rodada <= tentativa:
    print(f"Tetantativa {rodada} de {tentativa}")
    chute = int(input("Digite o seu numero: "))
    print(f"Voçe digitou {chute}")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("você ecertou")
        break
    else:
        if (maior):
            print("Você errou!!!! O seu chute foi maior que o numero secreto")
        elif (menor):
            print("Você errou!!! O seu chute foi menor que o numero secreto ")
    rodada += 1
print("Fim do Jogo!!!")


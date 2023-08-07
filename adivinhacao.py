import random
def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = int(random.randrange(1, 101))
    tentativa = 0
    pontos = 1000

    print("Qual nível de dificudade?")
    print("(1) Facíl (2) médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if nivel == 1:
        tentativa = 20
    elif nivel == 2:
        tentativa = 10
    else:
        tentativa =5

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
            print(f"você ecertou e fez {pontos} pontos")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if maior:
                print("Você errou!!!! O seu chute foi maior que o numero secreto")
                if rodada == tentativa:
                    print(f"o numero secreto era {numero_secreto}. Você fez {pontos} pontos")
            elif menor:
                print("Você errou!!! O seu chute foi menor que o numero secreto ")
                if rodada == tentativa:
                    print(f"o numero secreto era {numero_secreto}. Você fez {pontos} pontos")


    print("Fim do Jogo!!!")

if __name__ == "__main__":
    jogar()
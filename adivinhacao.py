import random
import jogos
import adivinhacao


def mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def gerar_numero():
    numero_secreto = round(random.randrange(1, 101))
    return numero_secreto


def selecionar_dificuldade():
    print("Selecione a dificuldade:")
    print("(1) Facil - (2) Medio - (3) Dificil")

    nivel = int(input("Defina a dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 10
        pontos = 100
        return total_de_tentativas, pontos
    elif (nivel == 2):
        total_de_tentativas = 7
        pontos = 75
        return total_de_tentativas, pontos
    elif (nivel == 3):
        total_de_tentativas = 5
        pontos = 50
        return total_de_tentativas, pontos
    else:
        print("A dificuldade selecionada não existe!")


def jogando(total_de_tentativas, pontos, numero_secreto):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi MAIOR que o numero!")
            elif (menor):
                print("Você errou! O seu chute foi MENOR que o numero!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (pontos < 0):
                break
        rodada += 1


def reiniciar():
    jogar = input("Deseja jogar novamente? S- sim / N- não: ").strip().upper()
    if (jogar == "S"):
        adivinhacao.jogar()
    else:
        voltar = input("Deseja escolher outro jogo/versão? S- Sim / N- não: ").strip().upper()
        if(voltar == "S"):
            jogos.escolhe_jogo()
        else:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("-*-*Obrigado por Jogar!*-*-")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def jogar():

    mensagem_abertura()

    numero_secreto = gerar_numero()

    total_de_tentativas, pontos = selecionar_dificuldade()

    jogando(total_de_tentativas, pontos, numero_secreto)

    print("O numero secreto era: ", numero_secreto)
    print("Fim de jogo!")

    reiniciar()

if(__name__ == "__main__"):
    jogar()
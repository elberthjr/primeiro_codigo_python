import random
import adivinhacao2
import jogos


def mensagem_abertura():
    print("---------------------------------")
    print("Bem vindo ao jogo de Adivinhação!")
    print("---------------------------------")


def gerar_numero():
    print("Escolha dois numeros e o jogo escolhera um numero secreto entre eles:")
    minimo = int(input("Selecione o minimo:"))
    maximo = int(input("Selecione o maximo:")) + 1
    numero_secreto = round(random.randrange(minimo, maximo))
    return numero_secreto, minimo, maximo


def selecionar_dificuldade(maximo):
    print("Selecione a dificuldade:")
    print("(1) Facil - (2) Medio - (3) Dificil")

    nivel = int(input("Defina a dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 10
        pontos = maximo * 2
        return total_de_tentativas, pontos
    elif (nivel == 2):
        total_de_tentativas = 7
        pontos = int(maximo * 1.5)
        return total_de_tentativas, pontos
    elif (nivel == 3):
        total_de_tentativas = 5
        pontos = maximo
        return total_de_tentativas, pontos
    else:
        total_de_tentativas = -1
        pontos = 0
        return total_de_tentativas, pontos


def finalizando_game(numero_secreto):
    print("O numero secreto era: ", numero_secreto)
    print("Fim de jogo!")


def reiniciar():
    jogar = input("Deseja jogar novamente? S- sim / N- não: ").strip().upper()
    if (jogar == "S"):
        adivinhacao2.jogar()
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

    numero_secreto, minimo, maximo = gerar_numero()
    maximo -= 1
    total_de_tentativas, pontos = selecionar_dificuldade(maximo)

    if(total_de_tentativas == -1):
        print("A dificuldade selecionada não existe!")
        total_de_tentativas, pontos = selecionar_dificuldade(maximo)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre {} e {}: ".format(minimo, maximo))
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < minimo or chute > maximo):
            print("Voce deve digitar um numero entre {} e {}!".format(minimo, maximo))
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

    finalizando_game(numero_secreto)

    reiniciar()


if(__name__ == "__main__"):
    jogar()
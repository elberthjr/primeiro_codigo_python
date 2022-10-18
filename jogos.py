import forca
import forca2
import adivinhacao
import adivinhacao2


def mensagem_abertura():
    print("*********************************")
    print("-------Escolha o seu jogo!-------")
    print("*********************************")
    print("(1) Adivinhação - (2) Forca")


def define_jogo(jogo):
    if (jogo == 1):
        print("Qual versão deseja jogar? ")
        versao = int(input("1 para versão Alura - 2 para a versão Elber: "))
        if(versao == 1):
            adivinhacao.jogar()
        elif(versao == 2):
            adivinhacao2.jogar()
        else:
            print("Versão Invalida!!")
    elif (jogo == 2):
        print("Qual versão deseja jogar? ")
        versao = int(input("1 para versão Alura - 2 para a versão Elber: "))
        if (versao == 1):
            forca.jogar()
        elif (versao == 2):
            forca2.jogar()
        else:
            print("Versão Invalida!!")
    else:
        print("Opção de joogo Invalida!!")


def escolhe_jogo():

    mensagem_abertura()

    jogo = int(input("Selecione o Jogo:"))

    define_jogo(jogo)


if (__name__ == "__main__"):
    escolhe_jogo()

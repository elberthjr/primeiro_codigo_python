import random

import forca2
import jogos


def jogar():

    mensagem_abertura()
    palavra_secreta = gerando_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        letra_ou_op = input("Seu chute será uma (L)etra ou o (O)perador?").strip().upper()
        if (letra_ou_op == "L"):
            chute = pede_letra()
            if (chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            else:
                erros += 1
                desenha_forca(erros)
            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)
        elif(letra_ou_op == "O"):
            acertou, enforcou = pede_palavra(palavra_secreta)
        else:
            print("Digite 'L' para Letra e 'O' para Operador!")

    if(acertou):
        mensagem_vencedora(palavra_secreta)
    else:
        mensagem_derrota(palavra_secreta)
        
    reiniciar()


def mensagem_abertura():
    print("---------------------------------")
    print("---Bem vindo ao jogo de Forca!---")
    print("-----Versão Rainbow 6 Siege!-----")
    print("---------------------------------")


def gerando_palavra():
        print("Selecione o lado do operador: ")
        tema = int(input("1- Ataque / 2- Defesa: "))

        if(tema == 1):
            arquivo = open("ataque.txt")
        else:
            arquivo = open("defesa.txt")

        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_letra():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def pede_palavra(palavra):
    chute = input("Qual Operador? ").upper().strip()
    if(chute == palavra):
        return True, False
    else:
        return False, True


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1


def mensagem_vencedora(palavra_secreta):
    print("O operador é {}".format(palavra_secreta))
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("O operador era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def reiniciar():
    jogar = input("Deseja jogar novamente? S- sim / N- não: ").strip().upper()
    if (jogar == "S"):
        forca2.jogar()
    else:
        voltar = input("Deseja escolher outro jogo/versão? S- Sim / N- não: ").strip().upper()
        if(voltar == "S"):
            jogos.escolhe_jogo()
        else:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("-*-*Obrigado por Jogar!*-*-")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")


if(__name__ == "__main__"):
    jogar()
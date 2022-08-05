import random

def jogar():

    print("*******************************")
    print("Bem vindo no jogo de adiviação")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000


    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 a 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100!")
            continue #continua o laço

        print("Você digitou {}".format(chute))

        #teste logicos
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break #para o laço
        else:
            if(maior):
                print("Você erro! o seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você erro! o seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #40 - 20
            pontos = pontos - pontos_perdidos


    #idade1 = 10
    #idade2 =int("20")
    #print(idade1 + idade2)
    #nome = "Nico"
    #sobrenome = "Steppat"
    #print(nome, sobrenome, sep=" ")
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()

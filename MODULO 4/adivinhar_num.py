import random

def adivinhe_numero():
    numero_sorteado = random.randint(1, 100)  # Número aleatório entre 1 e 100
    palpite = 0  # Inicializa a variável do palpite

    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Tente adivinhar o número entre 1 e 100.")

    while palpite != numero_sorteado:
        palpite = int(input("Digite seu palpite: "))  

        if palpite < numero_sorteado:
            print("O número é maior!")
        elif palpite > numero_sorteado:
            print("O número é menor!")
        else:
            print("Parabéns! Você acertou!")

adivinhe_numero()

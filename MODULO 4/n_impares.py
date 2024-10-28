n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    count = 0  # Contador para acompanhar quantos números ímpares foram impressos
    odd_number = 1  # O primeiro número ímpar

    while count < n:
        print(odd_number)  # Imprime o número ímpar
        odd_number += 2  # Passa para o próximo número ímpar
        count += 1  # Incrementa o contador

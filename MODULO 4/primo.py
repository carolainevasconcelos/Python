numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("não primo")
else:
    # Inicializa a variável de verificação
    i = 2
    is_primo = True

    # Verifica a divisibilidade até a raiz quadrada do número
    while i * i <= numero:
        if numero % i == 0:
            is_primo = False  # Não é primo se divisível por i
            break  # Sai do loop se um divisor é encontrado
        i += 1  # Incrementa i

    if is_primo:
        print("primo")
    else:
        print("não primo")

soma = 0

while True:  # Usar um loop infinito
    x = int(input("Digite um número (0 para sair): "))  # Ler o número do usuário
    if x == 0:  # Verificar se o número é zero
        break  # Sair do loop se for zero
    soma += x  # Adicionar o número à soma

print("A soma é:", soma)  # Exibir a soma total
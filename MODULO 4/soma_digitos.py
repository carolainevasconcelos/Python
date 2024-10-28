numero = int(input("Digite um número inteiro: "))

soma = 0  # inicia a variável com 0

# Usa o valor absoluto do número para lidar com números negativos
numero = abs(numero)

while numero > 0:
    # Obtém o último dígito do número usando o operador %
    digito = numero % 10
    
    # Adiciona o dígito à soma total
    soma += digito
    
    # Remove o último dígito do número usando o operador //
    numero //= 10

print(soma)  # Imprime apenas a soma dos dígitos
numero = input("Digite um número inteiro: ")

i = 0
tem_adjacente = False  # Assume que não há dígitos adjacentes iguais

# Loop para percorrer os dígitos do número
while i < len(numero) - 1:
    # Verifica se o dígito atual é igual ao próximo
    if numero[i] == numero[i + 1]:
        tem_adjacente = True  # Atualiza a flag
        break  # Sai do loop se encontrar dígitos iguais
    i += 1  # Incrementa o índice

if tem_adjacente:
    print("sim")
else:
    print("não")
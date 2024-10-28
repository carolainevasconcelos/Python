def fatorial(n):
    resultado = 1  # Inicializa o resultado como 1
    while n > 1:
        resultado *= n  # Multiplica o valor atual de resultado por n
        n -= 1  # Decrementa n em 1
    return resultado  

n = int(input("Digite um número inteiro: "))
k = int(input("Digite um número inteiro: "))

resultado= fatorial(n) // (fatorial(k)*fatorial(n-k))

print(f"O resultado de C({n}, {k}) é: {resultado}")
'''
def fatorial(n): 
    resultado = 1  # Inicializa o resultado como 1
    while n > 1:
        resultado *= n  # Multiplica o valor atual de resultado por n
        n -= 1  # Decrementa n em 1
    return resultado  

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

# Calcula a combinação C(n, k) = n! / (k! * (n - k)!)
resultado = fatorial(n) // (fatorial(k) * fatorial(n - k))

print(f"O resultado de C({n}, {k}) é: {resultado}")

'''
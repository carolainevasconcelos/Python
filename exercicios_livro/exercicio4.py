def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

n = int(input("Digite um número inteiro: "))
m = int(input("Digite um número inteiro: "))

resultado = fatorial(m) / (fatorial(m - n) * fatorial(n))

print(resultado)
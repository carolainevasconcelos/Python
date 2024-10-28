def eh_hipotenusa(h):
    i = 1
    while i < h:  # Verifica todos os inteiros menores que h
        j = i  # Começa j em i para evitar duplicação
        while j < h:  # Verifica todos os inteiros menores que h
            if h**2 == i**2 + j**2:  # Verifica a condição da hipotenusa
                return True
            j += 1
        i += 1
    return False

def soma_hipotenusas(n):
    soma = 0
    h = 1
    while h <= n:  # Para cada número de 1 a n
        if eh_hipotenusa(h):  # Verifica se h é uma hipotenusa
            soma += h  # Adiciona h à soma se for hipotenusa
        h += 1
    return soma

# Exemplo de uso
resultado = soma_hipotenusas(25)
print(resultado)
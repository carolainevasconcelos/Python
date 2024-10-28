import math

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"a raiz dupla desta equação é {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 > raiz2:
        raiz1, raiz2 = raiz2, raiz1
    print(f"as raízes da equação são {raiz1} e {raiz2}")

'''
import math

def resolver_equacao(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Esta equação não possui raízes reais"
    elif delta == 0:
        raiz = -b / (2 * a)
        return f"A raiz dupla desta equação é {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"As raízes da equação são {min(raiz1, raiz2)} e {max(raiz1, raiz2)}"

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Resultado
print(resolver_equacao(a, b, c))
'''
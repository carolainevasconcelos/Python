import math

x1 = float(input("Digite um numero:"))
y1 = float(input("Digite um numero:"))
x2 = float(input("Digite um numero:"))
y2 = float(input("Digite um numero:"))

d = math.sqrt(((x1 - y1)**2) + ((x2 - y2)**2))

if d >= 10:
    print("longe")
else:
    print("perto")
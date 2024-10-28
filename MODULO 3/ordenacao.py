'''
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente
'''

n1 = int(input("Digite um numero inteiro:"))
n2 = int(input("Digite um numero inteiro:"))
n3 = int(input("Digite um numero inteiro:"))

if n1 < n2 < n3:
    print("crescente")
else:
    print("não está em ordem crescente")
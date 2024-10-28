'''
Escreva uma função chamada soma_ate_limite que receba um número inteiro como parâmetro e que some números inteiros consecutivos começando de 1 até que a soma seja maior ou igual ao número dado. A função deve retornar a soma final e o número de termos somados.
'''

numero = int(input('Digite um numero inteiro: '))

soma = 0

while numero > 0:
    soma += numero  
    numero = int(input('Digite outro número inteiro: '))  

print("Resultado da soma:", soma)
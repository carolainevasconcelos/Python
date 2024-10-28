'''
Escreva uma função chamada contagem_regressiva que peça para o usuário digitar um número inteiro positivo. Se o número for negativo ou zero, o programa deve continuar pedindo um valor válido até que o usuário insira um número positivo. Em seguida, o programa deve realizar uma contagem regressiva do número inserido até 0, exibindo cada número na tela.
'''

numero = int(input('Digite um numero inteiro '))

while numero >= 0:
    print(numero)  
    numero -= 1

print("Contagem regressiva concluída!")
'''
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

    "A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada."

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.
'''

nome = input("Digite o nome do cliente:")
diaVencimento = input("Digite o dia de vencimento:")
mesVencimento = input("Digite o mês de vencimento:")
valorFatura = input("Digite o valor da fatura:")

print("Ola", nome)
print("A sua fatura com vencimento em", diaVencimento, "de", mesVencimento, "no valor de R$", valorFatura, "está fechada.")
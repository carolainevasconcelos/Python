n = int(input("Digite um número:"))  

f = 1  # Inicializa o fatorial como 1

if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    # Calcula o fatorial
    while n > 0:
        f = f * n  # Multiplica f pelo valor atual de n
        n = n - 1  # Decrementa n em 1
    
    print(f) 
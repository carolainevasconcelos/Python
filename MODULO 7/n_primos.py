def n_primos(n):
    count = 0  
    num = 2    

    while num <= n:
        is_primo = True

        divisor = 2 
        while divisor * divisor <= num:  # Verificamos até a raiz quadrada de 'num'
            if num % divisor == 0:  
                is_primo = False  
            divisor += 1

        if is_primo: 
            count += 1  

        num += 1  

    return count  

print(n_primos(2))    # Saída: 1
print(n_primos(4))    # Saída: 2
print(n_primos(121))  # Saída: 30
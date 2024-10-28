def maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:  
            maior = elemento  
    return maior  

lista = [2, 4, 2, 2, 3, 3, 1]
print(maior_elemento(lista))
def remove_repetidos(lista):
    lista = sorted(set(lista))  
    return lista  

lista = [2, 4, 2, 2, 3, 3, 1]
resultado = remove_repetidos(lista)
print(resultado)

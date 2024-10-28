# Pense em pelo menos cinco lugares no mundo que você gostaria de visitar.
# a) Armazene os locais em uma lista. Esteja certo que a lista não está em ordem alfabética.
locais = ['Italia', 'Grecia', 'Japao', 'Chile', 'EUA']

# b) Imprima sua lista em sua ordem original. Não se preocupe em imprimir a lista ordenadamente; apenas imprima-o como uma lista Python bruta.
print(locais)

# c) Use sorted() para imprimir sua lista em ordem alfabética sem modificar a lista real.
print("\nLista em ordem alfabética:")
print(sorted(locais))

# d) Mostre que sua lista ainda está em sua ordem original imprimindo-a.
print("\nLista original após sorted():")
print(locais)

# e) Use sorted() para imprimir sua lista em ordem alfabética reversa sem alterar a ordem da lista original.
print("\nLista em ordem alfabética reversa:")
print(sorted(locais, reverse=True))

# f) Mostre que sua lista ainda está em sua ordem original imprimindo-a novamente.
print("\nLista original após sorted(reverse):")
print(locais)

# g) Use reverse() para alterar a ordem da sua lista. Imprima a lista para mostrar que sua ordem foi alterada.
locais.reverse()  
print("\nLista após reverse():")
print(locais)

# h) Use reverse() para alterar a ordem de sua lista novamente. Imprima a lista para mostrar que está de volta à sua ordem original.
locais.reverse()  
print("\nLista após reverter novamente:")
print(locais)

# i) Use sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Imprima a lista para mostrar que sua ordem foi alterada.
locais.sort()  
print("\nLista após sort():")
print(locais)

# j) Use sort() para alterar sua lista para que ela seja armazenada em ordem alfabética reversa. Imprima a lista para mostrar que sua ordem foi alterada.
locais.sort(reverse=True)  
print("\nLista após sort(reverse=True):")
print(locais)
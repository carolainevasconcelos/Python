'''
Um ano bissexto ocorre aproximadamente a cada 4 anos. Escreva uma expressão (em função de uma incógnita ano) que resulte em True caso ano seja bissexto e False caso contrário. Para ser bissexto, o valor de ano precisa ser múltiplo de 4, exceto múltiplos de 100 que não são múltiplos de 400. Assim o ano de 2020 é bissexto pois satisfaz todas essas condições.
'''
ano = 2021
anoBissexto = ano % 4 == 0
print(anoBissexto)
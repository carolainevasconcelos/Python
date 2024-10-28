'''
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

a = 0  # Controla a altura
while a < altura:
    l = 0  # Controla a largura
    while l < largura:
        print("#", end="")
        l += 1
    print()  # Muda para a próxima linha
    a += 1
    /////////////////////////////////
     '''
largura= int(input("digite uma largura: "))
altura = int(input("digite uma altura: "))

a = 1
while a <= altura:
    l = 1
    while l <= largura:
        print("#", end="")
        l = l + 1
    print()
    a = a + 1
 

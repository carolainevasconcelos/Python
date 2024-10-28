''' largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

a = 0
while a < altura:
    if a == 0 or a == altura - 1:  # Primeira e última linha são completamente preenchidas
        print("#" * largura)
    else:  # Linhas intermediárias com espaços no meio
        print("#" + " " * (largura - 2) + "#")
    a += 1
    '''

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

a = 1
while a <= altura:
    l = 1
    while l <= largura:
        # Primeira ou última linha (borda)
        if a == 1 or a == altura:
            print("#", end="")
        # Linhas intermediárias (com espaços no meio)
        else:
            if l == 1 or l == largura:
                print("#", end="")
            else:
                print(" ", end="")
        l += 1
    print()
    a += 1
# a) Se você pudesse convidar qualquer pessoa, viva ou falecida, para jantar, quem você convidaria? Faça uma lista que inclua pelo menos três pessoas que você gostaria de convidar para jantar. Em seguida, use sua lista para imprimir uma mensagem para cada pessoa, convidando-a para jantar.

convidados = ['Joao Pedro', 'Kylie', 'Anne Hathaway']

print("Olá,", convidados[0], "gostaria de convidá-lo(a) para jantar!")
print("Olá,", convidados[1], "gostaria de convidá-lo(a) para jantar!")
print("Olá,", convidados[2], "gostaria de convidá-lo(a) para jantar!")

'''
b) Alteração da lista de convidados: você acabou de ouvir que um de seus convidados não pode comparecer ao jantar, então precisa enviar um novo conjunto de convites. Você terá que pensar em outra pessoa para convidar.

    Comece com seu programa do Exercício "a".
    Adicione uma chamada print() no final do seu programa, informando o nome do convidado que não pode comparecer
    Modifique sua lista, substituindo o nome do convidado que não pode comparecer pelo nome da nova pessoa que você está convidando.
    Imprima um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda está em sua lista.
'''

print(convidados[1], "não vai poder comparecer!")

del convidados[1]
convidados.append('Bela Hadid')

# print(convidados)

print("Olá,", convidados[0], "gostaria de convidá-lo(a) para jantar!")
print("Olá,", convidados[1], "gostaria de convidá-lo(a) para jantar!")
print("Olá,", convidados[2], "gostaria de convidá-lo(a) para jantar!")

'''
c) Você acabou de encontrar uma mesa de jantar maior, então agora há mais espaço disponível. Pense em mais três pessoas para convidar para jantar.

    Comece com seu programa do Exercício "a" ou "b".
    Adicione uma chamada print() ao final do seu programa, informando às pessoas que você encontrou uma mesa maior.
    Use insert() para adicionar um novo convidado ao início de sua lista.
    Use insert() para adicionar um novo convidado ao meio de sua lista.
    Use append() para adicionar um novo convidado ao final de sua lista.
    Imprima um novo conjunto de mensagens de convite, uma para cada pessoa em sua lista.
'''

print(convidados, "encontrei uma mesa maior!")

convidados.insert(0, 'Gigi Hadid')
convidados.insert(2, 'Kim Kardashian')
convidados.append('Jenifer Aniston')

print("Olá,", convidados, "gostaria de convidá-lo(a) para jantar!")

'''
d) Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e agora você tem espaço para apenas dois convidados.

    Comece com seu programa do "c"
    Adicione uma nova linha que imprima uma mensagem dizendo que você pode convidar apenas duas pessoas para jantar.
    Use pop() para remover convidados de sua lista, um por vez, até que apenas dois nomes permaneçam em sua lista.
    Cada vez que você tirar um nome de sua lista, imprima uma mensagem para essa pessoa informando que você lamenta não poder convidá-la para jantar.
    Imprima uma mensagem para cada uma das duas pessoas ainda em sua lista, informando que ainda estão convidadas.
    Use del para remover os dois últimos nomes de sua lista, para que você tenha uma lista vazia.
    Imprima sua lista para ter certeza de que você realmente tem uma lista vazia no final do seu programa.
'''

print("Infelizmente, só posso convidar duas pessoas para jantar.")

while len(convidados) > 2:
    removido = convidados.pop()  
    print("Desculpe,", removido, "não poderei convidá-lo(a) para jantar.")

print("\nConvidados que ainda estão na lista:")
for convidado in convidados:
    print("Olá,", convidado, "você ainda está convidado(a) para jantar!")

del convidados[:]
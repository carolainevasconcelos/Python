# a) Use uma variável para representar o nome de uma pessoa e imprima uma mensagem para essa pessoa. Sua mensagem deve ser simples, como “Olá Eric, gostaria de aprender um pouco de Python hoje?”

nome = input("Qual o seu nome? ")
saudacao = f"Olá {nome}, gostaria de aprender um pouco de Python hoje?"
print(saudacao)

# b) Use uma variável para representar o nome de uma pessoa e, em seguida, imprima o nome dessa pessoa com todas as letras minúsculas. Na sequência, imprima todas as letras maiúsculas e, por fim, apenas as iniciais de cada palavra em maiúscula.

print(nome.upper())
print(nome.title())

# c) encontre uma citação de uma pessoa famosa que você admira. Imprima a citação e o nome de seu autor. Sua saída deve ser algo como o seguinte, "incluindo as aspas":

    # *Albert Einstein disse uma vez: “Uma pessoa que nunca cometeu um erro nunca tentou nada novo”.*

autor = input("Diga o nome do autor da citacao: ")
citacao = input("Diga a citação: ")

print(f'{autor} disse uma vez: "{citacao}"')

# d) Repita o Exercício "c", mas desta vez, represente o nome da pessoa famosa usando uma variável chamada pessoa_famosa. Em seguida, refaça a composição de sua mensagem e represente-a com uma nova variável chamada mensagem. Imprima sua mensagem.

pessoa_famosa = input("Diga o nome da pessoa famosa: ")
citacao = input("Diga a citação: ")

mensagem = f'{pessoa_famosa} disse uma vez: "{citacao}"'

print(mensagem)

# e) Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. Certifique-se de usar cada uma das combinações de caracteres "\t" e "\n" pelo menos uma vez.

pessoa_famosa = input("Diga o nome da pessoa famosa: ")
citacao = input("Diga a citação: ")

mensagem = f'\t{pessoa_famosa} disse uma vez: "{citacao}"\n'

print(mensagem)
print(mensagem.rstrip())     
print(mensagem.lstrip())

# f) Imprima o nome armazenado na atividade "e" uma vez, para que o espaço em branco ao redor do nome seja exibido. Em seguida, imprima o nome usando cada uma das três funções de remoção, lstrip(), rstrip() e strip().

pessoa_famosa = input("Diga o nome da pessoa famosa: ")
citacao = input("Diga a citação: ")

mensagem = f'\t{pessoa_famosa} disse uma vez: "{citacao}"\n'

print(mensagem)
print(mensagem.rstrip())     
print(mensagem.lstrip())
print(mensagem.strip())

# g) Atribua o valor python_notes.txt a uma variável chamada nome_arquivo. Em seguida, programe um método para exibir o nome do arquivo sem a extensão do arquivo, como fazem alguns navegadores de arquivos.

# Atribuindo o nome do arquivo a uma variável
nome_arquivo = "python_notes.txt"

# Usando o split para dividir o nome do arquivo e a extensão
nome_sem_extensao = nome_arquivo.split(".")[0]

print(nome_sem_extensao) # nome do arquivo sem a extensão
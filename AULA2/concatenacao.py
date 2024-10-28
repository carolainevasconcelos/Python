#'' usado para separar o nome

#Concatenando Strings com +
nome = 'Joao'
sobrenome = 'Silva'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

#Usando multiplas strings juntas
nome = 'Joao', ' ', "Silva"
print(nome_completo)

#Usando f-strings
nome = 'Joao'
sobrenome = 'Silva'
nome_completo = f'{nome} {sobrenome}'
print(nome_completo)

# Usando %
nome = "Joao"
saudacao = "Olá, %s" % nome
print(saudacao)

# Usando  str.format()
nome = "Joao"
saudacao = "Olá, {}".format(nome)
print(saudacao)

# Usando  f-strings
nome = "Joao"
saudacao = f"Olá, {nome}"
print(saudacao)
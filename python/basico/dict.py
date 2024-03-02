
# criação de um dicionário

pessoa = {
    'nome': 'Diogo',
    'sobrenome': 'Antonio',
    'idade': 21
}

# atualizar um dado

pessoa.update({'sobrenome': 'Bohrer'})
print(pessoa)

# pegar um dado do dicionário

nome = pessoa.get('nome')
print(nome)

valorInexistente = pessoa.get('valorInexistente')
print(valorInexistente)

valorInexistente = pessoa.get('valorInexistente', "Valor não existente.")
print(valorInexistente)

# remover um dado do dicionário

del pessoa["sobrenome"]
print(pessoa)

pessoa.update({'sobrenome': 'Bohrer'}) # se valor não existir, ele cria
print(pessoa)

# loop dentro de um dicionário

for chave, valor in pessoa.items():
    print(chave, valor)

# igual lista mas evita números duplicados

lista1 = [10, 20, 30, 60, 70]
lista2 = [10, 30, 40, 50, 70]

set1 = set(lista1)
set2 = set(lista2)

print(set1)
print(set2)

print(set1 | set2) # uniao entre sets
print(set1 - set2) # diferença entre sets
print(set1 ^ set2) # diferença simétricas entre sets

# adicionar dados a um set

setExemplo = {1, 3, 5, 7}
setExemplo.add(9)

print(setExemplo)

setExemplo.update([3, 5, 11, 13]) # não adiciona o item se ele já existir no set
print(setExemplo)

# remover um item de um set
setExemplo.discard(3) # se o item não existir no set NÃO gera um erro
print(setExemplo)

setExemplo.remove(13) # se o item não existir no set gera um erro
print(setExemplo)

# sets ainda possuem as funções que fazem o padrão | ^ -
set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set3 = set1.symmetric_difference(set2)
print(set3)


# fazer uma lista a partir de outra lista

# criando a lista2 igual a 1 de uma maneira boba
lista1 = ['diogo', 'antonio', 'bohrer', 'pereira', '21 anos']
lista2 = lista1

print(lista2)

# com copy

lista2 = lista1.copy()
print(lista2)

# com list comprehension

lista2 = [item for item in lista1]
print(lista2)

# gerar uma lista direto com uma função

lista3 = [valor for valor in range(0, 5)]
print(lista3)

# usando generator para criar uma lista
from sys import getsizeof

lista = (valor for valor in range(0, 100))
print(list(lista))
print(type(lista))
print(getsizeof(lista)) # utiliza muito menos memoria do que o list comprehension normal

lista = [valor for valor in range(0, 100)]
print(list(lista))
print(type(lista))
print(getsizeof(lista))
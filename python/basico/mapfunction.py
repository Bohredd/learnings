
# aplica uma função de um unico item para uma lista

def multiplicar(x):
    return x * 2

lista = [1, 2, 4, 6]
print(multiplicar(lista))

print(list(map(multiplicar, lista)))

# map com lambda

resultado = lambda x: x*2
resultado = map(resultado, lista)
print(list(resultado))
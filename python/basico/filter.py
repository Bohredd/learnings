
# aplica um filtro em um item

def maiorQue10(x):

    return x > 10

lista = [10, 15, 20, 35, 5]

# recebe os booleanos da função
resultado = map(maiorQue10, lista)
resultado = list(resultado)
print(resultado)

# recebe os valores reais do filter
resultado = filter(maiorQue10, lista)
resultado = list(resultado)
print(resultado)

# fazendo a mesma coisa mas com lambda

resultado = filter(lambda x: x > 10, lista)
resultado = list(resultado)
print(resultado)
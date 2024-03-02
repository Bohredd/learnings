
# função lambda
# é uma função pequena sem nome

def somar(x):
    return x + x

soma = somar(5)
print(soma)

# agora a função com lambda

somaLambda = lambda y: y + y
print(somaLambda(5))

somaLambda = lambda x, y: x + y
print(somaLambda(5, 7))


# lambda inside function

def multiplicar(x):
    resultadoLambda = lambda x: x + 2
    return resultadoLambda(x) * 4

print(multiplicar(3))
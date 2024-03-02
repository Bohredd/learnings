

# parametros e args nas functions

# funcao que recebe uma tupla de dados e soma eles
def soma(*numeros):
    return sum(numeros)

soma_numeros = soma(1,2,4)
print(soma_numeros)

# funcao que recebe multiplos dados mas que eles são nomeados diferentemente

def montar_carro(**carro):

    # pode usar *args e **kwargs também

    modelo = carro["modelo"]
    cor = carro["cor"]
    potencia = carro["potencia"]
    return f"Seu carro é um {modelo} da cor {cor} e tem a potência de {potencia} cavalos."

carro = montar_carro(modelo="I30", cor="Prata", potencia="175hp")
print(carro)
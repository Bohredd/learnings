

# montagem de uma lista

cidades = ["Santa Maria", "Porto Alegre", "Araranguá"]
print(cidades)

# adicionar no final da lista

cidades.append("Balneário Camboriú")
cidades.append("Erechim")
print(cidades)

# remover do final da lista

cidades.pop()
print(cidades)

# adicionar em algum lugar da lista

cidades.insert(0, "Agua Santa")
print(cidades)

# remover um item da lista

cidades.remove("Porto Alegre")
print(cidades)

# ordenar a lista

cidades.sort()
print(cidades)

# obter o indice de ocorrência de um determinado valor
localOcorrencia = cidades.index("Balneário Camboriú")
print(localOcorrencia)

# obter o numero de ocorrências de um determino valor
quantidadeOcorrencias = cidades.count("Agua Santa")
print(quantidadeOcorrencias)
cidades.append("Agua Santa")
quantidadeOcorrencias = cidades.count("Agua Santa")
print(quantidadeOcorrencias)

cidades.pop()

# copiar uma lista para outra lista
listaInvertida = cidades.copy()
print(listaInvertida)

# inverter a ordem da lista

listaInvertida.reverse()
print(listaInvertida)

# remover tudo da lista

cidades.clear()
print(cidades)

# concatenar duas listas

letras = ["a", "b", "c"]
numeros = [1, 2, 3]

letras.extend(numeros)
print(letras)

# agregando duas listas
letras = ["a", "b", "c"]
numeros = [1, 2, 3]

listaZipada = zip(letras, numeros)
listaZipada = list(listaZipada)

print(listaZipada)
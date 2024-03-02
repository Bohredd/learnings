

# faça uma coisa se possível, se não mostre o exception do erro

lista = [1, 2, 3]

try:
    valor = lista[3]
    print(valor)
except Exception as error:
    print(error)


lista = [1, 2, 3, 4]

try:
    valor = lista[3]
    print(valor)
except Exception as error:
    print(error)


# else

lista = [1, 2, 3, 4]

try:
    valor = lista[3]
    print(valor)
except Exception as error:
    print(error)
else: # acontece se for válido o try
    print("Existia o valor na lista")

# finally

lista = [1, 2, 3, 4]

try:
    valor = lista[3]
    print(valor)
except Exception as error:
    print(error)
finally: # acontece se for válido o try
    print("Isso aqui acontece mesmo aconteça ou não o erro")

lista = [1, 2, 3]

try:
    valor = lista[3]
    print(valor)
except Exception as error:
    print(error)
finally: # acontece se for válido o try
    print("Isso aqui acontece mesmo aconteça ou não o erro")
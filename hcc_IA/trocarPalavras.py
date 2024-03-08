import json

textoTeste = "bah vsfd piá você é muito pnc"

with open('girias.json') as arquivo:
    girias = json.load(arquivo)

    for valores in girias:
        giria, significado = valores.values()
        if "|" in giria:
            giria = giria.split("|")
            for i in range(len(giria)):
                if giria[i] in textoTeste.split(" "):
                    textoTeste = textoTeste.replace(giria[i], significado)
        else:
            if giria in textoTeste.split(" "):
                textoTeste = textoTeste.replace(giria, significado)

print("Texto arrumado:", textoTeste)

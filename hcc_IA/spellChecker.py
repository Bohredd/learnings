import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from heapq import nlargest
from collections import defaultdict


# Passo 1: Pré-processamento do texto
def preprocessamento(texto):
    # Remover excesso de espaços
    texto = ' '.join(texto.split())

    # Remover stopwords
    stopwords_pt = set(stopwords.words('portuguese'))
    palavras = word_tokenize(texto.lower(), language='portuguese')
    palavras = [palavra for palavra in palavras if palavra not in stopwords_pt]

    # Remover pontuação
    palavras = [palavra for palavra in palavras if palavra not in punctuation]

    # Concatenar em um único parágrafo
    texto_processado = ' '.join(palavras)

    return texto_processado


# Passo 2: Frequência das palavras
def frequencia_palavras(texto):
    freq_palavras = defaultdict(int)
    for palavra in texto.split():
        freq_palavras[palavra] += 1
    return freq_palavras


# Passo 3: Frequência proporcional das palavras
def frequencia_proporcional(freq_palavras):
    max_freq = max(freq_palavras.values())
    for palavra in freq_palavras.keys():
        freq_palavras[palavra] /= max_freq
    return freq_palavras


# Passo 4: Tokenização das sentenças
def tokenizacao_sentencas(texto):
    return sent_tokenize(texto)


# Passo 5: Notas para as sentenças
def notas_sentencas(sentencas, freq_palavras):
    notas = defaultdict(int)
    for i, sentenca in enumerate(sentencas):
        for palavra in sentenca.split():
            if palavra in freq_palavras:
                notas[i] += freq_palavras[palavra]
    return notas


# Passo 6: Ordenação das melhores sentenças
def melhores_sentencas(notas, num_sentencas=3):
    return nlargest(num_sentencas, notas, key=notas.get)


# Passo 7: Geração do resumo
def gerar_resumo(texto, num_sentencas=3):
    texto_processado = preprocessamento(texto)
    freq_palavras = frequencia_palavras(texto_processado)
    freq_proporcional = frequencia_proporcional(freq_palavras)
    sentencas = tokenizacao_sentencas(texto)
    notas = notas_sentencas(sentencas, freq_proporcional)
    melhores = melhores_sentencas(notas, num_sentencas)
    resumo = ' '.join(sentencas[i] for i in sorted(melhores))
    return resumo


# Exemplo de uso:
texto = """
E aí, galera! Tudo certinho? 
Tô aqui pra bater um papo com vocês sobre um lance que tá bombando nas redes sociais, sabe? 
É a nova série que lançaram, tipo, "O Mestre dos Magos". 
Tô ligado que muita gente tá pirando com essa vibe retrô, né?
Mano, eu tava lá no shopping, de boa, quando encontrei o Zé, saca? 
Ele tava mó pilhado falando desse rolezinho que vai rolar no fim de semana. 
Vai ser sinistro, acredita? Vai ter altas atrações, uns sons irados e até uns comes e bebes de graça, tipo, de graça mesmo, de boa!
Mas aí, cê sabe como é, né? Tem sempre uns perrengues no meio do caminho. 
Tipo, a galera fica sem grana ou os rolezinhos ficam lotados demais. 
É mó zuado quando isso acontece, mano.
Ah, e não dá pra esquecer das gírias da quebrada, né? 
Tipo, cê pira nos bagulhos que a gente fala por aqui, é cada coisa louca, mano. 
Tem que tá ligado, senão vira mó mico, saca?
Enfim, é isso aí, galera. 
Bora curtir essa vida louca, mas sem esquecer de dar um toque nos parças quando rolar aquele vacilo no português, beleza? Valeu!
"""

print("Quantia de caracteres antes: ", len(texto))
resumo = gerar_resumo(texto)

print("Quantia de caracteres depois: ", len(resumo))
print(resumo)

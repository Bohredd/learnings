import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline

class HCC_InteligenciaArtificial:

    def __init__(self):
        self.textos = []
        self.categorias = []

        self.modelo = make_pipeline(TfidfVectorizer(), LinearSVC())

    def popular_dados(self, arquivo):

        with open(arquivo, 'r') as arquivoJson:
            dados = json.load(arquivoJson)

        for dado in dados:
            amostra = dado["texto"] if "texto" in dado.keys() else ""
            categoria = dado["categoria"] if "categoria" in dado.keys() else ""
            self.textos.append(amostra)
            self.categorias.append(categoria)

    def treinar_modelo(self):
        self.modelo.fit(self.textos, self.categorias)

    def get_categoria_texto(self, texto):
        return self.modelo.predict([texto])[0]


representanteArtificial = HCC_InteligenciaArtificial()
representanteArtificial.popular_dados('data.json')
representanteArtificial.treinar_modelo()

print(representanteArtificial.get_categoria_texto('bei 7 hora da noite já'))
print(representanteArtificial.get_categoria_texto('hora de jantar'))
print(representanteArtificial.get_categoria_texto('indo almoçar'))
print(representanteArtificial.get_categoria_texto('da pra ir cedinho ai amanhã?'))
print(representanteArtificial.get_categoria_texto('muito tarde pra mim ir'))


from spellchecker import SpellChecker
from enelvo.normaliser import Normaliser

class InteligenciaArtificial:

    def __init__(self, texto: str):
        self.mensagem = texto

    def verificar_abreviacoes(self):
        norm = Normaliser(tokenizer='readable')
        return norm.normalise(self.mensagem)

    def spell_checker(self):
        spell = SpellChecker(language='pt')
        erradas = spell.unknown(self.mensagem.split())

        for palavra in erradas:
            palavra_corrigida = spell.correction(palavra)

            self.mensagem.replace(palavra, palavra_corrigida)
            print(f"Palavra original: {palavra}, Palavra corrigida: {palavra_corrigida}")


ia = InteligenciaArtificial('cacete vsf pqp fdp vc vai se fdr na minha mao')
print(ia.verificar_abreviacoes())
ia.spell_checker()
print(ia.mensagem)
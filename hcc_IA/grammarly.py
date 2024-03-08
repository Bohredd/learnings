from enelvo.normaliser import Normaliser

norm = Normaliser(tokenizer='readable')

# problemas <-

# vc
# n
# pesso
# teinho
# bm
# gd
# vc
# feiozo
# vc
# touxa
# memo

msg = '!vc n responde o que eu pesso ne!teinho uma fome bm gd!vc é feiozo!vc é um touxa memo'

resposta = norm.normalise(msg)
resposta = resposta.split("!")
resposta = "\n".join(resposta)
print(resposta)

xingamentos = "!vsf!pnc!fdp"

resposta = norm.normalise(xingamentos)
resposta = resposta.split("!")
resposta = "\n".join(resposta)
print(resposta)
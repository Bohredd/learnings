from decouple import config
from openai import OpenAI

client = OpenAI(api_key=config("GPT_ACCESS_API_KEY"))


class BotInteligenteHCC:

    def __init__(self, texto: str):
        self.mensagem = texto

    def formalizar_mensagem(self):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Deixe a mensagem informal, formalizada. Retorne apenas o texto formalizado. Texto: {self.mensagem}",
                }
            ],
        )

        return response.choices[0].message.content

    def resumir_mensagem(self):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Resuma a mensagem e deixe-a formalizada. Retorne apenas o texto formalizado e resumido. Texto: {self.mensagem}",
                }
            ],
        )

        return response.choices[0].message.content


bot = BotInteligenteHCC(
    """
    Hj fui p/ a escola c/ mt atraso pq ñ consegui acordar cedo dms. 
    Mts pesss malandr oq ñ ajudou em nd. Mas dpois d 1 xíc d café, td melhorou. 
    Na aula, o prof passo 1 texto q eu ñ intendi nd, mas n vo mentir, tava dms cansado p/ pensar. 
    Depois da aula, peguei 1 busão p/ ir p/ ksa e dormi o trajeto td. 
    Ainda bem q a ksa era perto, pq ñ ia aguentar ficar + 1 min no bus.
    """
)

# print(bot.formalizar_mensagem())
print(bot.resumir_mensagem())

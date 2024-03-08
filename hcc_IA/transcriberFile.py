import speech_recognition as sr

audios = [
    {
        "audio": "queriaInstalacao.wav",
        "textoEsperado": "Fala meu amigo velho tudo bom, cara queria ver se vocês conseguem vir aqui essa semana instalar aquela placa que eu tava vendo queria instalar 3 placas aqui",
    },
    {
        "audio": "falaCupinxa.wav",
        "textoEsperado": "E aí meu cupincha como é que tá",
    }
]
for itens in audios:

    audioFile, textoEsperado = itens.values()
    recognizer = sr.Recognizer()

    with sr.AudioFile(audioFile) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("O que o recog entendeu do áudio:", text)
        print("O que eu falei no audio: ", textoEsperado)
    except sr.UnknownValueError:
        print("entendi nada")
    except sr.RequestError as e:
        print(e)

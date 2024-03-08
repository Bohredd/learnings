import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("micro: ", sr.Microphone)
    print("microfone sendo captado direitinh")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("transcricao:", text)
except sr.UnknownValueError:
    print("nao deu pra entende o audio")
except sr.RequestError as e:
    print(e)

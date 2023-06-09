#recomendo transformar o .py em .bat, não se preocupe! o app continua funcionando sem defeitos.
import datetime
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'ada' in comando:
                comando = comando.replace('ada', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

# os comandos de voz podem ser modificados
#quantas horas são
def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    #pesquisa na wikipedia
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    #tocar musica no youtube
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()




comando_voz_usuario()

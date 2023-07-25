import speech_recognition as sr
import pyttsx3

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    
    try:
        texto = r.recognize_google(audio, language='es-US') # Reconocimiento de voz utilizando Google Speech Recognition
        print("Has dicho: " + texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla")
        return None
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))
        return None

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de habla
    engine.setProperty('volume', 0.9)  # Volumen de habla
    engine.say(texto)
    engine.runAndWait()

# Ejemplo de uso
texto = escuchar()
if texto:
    hablar("Has dicho: " + texto)

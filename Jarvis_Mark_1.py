import speech_recognition as sr 
import pyttsx3
import pywhatkit

name = 'jarvis'
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Klk tu dice?")
        recognizer.adjust_for_ambient_noise(source)
        jarvis = recognizer.listen(source)
        
    try:
        rec = recognizer.recognize_google(jarvis, language='es-ES')
        rec = rec.lower()
    except sr.UnknownValueError:
        print("Repite papi que no te entiendo")
        rec = ""
    
    return rec

def run_jarvis():
    while True:
        rec = listen()
        if "Jarvis" in rec:
            music = rec.replace('jarvis', '').strip()
            print('reproduciendo' + music)
            talk('reproduciendo' + music)
            pywhatkit.playonyt(music) 
            
if __name__ == "__main__":
    run_jarvis()
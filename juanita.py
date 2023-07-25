import speech_recognition as sr
import pyttsx3 
import pywhatkit

name = "juanita"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    
def listen():
    rec = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec.strip()

def juanita():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '').strip()
        print("Reproduciendo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)
        
if __name__ == '__main__':
    juanita()

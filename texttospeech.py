import pyttsx3

def speaknow(string):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',145)
    engine.say(string)
    engine.runAndWait()
    engine.stop()

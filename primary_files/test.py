import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say("I will speak this text")
engine.runAndWait()
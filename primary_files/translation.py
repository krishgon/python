# import all the superpowers
from googletrans import Translator
import pyttsx3

# set the speak system
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-75)

# set the tranlator
translator= Translator() 

# take text from the user to translate
toTranslate = input("Type what you want to convert in English: ")

# tranlate and store in a dabba
translation= translator.translate(toTranslate) 

# speak and print translation
engine.say(translation.text)
print(translation.text)

# tell the computer to wait until the speaker finishes speaking
engine.runAndWait()
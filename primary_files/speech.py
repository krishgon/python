import speech_recognition

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("say something!")
    audio = recognizer.listen(source)

print("You probably said: ")
print(recognizer.recognize_google(audio))
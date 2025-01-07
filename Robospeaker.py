import pyttsx3

engine = pyttsx3.init()

while True:
    speak = input("Enter text to speak: ")

    if speak != 'q':
        engine.say(speak)  # This tells the engine to say the input text
        engine.runAndWait()  # This makes the engine actually speak

    else:
        print("Thank you for using Robo Speaker!!")
        break

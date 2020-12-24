import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how  may I help you")


def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n:")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak('Say that again please...')
        return "None"
    return query


def fibonacci(number):
    if number < 0:
        speak('Invalid number sir! Fibonacci! is not defined for negative number sir!')
        print('Invalid number sir! Fibonacci! is not defined for negative number sir!')
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return(fibonacci(number-1) + fibonacci(number-2))

if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'play music v'in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[5])
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            speak('sure sir!')
            exit()

        elif 'who are you' in query:
            speak('I am your AI assistant sir, made by you on 13th june thursday at 10:30am.')

        elif 'who is nitesh pandey' in query:
            speak('He is one of very intelligent person, studying computer science in  Ghaziabad and also he is my creator sir.')

        elif 'who is pappu' in query:
            speak("He is father of Neha pandey, that is Nitesh's sister.")

        elif 'play music 4'in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[4])
            os.startfile(os.path.join(music_dir, songs[4]))

        elif 'who is abhishek pandey' in query:
            speak("He is Nitesh's younger brother and also son of Shri Meenu Pandey.")

        elif 'who is meenu pandey' in query:
            speak("She is Nitesh's mother and presently living in pandeypur,varanasi.")

        elif 'who is neha pandey' in query:
            speak("She is nitesh's sister and ,also her nickname is 'choota!',she is very daayan ladkii!.")

        elif 'what can you do jarvis' in query:
            speak('I can do the tasks which are programmed in me.')

        elif 'play music 3'in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[3])
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'play music 2' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[2])
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'play music one' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[1])
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play music 0' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[0])
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music 6' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[6])
            os.startfile(os.path.join(music_dir, songs[6]))

        elif 'play music 7' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[7])
            os.startfile(os.path.join(music_dir, songs[7]))

        elif 'hello jarvis' in query:
            speak('Hello sir! Its my pleasure to talk with you!')

        elif 'play music 8' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[8])
            os.startfile(os.path.join(music_dir, songs[8]))

        elif 'play music 9' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[9])
            os.startfile(os.path.join(music_dir, songs[9]))

        elif 'play music 10' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs[10])
            os.startfile(os.path.join(music_dir, songs[10]))

        elif 'shutdown' in query:
            speak('Shutting down sir! I hope you will start me soon sir! ')
            os.system("shutdown /s /t 1");

        elif 'check number is even or odd' in query:
            speak('What is the number sir?')
            print('what is the number sir?')
            number = takeCommand()
            if number == 'zero':
                print('Number is neither even! nor odd sir!')
                speak('Number is neither even!nor odd sir!')
            else:
             speak('Say again your natural number sir!')
             print('Say again your natural number sir!')
             number = int(takeCommand())
             print(number)
             if number % 2 ==0:
                print('Its even number sir!')
                speak('Its even number sir!')

             else:
                speak('Its odd number sir!')
                print('Its odd number sir!')

        elif 'who made you' in query:
            speak('My Sir! Nitesh Pandey!')

        elif 'generate fibonacci series' in query:
            speak('Upto which number sir!')
            print('Upto which number sir!')
            number = takeCommand()
            if number == 'zero':
                print('0')
                speak('0')
            else:
                speak('Say  your natural number again sir!')
                print('Say your natural number again sir!')
                number = int(takeCommand())
                for i in range(number):
                    print(fibonacci(i))
                    speak(fibonacci(i))

        elif 'i am bored' in query:
            speak('I can play music sir!Tell me Which song sir!')
            print('I can play music sir!Tell me Which song sir!')

        elif 'check number is armstrong or not' in query:
            print('What is the the number')
            speak('What is the number sir!')
            number = int(takeCommand())
            order = len(str(number))
            sum = 0
            temp = number
            while temp > 0:
                digit = temp % 10
                sum += digit ** order
                temp //= 10
            if sum == number:
                print('Number is armstrong sir!')
                speak('Number is armstrong sir!')
            else:
                print('Number is not armstrong sir!')
                speak('Number is not armstrong sir!')

        elif 'generate maths table for a number' in query:
            print('What is the natural number sir!')
            speak('What is the natural number sir!')
            number = int(takeCommand())
            for i in range(1, 11):
                product = number * i
                print('{} x {} = {}'.format(number, i, product))




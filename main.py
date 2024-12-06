import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "2b293cd9c511439db5e50e394b0a85c3"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=2b293cd9c511439db5e50e394b0a85c3")

        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles',[])
            # Extract and print headlines

            for article in articles:
                speak(article['title'])

    else:
        #let OpenAI handle the request:
        pass  






if __name__ == "__main__":
    speak("initializing jarvis...")

    while True:
        #listen for wake word "jarvis"
        r = sr.Recognizer()
       
        print("Recognizing..")

        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                #listen for command:
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    
        
        except Exception as e:
            print("Error;{0}".format(e))
    

    


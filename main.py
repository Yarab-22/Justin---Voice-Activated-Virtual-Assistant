import speech_recognition as sr        # for converting audio to text
import pyttsx3                         # for making the assistant to speek
import webbrowser                      # for opening websites
import MusicLibrary                    # music links stored here
import os
from google import genai               # gemini AI model integration

engine = pyttsx3.init()

def speak(text):                       # function for speaking
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 160)     # setting up new voice rate
    engine.say(text)
    engine.runAndWait()

with open("key.txt", "r") as f:             
    API_KEY= f.read().strip()

client = genai.Client(api_key=API_KEY)

def aiprocess(content):                         # send whatever user said to Gemini AI and make it talk back
    """
    Sends a user query to Gemini and reads the response aloud.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=[
            {"role": "system", "content": "You are a virtual assistant named Justin skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": content}
        ]
    )

    speak(response.text)





def ProcessCommand(c):                         # check what the user wants and do it
    if "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c:
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
  
    elif "play" in c:
        song = c.split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    else:
        aiprocess(c)




if __name__ == "__main__":
    print("Initializing Justin....")
    speak("Initializing Justin....")

    while True:
                
        r = sr.Recognizer()

        print("Recognizing...")
        
        try:
            # obtain audio from the microphone

            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout= 2, phrase_time_limit= 1)

            
            word = r.recognize_google(audio)

            if (word.lower() == "Justin"):            # Wake word
                speak("Yes Master..")
                
                with sr.Microphone() as source:
                    print("Justin is active..")
                    audio = r.listen(source)

                command = r.recognize_google(audio)         # command

                ProcessCommand(command.lower())


        except Exception as e:                     # if any error, print it
            print("error; {0}".format(e))



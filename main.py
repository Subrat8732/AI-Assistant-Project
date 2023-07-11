import speech_recognition as sr
import os
import pyttsx4
import webbrowser
import datetime
import openai
from config import apikey
import random

chatStr=""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Subrat : {query}\n Phoenix : "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a try catch block
    speak.say(response["choices"][0]["text"])
    speak.runAndWait()
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    with open(f"OpenAI\\{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n**************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI\\{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)

# initialisation
speak = pyttsx4.init()

def SpeakText(command):
    speak.say(command)
    speak.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #wait for recognizer to adjust the energy threshold
        r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            user_said = r.recognize_google(audio, language="en-in")
            print(f"User said: {user_said}")
            #for repeating what user said to assistant
            #SpeakText(user_said)
            return user_said
        except Exception as e:
            return "Some Error Occurred. Sorry from Phoenix"

if __name__=='__main__':
    # testing
    speak.say("Hello my name is Phoenix, I am your AI assistant")
    speak.runAndWait()
    while True:
        print("Listening...")
        query = takeCommand()

        # todo: Add a feature to open specific websites
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["spotify","https://www.spotify.com"],["whatsapp","https://www.whatsapp.com"],["instagram","https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak.say(f"Opening {site[0]} sir...")
                speak.runAndWait()
                webbrowser.open(site[1])

        #date and time module to tell what is the current time
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak.say(f"Sir the time is {hour} hours and {min} minutes")
            speak.runAndWait()

        # todo: Add a feature to play a specific song
        elif "open music" in query:
            musicPath = "C:\\Users\\Subrat\\Music\\Believer.mp3"
            os.system(f"{musicPath}")

        # todo: Add a feature to open a specific app
        elif "open zoom".lower() in query.lower():
            os.system(f"C:\\Users\\Subrat\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        # todo: Using OpenAI
        elif "Using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "great work" in query:
            speak.say("Thank you sir, it's my pleasure")
            speak.runAndWait()
            exit()

        else:
            chat(query)
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import datetime
import time
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("Api_key")  #add your api key here to runthis code
if not api_key:
    print("ERROR: OpenAI API key not found. Please add it to your .env file as Api_key=sk-... and restart.")
    exit(1)
openai.api_key = api_key

# Speak function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


    
def processCommand(c):
    
    #opening any websites
    if c.startswith("open"):
        c = c.replace("open", "")
        c = c.strip()
        try:
            speak(f"Opening {c} for you.")
            wb.open("http://" + c)
        except:
            speak("Sorry, I couldn't open that website.")
            
    
    elif  "time" in c:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    
    elif "date" in c:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    
    elif "talk" in c or "speak" in c:     
        speak("I am Cyrus, your personal assistant. Let's chat! Say 'stop' to end our conversation.")
        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            try:
                user_input = r.recognize_google(audio).lower()
                if "stop" in user_input or "exit" in user_input:
                    speak("Okay, ending our conversation, thank you")
                    break
                elif "how are you" in user_input:
                    speak("I'm doing well, thank you! How can I assist you today?")
                else:
                    # Use OpenAI to generate a response (new API style)
                    try:
                        client = openai.OpenAI(api_key=api_key)
                        response = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are Cyrus, a helpful voice assistant."},
                                {"role": "user", "content": user_input}
                            ]
                        )
                        answer = response.choices[0].message.content
                        speak(answer)
                    except Exception as e:
                        print(f"OpenAI error: {e}")
                        speak("Sorry, I could not get an answer from OpenAI.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Please repeat.")
        

    
    
    
    
# Main function
if __name__ == "__main__":
    speak("Initializing Cyrus...")
    time.sleep(0.5)
    speak("Welcome Rohan, how may I help you?")
    
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
          speak("cyrus is Active,what do you want me to do?")
          print("Listening...")
          audio = r.listen(source)
          
        command = r.recognize_google(audio)
        
        processCommand(command.lower())
        
    
            
    except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
                
    
    
    
        
   
     
            
   
   
        

 
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




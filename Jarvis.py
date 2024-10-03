import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import datetime
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice, use voices[0].id for male

# WolframAlpha API key
app_id = "KPA637-J82R3VUKHR"  # Replace with your WolframAlpha API key
client = wolframalpha.Client(app_id)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # You can change language to 'en-us'
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    
    return query.lower()

# Function to tell the current time
def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")

# Function to search Wikipedia
def search_wikipedia(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

# Function to open a website
def open_website(website):
    webbrowser.open(f"https://{website}.com")
    speak(f"Opening {website}")

# Function to perform calculations or answer questions using WolframAlpha
def ask_wolfram(query):
    try:
        res = client.query(query)
        answer = next(res.results).text
        speak(f"The answer is {answer}")
    except Exception:
        speak("Sorry, I couldn't find the answer.")

# Main function where the assistant listens and responds
if __name__ == "__main__":
    speak("Hello Boss, this is Jarvis. How can I help you today?")
    
    while True:
        query = take_command()

        if 'time' in query:
            tell_time()

        elif 'wikipedia' in query:
            search_wikipedia(query)

        elif 'open youtube' in query:
            open_website("youtube")

        elif 'open google' in query:
            open_website("google")

        elif 'calculate' in query or 'what is' in query:
            ask_wolfram(query)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

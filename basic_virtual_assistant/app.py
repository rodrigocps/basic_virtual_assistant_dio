# Import Libraries
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import wikipedia
import webbrowser
import pyjokes
from pygame import mixer
import time

mixer.init()

wikipedia.set_lang('en')

def speak(text_to_speak, lang='en'):

    try:
        tts = gTTS(text=text_to_speak, lang=lang, slow=False)
        
        audio_file = 'response.mp3'
        tts.save(audio_file)

        mixer.music.load(audio_file)
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(0.1)

        mixer.music.unload()
            
    except Exception as e:
        print(f"Error in speak function: {e}")

def get_voice_command():

    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:

        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening... Please speak your command.")

        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            print("Processing...")

            command = recognizer.recognize_google(audio_data, language='en-US')
            print(f"You said: {command}")
            return command.lower()
            
        except sr.WaitTimeoutError:
            print("Listening timed out. No command received.")
            return ""
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google service; {e}")
            return ""
        except Exception as e:
            print(f"Error in get_voice_command: {e}")
            return ""

def run_virtual_assistant():

    greeting = "Hello! I am your virtual assistant. Say a command."
    print(greeting)
    speak(greeting)
    
    while True:

        command = get_voice_command()
        
        if not command:
            continue

        # 1. Exit Command
        if 'stop' in command or 'exit' in command or 'bye' in command:
            farewell = "Understood. Shutting down. Goodbye!"
            print(farewell)
            speak(farewell)
            break

        # 2. Wikipedia Search
        elif 'wikipedia' in command:
            search_term = command.replace('search on wikipedia', '').replace('wikipedia', '').strip()
            
            if not search_term:
                speak("What would you like me to search on Wikipedia?")
                search_term = get_voice_command()

            if search_term:
                try:
                    speak(f"Searching for {search_term} on Wikipedia...")
                    summary = wikipedia.summary(search_term, sentences=2)
                    print(f"Wikipedia result: {summary}")
                    speak(summary)
                except wikipedia.exceptions.PageError:
                    speak(f"Sorry, I could not find the page for {search_term}.")
                except Exception as e:
                    speak("An error occurred while searching on Wikipedia.")

        # 3. Open YouTube
        elif 'youtube' in command:
            search_term = command.replace('open youtube', '').replace('youtube', '').strip()
            
            if not search_term:
                speak("What would you like to search on YouTube?")
                search_term = get_voice_command()

            if search_term:
                url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
                speak(f"Opening YouTube with search for {search_term}.")
                webbrowser.open(url)

        # 4. Nearby Pharmacy
        elif 'pharmacy' in command or 'drugstore' in command:
            url = "https://www.google.com/maps/search/pharmacy+nearby"
            speak("Showing nearby pharmacies on Google Maps.")
            webbrowser.open(url)

        # 5. Tell a Joke
        elif 'joke' in command:
            joke = pyjokes.get_joke(language='en', category='neutral')
            print(f"Joke: {joke}")
            speak(joke)

        # 6. Date and Time
        elif 'date' in command:
            today = datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {today}")
        
        elif 'time' in command:
            now = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        else:
            response = "Sorry, I did not understand that command. Can you repeat?"
            print(response)
            speak(response)

if __name__ == "__main__":
    run_virtual_assistant()
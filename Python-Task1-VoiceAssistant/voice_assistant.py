import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus


# -----------------------------
# Initialize voice components
# -----------------------------
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty("rate", 170)


# -----------------------------
# Text-to-speech function
# -----------------------------
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Listen to user's voice
# -----------------------------
def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


# -----------------------------
# Tell date and time
# -----------------------------
def tell_date_time(command):

    now = datetime.datetime.now()

    if "time" in command:
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in command or "today" in command:
        current_date = now.strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}.")


# -----------------------------
# Web search
# -----------------------------
def search_web(command):

    search_words = [
        "search for",
        "search",
        "google",
        "look up"
    ]

    topic = command

    for word in search_words:
        if word in topic:
            topic = topic.replace(word, "", 1)
            break

    topic = topic.strip()

    if topic:
        speak(f"Searching the web for {topic}.")
        url = "https://www.google.com/search?q=" + quote_plus(topic)
        webbrowser.open(url)
    else:
        speak("What would you like me to search for?")


# -----------------------------
# Process commands
# -----------------------------
def process_command(command):

    if not command:
        return True

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Exit command
    elif (
        "goodbye" in command
        or "exit" in command
        or "quit" in command
        or "stop" in command
    ):
        speak("Goodbye! Have a nice day.")
        return False

    # Time and date
    elif "time" in command or "date" in command or "today" in command:
        tell_date_time(command)

    # Web search
    elif (
        "search" in command
        or "google" in command
        or "look up" in command
    ):
        search_web(command)

    else:
        speak(
            "I don't know that command yet. "
            "You can say hello, ask for the time or date, "
            "or ask me to search the web."
        )

    return True


# -----------------------------
# Main program
# -----------------------------
def main():

    speak(
        "Voice assistant started. "
        "You can say hello, ask for the time or date, "
        "or ask me to search the web."
    )

    running = True

    while running:
        command = listen()
        running = process_command(command)


# Start the assistant
if __name__ == "__main__":
    main()
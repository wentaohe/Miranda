import sys
import speech_recognition
import pyttsx3 as tts

class CustomIntentMethods():
    def __init__(self, speaker):
        self.speaker = speaker

    def custom_intents(self):
        mappings = {'greeting' : self.function_for_greetings, 'stocks' : self.function_for_stocks, 'goodbye' : self.function_for_goodbye, 'exavault_constructor' : self.function_for_exavault_constructor}

        return mappings

    def function_for_greetings(self):
        self.speaker.say("Hello how are you doing!")
        self.speaker.runAndWait()
        # Some action you want to take

    def function_for_stocks(self):
        self.speaker.say("You own the following shares: ABBV, AAPL, FB, NVDA and an ETF of the S&P 500 Index!")
        self.speaker.runAndWait()
        # Some action you want to take

    def function_for_goodbye(self):
        self.speaker.say("Sad to see you go :(")
        self.speaker.runAndWait()
        sys.exit(0)

    def function_for_exavault_constructor(self):
        recognizer = speech_recognition.Recognizer()

        self.speaker.say("Running Exavault Constructor 1.0.0.")

        done = False
        while not done:
            try:
                with speech_recognition.Microphone() as mic:
                    self.speaker.say("What is your name?")
                    self.speaker.runAndWait()
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    name = recognizer.recognize_google(audio)
                    name = name.lower()

                    self.speaker.say(f"Hello {name} what is your email?")
                    self.speaker.runAndWait()
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    email = recognizer.recognize_google(audio)
                    email = email.lower()

                    self.speaker.say(f"What is the cherry version?")
                    self.speaker.runAndWait()
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    cherre_version = recognizer.recognize_google(audio)
                    cherre_version = cherre_version.lower()

                    self.speaker.say(f"What is the project name?")
                    self.speaker.runAndWait()
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    project_name = recognizer.recognize_google(audio)
                    project_name = project_name.lower()

                    self.speaker.say(f"Congratz {name}, successfully created exavault {project_name} for cherry version {cherre_version}!")
                    self.speaker.runAndWait()

                    done = True
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                self.speaker.say(f"Sorry I did not catch that.")
                self.speaker.runAndWait()
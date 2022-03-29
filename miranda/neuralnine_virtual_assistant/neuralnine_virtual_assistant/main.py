from virtual_assistant import GenericAssistant
import pyttsx3 as tts
import speech_recognition

if __name__ == "__main__":
    assistant = GenericAssistant('intents.json', model_name="test_model")
    assistant.train_model()

    # done = False

    # while not done:
    #     message = input("Enter a message: ")
    #     if message == "STOP":
    #         done = True 
    #     else:
    #         assistant.request(message)

    speaker = tts.init()
    speaker.setProperty('rate', 165)
    #speaker.setProperty('voice', 'com.apple.speech.synthesis.voice.Fred')

    # engine = tts.init()
    # engine.setProperty('rate', 175)
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice, voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say("Hello World!")
    #     engine.runAndWait()
    #     engine.stop()

    recognizer = speech_recognition.Recognizer()
    ########################################################################################################
    ########################################################################################################

    speaker.say("I am become aware. Hello master Nikolai.")
    speaker.runAndWait()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                message = message.lower()

            assistant.request(message)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
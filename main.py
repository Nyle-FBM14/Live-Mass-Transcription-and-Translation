import os
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    while True:
        audio = r.listen(source)

        # recognize speech using whisper
        try:
            print(r.recognize_whisper(audio, language="english"))
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Whisper; {e}")
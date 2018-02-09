#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def translate(audio):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(r.recognize_google(audio))

# obtain audio from the microphone
r = sr.Recognizer()
print("Say something!")
with sr.Microphone() as source:
    while True:
    	audio = r.listen(source)
    	translate(audio)


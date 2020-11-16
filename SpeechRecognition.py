import speech_recognition as sr
import pyttsx3 as pt
import pyaudio

r = sr.Recognizer()

# to connect mic device using python pyAudio library
with sr.Microphone() as source:

    print('start saying......')
    pt.speak('start saying')

    # on and off the mic after listening audio source
    myaudio = r.listen(source)

    pt.speak('speech done')
    print('speech done....')

    data = r.recognize_google(myaudio)

    print('\n************output*************')

    print(data)
    pt.speak(data)

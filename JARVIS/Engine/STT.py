# File for Jarvis conversion of speech into text

import subprocess

try :
    import speech_recognition as sr
except ModuleNotFoundError:
    subprocess.run("pip install SpeechRecognition")
    subprocess.run("pip install pyAudio")
    import speech_recognition as sr

def STT():
    r = sr.Recognizer()
    r.dynamic_energy_adjustment_damping = 0.3
    r.dynamic_energy_ratio = 0.9
    r.dynamic_energy_threshold = False
    r.pause_threshold = 0.5
    r.operation_timeout = None
    r.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        print("Speak Now...", flush=True)
        try:
            ad = r.listen(source)
            print("processing...", flush=True)
            text = r.recognize_google(ad, language="en-IN")
            print(f"You said: {text}")
            return text
        except Exception as e:
            pass

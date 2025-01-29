from Engine.STT import STT
from Engine.TTS import TTS
from Brain.Brain import get_answer
import webbrowser

try:
    import pywhatkit as kt
    import subprocess
except ModuleNotFoundError:
    subprocess.run("pip install pywhatkit")   
    import pywhatkit as kt
except FileNotFoundError:
    subprocess.run("pip install pywhatkit") 
    import pywhatkit as kt

print("Please enter 1 or 2 for the Input of JARVIS AI Model")
print("1: Manually Use the JARVIS AI Model")
print("2: Automatic Speech Recognition using the JARVIS AI Model")
x = int(input())

if x == 1:
    while True:
        text = input()
        if text == None:
            continue
        text = text.lower()


        if "search in youtube" in text:
            text = text.replace("search in youtube", "")
            text = text.replace("jarvis", "")
            TTS("Searching about your request sir")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            TTS(f"Search Results {text}")

        if "search in google" in text:
            text = text.replace("search in google", "")
            text = text.replace("jarvis", "")
            # To replace key strokes
            text = text.replace("who is", "")
            text = text.replace("what is", "")
            TTS("Searching about your request sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"Search Results {text}")

        if "music on youtube" in text:
            text = text.replace("music on youtube", "")
            text = text.replace("play", "")
            TTS(f"Playing your music {text}")
            kt.playonyt(text)

        
        if "jarvis stop" in text:
            quit()

        if "jarvis" in text:
            text = text.replace("jarvis", "")
            text = text.replace("who is", "")
            text = text.replace("what is", "")
            TTS(get_answer(text))


if x == 2:
    while True:
        text = STT()
        if text == None:
            continue
        text = text.lower()

        if "search in youtube" in text:
            text = text.replace("search in youtube", "")
            text = text.replace("jarvis", "")
            TTS("Searching about your request sir")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            TTS(f"Search Results {text}")

        if "search in google" in text:
            text = text.replace("search in google", "")
            text = text.replace("jarvis", "")
            # To replace key strokes
            text = text.replace("who is", "")
            text = text.replace("what is", "")
            TTS("Searching about your request sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"Search Results {text}")

    
        if "music on youtube" in text:
            text = text.replace("music on youtube", "")
            text = text.replace("play", "")
            TTS(f"Playing your music {text}")
            kt.playonyt(text)
     
        if "jarvis stop" in text:
            quit()
        
        if "jarvis" in text:
            text = text.replace("jarvis", "")
            text = text.replace("who is", "")
            text = text.replace("what is", "")
            TTS(get_answer(text))




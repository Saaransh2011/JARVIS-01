try:
    import webbrowser
    import wikipedia
    import subprocess
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install wikipedia')
    subprocess.run('pip install webbrowser')
except FileNotFoundError:
    import subprocess
    subprocess.run('pip install wikipedia')
    subprocess.run('pip install webbrowser')

from Engine.TTS import TTS
def get_answer(text):
    try:
        return wikipedia.summary(text, sentences = 2)
    except Exception:
        TTS("Searching about your request sir")
        webbrowser.open(f"https://www.google.com/search?q={text}")
        TTS(f"Search Results {text}")
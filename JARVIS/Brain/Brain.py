try:
    import webbrowser
    import wikipedia
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install wikipedia')

from Engine.TTS import TTS
def get_answer(text):
    try:
        return wikipedia.summary(text, sentences = 2)
    except Exception:
        TTS("Searching about your request sir")
        webbrowser.open(f"https://www.google.com/search?q={text}")
        TTS(f"Search Results {text}")
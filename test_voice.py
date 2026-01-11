import pyttsx3

print("Testing TTS engine...")

try:
    engine = pyttsx3.init()
    print("Engine initialized successfully")
    
    print("Available voices:")
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")
    
    print("Testing speech...")
    engine.say("Hello, this is a test")
    engine.runAndWait()
    print("Speech test completed")
    
except Exception as e:
    print(f"TTS Error: {e}")
    print("TTS engine not working properly")
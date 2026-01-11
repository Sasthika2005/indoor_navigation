import pyttsx3

print("Testing TTS audio...")
engine = pyttsx3.init()
engine.say("Hello, can you hear me?")
engine.runAndWait()
print("Test completed")
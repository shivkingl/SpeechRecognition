import speech_recognition as sr

def listen_and_convert_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as source
    with sr.Microphone() as source:
        print("Please say something...")
        
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Listen for the user's input
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError:
            print("Sorry, there was a problem with the request")

# Ensure the required packages are installed
try:
    import distutils
except ModuleNotFoundError:
    print("Installing setuptools to ensure distutils is available...")
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "setuptools"])

# Run the function
listen_and_convert_to_text()
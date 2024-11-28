"""

    pip install speechrecognition
    pip install pyaudio
    
"""

import speech_recognition as speech_rc


## Inicializar el reconocimiento de voz
recognizer = speech_rc.Recognizer()

## Inicializar micrófono
with speech_rc.Microphone() as source:
    print("Dí algo")
    audio = recognizer.listen(source)
    

try:
    text = recognizer.recognize_google(audio, language="es-Es")
    print("Texto reconocido: " + text)
except speech_rc.UnknownValueError as err:
    print(f"No se reconocidió el audio {err} ")
except speech_rc.RequestError as err:
    print(f"Error en la solicitud {err}")    
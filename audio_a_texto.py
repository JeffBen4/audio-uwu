import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import os

def convertir_mp3_a_wav(ruta_mp3):
    wav_path = ruta_mp3.replace(".mp3", ".wav")
    audio = AudioSegment.from_mp3(ruta_mp3)
    audio.export(wav_path, format="wav")
    return wav_path

def audio_a_texto(nombre_archivo):
    # Convertir a WAV si es MP3
    if nombre_archivo.endswith(".mp3"):
        nombre_archivo = convertir_mp3_a_wav(nombre_archivo)

    r = sr.Recognizer()
    try:
        with sr.AudioFile(nombre_archivo) as source:
            print("Procesando audio...")
            audio = r.record(source)
        texto = r.recognize_google(audio, language="es-PE")
        print("Texto reconocido:")
        print(texto)
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error con el servicio de reconocimiento: {e}")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def texto_a_audio():
    texto = input("Escribe el texto que deseas convertir a audio: ")
    tts = gTTS(text=texto, lang="es")
    tts.save("voz_generada.mp3")
    print("Audio guardado como voz_generada.mp3")
    try:
        from playsound import playsound
        playsound("voz_generada.mp3")
    except:
        print("No se pudo reproducir el audio, pero fue guardado correctamente.")

def menu():
    while True:
        print("\n--- Conversor de Voz y Texto ---")
        print("1. Convertir audio (.wav o .mp3) a texto")
        print("2. Convertir texto a audio")
        print("3. Salir")
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            archivo = input("Escribe el nombre del archivo (con extensión .wav o .mp3): ")
            audio_a_texto(archivo)
        elif opcion == "2":
            texto_a_audio()
        elif opcion == "3":
            print("¡Hasta luego, uwu!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile
import sounddevice as sd
import numpy as np


def speech_to_text_google_file(audio_path: str) -> str:
    """
    Convert MP3/WAV audio file to text using Google Speech Recognition.
    """

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio not found: {audio_path}")

    recognizer = sr.Recognizer()
    temp_wav = None

    try:
        # ---- Convert MP3 to WAV if needed ----
        if audio_path.lower().endswith(".mp3"):
            sound = AudioSegment.from_mp3(audio_path)
            sound = sound.set_frame_rate(16000).set_channels(1)

            temp_wav = tempfile.NamedTemporaryFile(
                suffix=".wav", delete=False
            ).name
            sound.export(temp_wav, format="wav")
            audio_path = temp_wav

        # ---- Load audio file ----
        with sr.AudioFile(audio_path) as source:
            # recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.record(source)

        # ---- Google STT ----
        return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        raise RuntimeError("Google STT could not understand the audio file.")

    except sr.RequestError as e:
        raise RuntimeError(f"Google STT request failed: {e}")

    finally:
        if temp_wav and os.path.exists(temp_wav):
            os.remove(temp_wav)



def beep(freq=880, duration=0.15, volume=0.5):
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    sd.play(volume * tone, fs)
    sd.wait()


def speech_to_text_google_mic(max_retries: int = 3):
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.8
    recognizer.phrase_threshold = 0.3
    recognizer.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        print("🔔 Ready")
        beep(freq=700)          # START BEEP (lower tone)

        recognizer.adjust_for_ambient_noise(source, duration=1)

        for attempt in range(1, max_retries + 1):
            try:
                print("🎤 Listening... Speak now")
                audio = recognizer.listen(source)

                beep(freq=1200)   # END BEEP (higher tone)
                print("🛑 Recording finished")
                print("🧠 Transcribing...")

                text = recognizer.recognize_google(audio)
                print("📝 You said:", text)


                return text

            except sr.UnknownValueError:
                beep(freq=400)
                print(f"⚠️ Could not understand audio (attempt {attempt}/{max_retries}). Try again.")

            except sr.RequestError as e:
                raise RuntimeError(f"Google STT request failed: {e}")

    print("❌ Speech could not be recognized.")
    return ""
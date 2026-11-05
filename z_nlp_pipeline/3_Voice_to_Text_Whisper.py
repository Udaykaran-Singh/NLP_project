import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os


def speech_to_text_whisper(audio_path=None, duration=8):
    model = whisper.load_model("base")

    if audio_path:
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio not found: {audio_path}")
        result = model.transcribe(audio_path)
        return result["text"]

    print("Recording from microphone...")
    audio = sd.rec(int(duration * 16000), samplerate=16000, channels=1, dtype="int16")
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav.write(tmp.name, 16000, audio)
        result = model.transcribe(tmp.name)

    return result["text"]

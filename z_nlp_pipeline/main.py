import importlib.util
import os
import time

# ===============================
# Utility functions
# ===============================

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sanitize_path(p):
    return p.strip().strip("'").strip('"')


# ===============================
# Base directory
# ===============================

BASE = os.path.dirname(os.path.abspath(__file__))

# ===============================
# Load pipeline modules
# ===============================

ocr = load_module("ocr", f"{BASE}/1_OCR_2.py")
google = load_module("google", f"{BASE}/2_Voice_to_Text_google.py")
whisper = load_module("whisper", f"{BASE}/3_Voice_to_Text_Whisper.py")
corrector = load_module("corrector", f"{BASE}/4_Text_Correction.py")
summarizer = load_module("summarizer", f"{BASE}/5_Text_Summary_Better.py")
tts = load_module("tts", f"{BASE}/6_Text_to_Speech.py")
utils = load_module("utils", f"{BASE}/utils.py")

# ===============================
# Main pipeline
# ===============================

def main():

    print("\n====== NLP PIPELINE MENU ======")
    print("1. OCR (Image → Text)")
    print("2. Google STT (Microphone)")
    print("3. Google STT (Audio File)")
    print("4. Whisper (Microphone)")
    print("5. Whisper (Audio File) [RECOMMENDED]")
    print("0. Exit")

    choice = input("Enter choice: ").strip()
    raw_text = ""

    # ===============================
    # Start END-TO-END timer
    # ===============================
    pipeline_start = time.time()

    # ---------- INPUT STAGE ----------
    if choice == "1":
        p = sanitize_path(input("Enter image path: "))
        t1 = time.time()
        raw_text = ocr.run_ocr(p)
        t2 = time.time()
        print(f"OCR Time: {t2 - t1:.2f} seconds")

    elif choice == "2":
        t1 = time.time()
        raw_text = google.speech_to_text_google_mic()
        t2 = time.time()
        print(f"Google STT (Mic) Time: {t2 - t1:.2f} seconds")

    elif choice == "3":
        p = sanitize_path(input("Enter audio file path: "))
        t1 = time.time()
        raw_text = google.speech_to_text_google_file(p)
        t2 = time.time()
        print(f"Google STT (File) Time: {t2 - t1:.2f} seconds")

    elif choice == "4":
        t1 = time.time()
        raw_text = whisper.speech_to_text_whisper()
        t2 = time.time()
        print(f"Whisper STT (Mic) Time: {t2 - t1:.2f} seconds")

    elif choice == "5":
        p = sanitize_path(input("Enter audio file path: "))
        t1 = time.time()
        raw_text = whisper.speech_to_text_whisper(audio_path=p)
        t2 = time.time()
        print(f"Whisper STT (File) Time: {t2 - t1:.2f} seconds")

    elif choice == "0":
        print("Exiting pipeline.")
        return

    else:
        print("Invalid choice.")
        return

    if not raw_text or not raw_text.strip():
        print("No text extracted.")
        return

    # ---------- TEXT CORRECTION ----------
    t1 = time.time()
    corrected_text = corrector.correct_text(raw_text)
    t2 = time.time()
    print(f"Text Correction Time: {t2 - t1:.2f} seconds")

    # ---------- SUMMARIZATION ----------
    t1 = time.time()
    summary = summarizer.summarize_text(corrected_text)
    t2 = time.time()
    print(f"Summarization Time: {t2 - t1:.2f} seconds")

    # ---------- CLEANUP ----------
    t1 = time.time()
    final_summary = utils.clean_summary_text(summary)
    t2 = time.time()
    print(f"Post-processing Time: {t2 - t1:.2f} seconds")

    # ---------- OUTPUT ----------
    print("\n===== FINAL SUMMARY =====\n")
    print(final_summary)

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write("\n\n===== SUMMARY =====\n")
        f.write(final_summary)

    # ---------- OPTIONAL TTS ----------
    if input("\nEnable TTS? (y/n): ").lower() == "y":
        t1 = time.time()
        tts.text_to_speech(final_summary, "summary_audio.mp3")
        t2 = time.time()
        print(f"TTS Time: {t2 - t1:.2f} seconds")

    # ===============================
    # END-TO-END METRIC
    # ===============================
    pipeline_end = time.time()
    print("\n==============================")
    print(f"End-to-End Pipeline Time: {pipeline_end - pipeline_start:.2f} seconds")
    print("==============================")

# ===============================
# Entry point
# ===============================

if __name__ == "__main__":
    main()

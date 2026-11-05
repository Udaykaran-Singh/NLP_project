# NLP Pipeline – Multimodal Natural Language Processing System

An end-to-end **Natural Language Processing (NLP) Pipeline** that accepts three different input modalities — **Image, Voice, and Text** — and processes them through an integrated NLP workflow.

The system extracts or accepts text from the selected input, performs grammar correction, generates concise summaries, and converts the processed output into speech.

## 🚀 Features

### Three Input Modes

**1. Image Input (OCR)**
- Upload an image containing textual information.
- Apply image preprocessing using OpenCV.
- Extract text using Tesseract OCR and Pytesseract.

**2. Voice Input (Speech-to-Text)**
- Capture voice input through a microphone.
- Convert speech into text using Google Speech Recognition or OpenAI Whisper.
- Process the recognized text through subsequent NLP stages.

**3. Text Input**
- Directly enter or provide textual content.
- Skip the extraction stage and pass the input directly to the NLP processing pipeline.

### NLP Processing Pipeline

All three input modes converge into a common processing workflow:

- **Grammar Correction:** Detect and correct grammatical errors using LanguageTool.
- **Text Summarization:** Generate concise summaries using pretrained Transformer models.
- **Text-to-Speech:** Convert the generated summary into audio using TTS engines.

## 🏗️ System Architecture

```text
                USER INPUT
                    |
          +---------+---------+
          |         |         |
        IMAGE     VOICE      TEXT
          |         |         |
         OCR      Speech    Direct Text
          |      Recognition  Input
          |         |         |
          +---------+---------+
                    |
              Extracted Text
                    |
                    v
           GRAMMAR CORRECTION
                    |
                    v
            TEXT SUMMARIZATION
                    |
                    v
              TEXT-TO-SPEECH
                    |
                    v
             AUDIO OUTPUT
```

## 🛠️ Technology Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Image Processing | OpenCV |
| OCR | Tesseract, Pytesseract |
| Speech-to-Text | Google Speech Recognition, OpenAI Whisper |
| Grammar Correction | LanguageTool |
| Text Summarization | Hugging Face Transformers, BART / PEGASUS |
| Text-to-Speech | Edge TTS, Bark |
| Audio Processing | Pydub, FFmpeg |
| NLP Utilities | NLTK |

## 📂 Project Structure

```text
NLP_project/
│
├── z_nlp_pipeline/
│   ├── 1_OCR_2.py
│   ├── 2_Voice_to_Text_google.py
│   ├── 3_Voice_to_Text_Whisper.py
│   ├── 4_Text_Correction.py
│   ├── 5_Text_Summary_Better.py
│   ├── 6_Text_to_Speech.py
│   └── main.py
│
├── requirements.txt
├── NLP_Project.pdf
├── output.txt
├── summary_audio.mp3
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Udaykaran-Singh/NLP_project.git
cd NLP_project
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install External Dependencies

For macOS:

```bash
brew install tesseract
brew install ffmpeg
```

## ▶️ Running the Project

Execute the main application:

```bash
python z_nlp_pipeline/main.py
```

The application provides a menu-driven interface where users can select one of the three input modes:

1. Image Input
2. Voice Input
3. Text Input

The selected input is passed through the corresponding processing stages.

## 🔍 Implementation Highlights

- Integrated three different input modalities into a unified NLP workflow.
- Implemented image preprocessing to improve OCR extraction.
- Integrated two speech recognition approaches: Google Speech Recognition and Whisper.
- Used sentence-based chunking to handle longer text during summarization.
- Integrated grammar correction, Transformer-based summarization, and speech synthesis.
- Designed the application using modular Python scripts.

## 📊 Performance

The integrated pipeline achieves an approximate end-to-end processing latency of **15–30 seconds**, depending on the input modality, input size, and execution environment.

## 🎯 Applications

- Document text extraction and summarization.
- Voice-based information processing.
- Automated text correction and summarization.
- Accessibility and assistive technology.
- Multimodal information processing.

## 🔮 Future Improvements

- Develop a web-based interface.
- Improve processing speed and model efficiency.
- Extend multilingual support.
- Integrate more advanced OCR and speech recognition models.
- Deploy the pipeline as a REST API.

## 👨‍💻 Author

**Udaykaran Singh**

B.Tech – Data Science, NIT Jalandhar

- GitHub: [Udaykaran-Singh](https://github.com/Udaykaran-Singh)
- LinkedIn: [Udaykaran Singh](https://www.linkedin.com/in/udaykaran-singh-56821833a/)
- Email: udaykaransingh1313@gmail.com

---

⭐ If you find this project interesting, consider giving the repository a star!

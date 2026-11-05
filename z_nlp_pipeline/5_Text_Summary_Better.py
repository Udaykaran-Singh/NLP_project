import nltk
from transformers import pipeline
from nltk.tokenize import sent_tokenize


# Load a DOCUMENT summarization model (not extreme)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text: str, max_chunk_size: int = 900) -> str:
    """
    Fluent abstractive summarization with controlled hallucination.
    Suitable for academic and project use.
    """

    if not text or not text.strip():
        return ""

    sentences = sent_tokenize(text)
    chunks = []
    chunk = ""

    # ---- Chunking (safe for long documents) ----
    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_chunk_size:
            chunk += " " + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence

    if chunk:
        chunks.append(chunk.strip())

    summaries = []

    # ---- Summarize each chunk ----
    for chunk in chunks:
        word_count = len(chunk.split())

        max_len = min(150, max(60, int(word_count * 0.4)))
        min_len = max(40, int(word_count * 0.2))

        summary = summarizer(
            chunk,
            max_length=max_len,
            min_length=min_len,
            do_sample=False,
            truncation=True
        )

        summaries.append(summary[0]["summary_text"])

    return "\n".join(summaries)

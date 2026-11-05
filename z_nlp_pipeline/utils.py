import re

def clean_summary_text(text: str) -> str:
    """
    Light post-processing to clean OCR / summarization artifacts.
    Preserves meaning. No hallucination added.
    """

    if not text or not text.strip():
        return ""

    # Remove unnecessary line breaks
    text = re.sub(r"\n+", " ", text)

    # Fix broken hyphenated words (e.g., dis-cussed -> discussed)
    text = re.sub(r"(\w)-\s*(\w)", r"\1\2", text)

    # Normalize spacing
    text = re.sub(r"\s+", " ", text)

    # Ensure proper spacing after punctuation
    text = re.sub(r"\.\s*", ". ", text)

    return text.strip()

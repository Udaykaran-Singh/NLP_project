import language_tool_python
import re

tool = language_tool_python.LanguageTool("en-US")


def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def correct_text(text):
    """
    Grammar correction using LOCAL LanguageTool (offline).
    No API, no upgrade issues.
    """
    if not text or not text.strip():
        return text

    cleaned = clean_text(text)

    try:
        # LOCAL server (offline)
        matches = tool.check(cleaned)
        corrected = language_tool_python.utils.correct(cleaned, matches)
        return corrected

    except Exception as e:
        print("[WARN] Grammar correction skipped:", e)
        return cleaned

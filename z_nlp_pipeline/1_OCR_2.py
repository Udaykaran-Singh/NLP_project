import cv2
import pytesseract
import os

# OPTIONAL: set tesseract path manually if needed
# pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 2
    )
    return thresh


def run_ocr(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = cv2.imread(image_path)
    processed = preprocess_image(img)

    text = pytesseract.image_to_string(
        processed, config="--oem 3 --psm 3"
    )

    return text

import pytesseract
from PIL import Image
import cv2

# If needed, explicitly set path (uncomment if error)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("data/images/sample.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(
    gray,
    lang="tam+eng"
)

print("\n--- OCR Output ---")
print(text)

with open("data/ocr_raw.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("OCR text saved to data/ocr_raw.txt")

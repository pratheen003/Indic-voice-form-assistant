import easyocr
from ocr.preprocess import preprocess_image
import tempfile
import cv2

def image_to_text(image_path):
    processed = preprocess_image(image_path)

    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    cv2.imwrite(temp_file.name, processed)

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(temp_file.name, detail=0)

    return "\n".join(result)

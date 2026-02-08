import easyocr

def image_to_text(image_path):
    reader = easyocr.Reader(['en'], gpu=False)  # TEMP FIX
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)


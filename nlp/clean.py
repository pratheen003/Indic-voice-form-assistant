import re

def clean_ocr_text(text):
    lines = text.split("\n")
    useful = []

    for line in lines:
        if len(line) > 4 and re.search("[A-Za-z]", line):
            useful.append(line)

    return "\n".join(useful)

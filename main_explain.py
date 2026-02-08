from nlp.text_cleaner import clean_text
from nlp.form_understanding import extract_sections
from nlp.explainer import explain_form

with open("data/ocr_raw.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

lines = clean_text(raw_text)
sections = extract_sections(lines)
explanation = explain_form(sections)

print("\n--- Simple Tamil Explanation ---")
for line in explanation:
    print(line)

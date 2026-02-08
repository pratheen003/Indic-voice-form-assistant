from speech.stt import speech_to_text
from ocr.ocr import image_to_text
from nlp.explain import explain_text
from nlp.clean import clean_ocr_text
from tts.speak import speak_tamil

print("Choose input type:")
print("1. Voice")
print("2. Image")

choice = input("Enter choice (1/2): ")

if choice == "1":
    text = speech_to_text("data/audio/input.mp3")

elif choice == "2":
    text = image_to_text("data/images/input.jpeg")
    text = clean_ocr_text(text)   # 👈 THIS IS THE DAY 7 UPGRADE

else:
    print("Invalid choice")
    exit()

print("\n--- Extracted Text ---")
print(text)

explanation = explain_text(text)

print("\n--- Simple Tamil Explanation ---")
print(explanation)

speak_tamil(explanation)

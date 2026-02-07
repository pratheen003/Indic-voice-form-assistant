import whisper

model = whisper.load_model("base")

result = model.transcribe(
    "data/audio/sample.mp3",
    language="ta"  
)

print("Transcribed Text:")
print(result["text"])

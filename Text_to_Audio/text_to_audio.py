from gtts import gTTS
import os

# 1. The text you want to turn into speech
text_script = """
Welcome to your Python audio file generator! 
This audio was generated using Google Text-to-Speech in Python.
"""

# 2. Convert text to audio (Language: English)
print("🎙️ Generating audio file...")
tts = gTTS(text=text_script, lang='en', slow=False)

output_filename = "output.mp3"
tts.save(output_filename)

print(f"✅ Audio file successfully created and saved as '{output_filename}'!")

os.system(f"start {output_filename}")
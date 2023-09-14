
from gtts import gTTS
import os

text = "I am awesome"

# Initialize gTTS
tts = gTTS(text)

# Save the audio file
tts.save("output.mp3")

# Play the audio file (requires a media player)
os.system("mpg123 output.mp3")

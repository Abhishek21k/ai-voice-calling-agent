
from elevenlabs import play
from elevenlabs.client import ElevenLabs

import os
from dotenv import load_dotenv

load_dotenv(override=True)


client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.generate(
    text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
    voice="Rachel",
    model="eleven_multilingual_v2"
)
play(audio)

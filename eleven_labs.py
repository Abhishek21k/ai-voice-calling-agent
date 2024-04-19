
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

import os
from dotenv import load_dotenv

load_dotenv(override=True)


client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def tts(text: str):
    print("\ntts")
    audio = client.generate(
        text=text,
        voice="Rachel",
        # model="eleven_multilingual_v2"
    )
    play(audio)


# save(audio, "hello.mp3")

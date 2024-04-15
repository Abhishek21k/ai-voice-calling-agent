
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

import os
from dotenv import load_dotenv

load_dotenv(override=True)


client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.generate(
    text='''भेन का लौड़ा''',
    voice="gh4KqQpuToGmra4sU2FJ",
    model="eleven_multilingual_v2"
)


save(audio, "hello.mp3")

import chatgpt
import speech_to_text
import eleven_labs
import asyncio


while True:
    text = asyncio.run(speech_to_text.transcripts())
    output = chatgpt.streaming(text)
    eleven_labs.tts(output)

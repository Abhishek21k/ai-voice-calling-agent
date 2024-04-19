import asyncio
import os

from dotenv import load_dotenv


from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

load_dotenv(override=True)


API_KEY = os.getenv("DG_API_KEY")


async def transcripts():
    transcript_complete = asyncio.Event()
    try:
        text = []
        # STEP 1: Create a Deepgram client using the API key
        config = DeepgramClientOptions(options={"keepalive": "true"})

        deepgram: DeepgramClient = DeepgramClient(API_KEY, config)
        # STEP 2: Create a websocket connection to Deepgram
        dg_connection = deepgram.listen.asynclive.v("1")

        # STEP 3: Define the event handlers for the connection
        async def on_message(self, result, **kwargs):

            sentence = result.channel.alternatives[0].transcript
            if len(sentence) == 0:
                return

            text.append(sentence)
            print(f"speaker: {sentence}")
            transcript_complete.set()

        # STEP 4: Register the event handlers
        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)

        # STEP 5: Configure Deepgram options for live transcription
        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-IN",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            numerals=True,
            endpointing=True,
        )

        # STEP 6: Start the connection
        await dg_connection.start(options)

        print("\nConnected to Deepgram\n")

        # STEP 7: Start recording audio from the microphone
        microphone = Microphone(dg_connection.send)
        microphone.start()

        await transcript_complete.wait()

        # STEP 11: Stop recording audio from the microphone
        microphone.finish()
        # STEP 13: Close the connection to Deepgram
        await dg_connection.finish()

        print("\nFinished")
        print("\nTEXT:\n", text)

    except Exception as e:
        print(f"Could not open socket: {e}")
        return


if __name__ == "__main__":
    asyncio.run(transcripts())

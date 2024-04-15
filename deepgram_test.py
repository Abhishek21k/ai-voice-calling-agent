import asyncio
import os
import httpx
from dotenv import load_dotenv


from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

load_dotenv()

# URL for the realtime streaming audio you would like to transcribe
# URL = "http://stream.live.vc.bbcmedia.co.uk/bbc_world_service"

API_KEY = os.getenv("DG_API_KEY")


async def transcripts():
    try:
        # STEP 1: Create a Deepgram client using the API key

        deepgram: DeepgramClient = DeepgramClient()
        # STEP 2: Create a websocket connection to Deepgram
        dg_connection = deepgram.listen.live.v("1")

        # STEP 3: Define the event handlers for the connection
        def on_message(self, result, **kwargs):
            # print("message received")
            sentence = result.channel.alternatives[0].transcript

            if len(sentence) == 0:
                return

            print(f"speaker: {sentence}")

        def on_error(self, error, **kwargs):
            print(f"\n\n{error}\n\n")

        # STEP 4: Register the event handlers
        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        # STEP 5: Configure Deepgram options for live transcription
        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            numerals=True,
            # To get UtteranceEnd, the following must be set:
            interim_results=True,
            utterance_end_ms="1000",
            vad_events=True,
        )

        # STEP 6: Start the connection
        if dg_connection.start(options) is False:
            print("\n\nFAILED to connect to Deepgram.\n\n")
            return

        print("\nConnected to Deepgram\n")

        print("\n\nPress Enter to stop recording...\n\n")
        # STEP 7: Start recording audio from the microphone
        microphone = Microphone(dg_connection.send)
        microphone.start()
        input("")

        # STEP 11: Stop recording audio from the microphone
        microphone.finish()
        # STEP 13: Close the connection to Deepgram
        dg_connection.finish()

        print("Finished")

    except Exception as e:
        print(f"Could not open socket: {e}")
        return


if __name__ == "__main__":
    asyncio.run(transcripts())

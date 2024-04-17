import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

load_dotenv()

SPEAK_OPTIONS = {
    "text": "Talking to my shadow, he advised me not to worry / Said I should plant my tree and let it rise out of the fury"}
filename = "output.wav"


def main():
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()

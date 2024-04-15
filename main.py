from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from elevenlabs import save
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Initialize OpenAI and Eleven Labs clients
api_key_openai = os.getenv("OPENAI_API_KEY")
api_key_elevenlabs = os.getenv("ELEVENLABS_API_KEY")

llm = ChatOpenAI(api_key=api_key_openai, model="gpt-3.5-turbo")
elevenlabs_client = ElevenLabs(api_key=api_key_elevenlabs)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a mother and you are talking to your son. The Son says, 'I feel like I am not good enough'.'"),
    ("user", "{input}")
])

output_parser = StrOutputParser()

# Define the chain
chain = prompt | llm | output_parser

# Invoke the chain with user input
user_input = "I feel like I am not good enough. Can you please make me feel good enough?"
response = chain.invoke(user_input)

# Generate audio from the ChatGPT response using Eleven Labs
audio = elevenlabs_client.generate(
    text=response, voice="gh4KqQpuToGmra4sU2FJ", model="eleven_multilingual_v2")

# Save the generated audio to a file
save(audio, "response_audio.mp3")

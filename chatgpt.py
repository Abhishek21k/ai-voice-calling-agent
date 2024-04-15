from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a mother and you are talking to your son. The Son says, 'I feel like I am not good enough'.'"),
    ("user", "{input}")
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser


response = chain.invoke(
    "I feel like I am not good enough.can you please make me feel good enough?")

print("response:", response)

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser


response = chain.invoke("What is the langchain?")

print("response:", response)

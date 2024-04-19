from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")


def streaming(input: str):
    print("\n openai\n")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a voice calling agent that responds to the user requests."),
        ("user", "{input}")
    ])
    output_parser = StrOutputParser()

    chain = llm | output_parser

    response = chain.invoke(
        input=input)
    print("response:", response)

    # for chunk in chain.stream("I feel like I am not good enough.can you please make me feel good enough?"):
    #     print(chunk, end="", flush=True)

    return response

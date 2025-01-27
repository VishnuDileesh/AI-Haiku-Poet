from fastapi import FastAPI
from typing import Union

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)

import os 

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")


chatllm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.9, model="gpt-3.5-turbo")

human_template = ("Write me a haiku about {theme}")

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

system_template = ("You are an expert haiku poet who is in love with nature")

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

app = FastAPI()

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/haiku")
def read_haiku(theme: Union[str, None] = None):
    haiku = chatllm.invoke(chat_prompt.format_prompt(theme=theme).to_messages())
    return {"Haiku": haiku.content}

@app.get("/health")
def read_health():
    return {"Health": "Ok"}

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI


load_dotenv()

model = ChatMistralAI(model='mistral-small')

def call_llm(query):

    reponse = model.invoke(query)

    return reponse.content

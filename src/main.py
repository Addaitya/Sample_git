import os
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
print(f"API key: {os.getenv('GOOGLE_API_KEY')}")
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
print(llm.invoke("Write me a ballad about LangChain"))


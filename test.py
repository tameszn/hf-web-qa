from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

response=llm.invoke("How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia.")

print(response.content)
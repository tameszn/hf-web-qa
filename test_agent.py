from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain.agents import create_agent







RULES="""
Return the final answer with very little/NO explanations or  NO additional sentences 
Write numbers using digits only,without commas and units unless requested
do not include the 'final answer:' prefix or trailing period 
If genuinely unable to answer any question,return 'unknown'
"""

load_dotenv()
tools=[TavilySearch(max_results=3)]

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)
question='What is the first name of the only Malko Competition recipient from the 20th Century (after 1977) whose nationality on record is a country that no longer exists?'


def get_text(content):
    if isinstance(content, str):
        return content
    return "".join(p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") == "text")




agent=create_agent(model=llm, tools=tools,system_prompt=RULES)


result = agent.invoke({"messages": [("user", question)]})
print(get_text(result["messages"][-1].content))
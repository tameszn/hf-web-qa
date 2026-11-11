from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv



RULES="""
Return the final answer with very little/NO explanations or  NO additional sentences 
Write numbers using digits only,without commas and units unless requested
do not include the 'final answer:' prefix or trailing period 
If genuinely unable to answer any question,return 'unknown'
"""

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)
question=' I\'m making a grocery list for my mom, but she\'s a professor of botany and she\'s a real stickler when it comes to categorizing things. I need to add different foods to different categories on the grocery list, but if I make a mistake, she won\'t buy anything inserted in the wrong category. Here\'s the list I have so far: milk, eggs, flour, whole bean coffee, Oreos, sweet potatoes, fresh basil, plums, green beans, rice, corn, bell pepper, whole allspice, acorns, broccoli, celery, zucchini, lettuce, peanuts'
response = llm.invoke([("system", RULES), ("user", question)])

def get_text(content):
    if isinstance(content, str):
        return content
    return "".join(p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") == "text")

print(get_text(response.content))
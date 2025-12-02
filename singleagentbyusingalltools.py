import os
import requests
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType


# ---------- ENV & LLM SETUP ----------
load_dotenv()

# Ensure you have GOOGLE_API_KEY in your .env
# GOOGLE_API_KEY="your_gemini_api_key"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",       # or "gemini-2.5-flash", etc.
    temperature=0,
    google_api_key=GEMINI_API_KEY,
)


# ---------- TOOLS ----------
def greet(name: str):
    return f"Hello {name}, I am your LangChain Agent powered by Gemini!"


def weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    res = requests.get(url).json()
    temp = res["current_condition"][0]["temp_C"]
    return f"Current temperature in {city} is {temp}°C"


greet_tool = Tool(
    name="greeting_tool",
    func=greet,
    description="Use this to greet a person by name."
)

weather_tool = Tool(
    name="weather",
    func=weather,
    description="Get current temperature of a city."
)

tools = [greet_tool, weather_tool]


# ---------- MEMORY ----------
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


# ---------- AGENT CREATION ----------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors="Sorry, I couldn't understand that, but here's my response:"
)



# ---------- MAIN LOOP ----------
def main():
    print("LangChain Gemini Agent is ready!")
    print("Type 'exit' to quit.")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        response = agent.run(query)
        print("Agent:", response)


if _name_ == "_main_":
    main()
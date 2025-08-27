from collections.abc import AsyncGenerator
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server 
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

server = Server()


model = ChatOpenAI(
    model="gpt-4o", 
    temperature=0.7,
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY
)


poem_writer = create_react_agent(
    model=model,  
    tools=[],
    prompt="You are a poem writer, create a poem about friendship."
)

@server.agent() 
async def poem_writer_agent(messages: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    query = " ".join(part.content for m in messages for part in m.parts)

    response = await poem_writer.ainvoke({
        "messages": [ 
            {
                "role": "user",
                "content": query
            }
        ]
    })

    yield Message(parts=[MessagePart(content=response["messages"][-1].content)])

server.run(port=8002)
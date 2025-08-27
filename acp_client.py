from acp_sdk.client import Client
import asyncio
from colorama import Fore 

async def main():
    # Create clients for the comedian and poem writer agents
    async with Client(base_url="http://localhost:8001") as comedian_client, Client(base_url="http://localhost:8002") as poem_writer_client:

        # Send a message to the comedian agent
        comedian_result = await comedian_client.run_sync(agent='comedian_agent', input="Hello, how are you?")
        print(Fore.BLUE+ comedian_result.output[0].parts[0].content)

        # Send the comedian's response to the poem writer agent
        poem_writer_result = await poem_writer_client.run_sync(agent='poem_writer_agent', input=comedian_result.output[0].parts[0].content)
        print(Fore.YELLOW + poem_writer_result.output[0].parts[0].content)
        print(Fore.WHITE)


asyncio.run(main())


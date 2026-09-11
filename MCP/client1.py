import asyncio
from fastmcp import Client


async def main():

    client = Client("1_simple_mcp.py")

    async with client:

        tools = await client.list_tools()

        print("Available Tools: ")
        print(tools)

        result = await client.call_tool(
            "add_numbers",
            {
                "a": 1,
                "b": 5
            }
        )
        print()
        print(f"Final Result: {result.content[0].text}")



if __name__ == "__main__":
    asyncio.run(main())
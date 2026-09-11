import asyncio
from fastmcp import Client


async def main():

    client = Client("1_simple_mcp.py")

    async with client:

        # tool discovery
        tools = await client.list_tools()

        print(f"Available Tools: ")
        print(tools[0].name)

        result = await client.call_tool(
            "add_numbers",
            {
                "a": 40,
                "b": 89
            }
        )

        print()
        print("Result: ")
        print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
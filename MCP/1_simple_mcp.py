# from fastmcp import FastMCP

# mcp = FastMCP("Calculator")


# @mcp.tool()
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers."""
#     return a + b


# if __name__ == "__main__":
#     mcp.run()



from fastmcp import FastMCP


mcp = FastMCP("sample server")



@mcp.tool
def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run()
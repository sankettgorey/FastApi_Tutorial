# Level 1 — Basic async / await

# 1. Write an async function called hello() that:

# Prints "Hello"
# Waits for 2 seconds asynchronously
# Prints "World"


import asyncio

async def hello():

    print("hello")

    await asyncio.sleep(2)

    print('world')

asyncio.run(hello())
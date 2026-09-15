# 10. Consider this requirement:

# You first need to fetch a user's ID. Only after getting the ID can you fetch that user's orders.

# Write the async code.

import asyncio
import time

async def fetch_id():

    print('fetching id')

    await asyncio.sleep(2)

    return "id"




async def fetch_order(id: str):

    print('fetching order')

    await asyncio.sleep(2)
    order = f"order_{id}"

    return order


async def main():



    id = await fetch_id()

    order = await fetch_order(id)

    print(order)

asyncio.run(main())
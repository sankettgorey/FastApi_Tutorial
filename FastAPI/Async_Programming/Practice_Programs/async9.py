# 9. Consider this requirement:

# You need to fetch a user's profile, orders, and notifications. None of these operations depends on the others.

# Write the async code you would use to perform these operations efficiently.


import asyncio
import time

async def fetch_profile():

    await asyncio.sleep(3)

    print('task 1 completed')

    return "user_profile"


async def orders():

    await asyncio.sleep(2)

    print('task 2 completed')


    return "orders"


async def notification():

    await asyncio.sleep(4)

    print('task 3 completed')


    return "notification"



async def main():

    t1 = asyncio.create_task(fetch_profile())
    t2 = asyncio.create_task(orders())
    t3 = asyncio.create_task(notification())

    await t1
    await t2
    await t3


asyncio.run(main())
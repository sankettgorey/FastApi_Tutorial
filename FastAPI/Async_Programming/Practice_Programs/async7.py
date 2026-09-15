# 7. Create three async functions:

# get_user()          → waits 2 seconds → returns "User data"
# get_orders()        → waits 3 seconds → returns "Order data"
# get_notifications() → waits 1 second → returns "Notification data"

# Use asyncio.gather() to run all three concurrently and collect their results.


import asyncio
import time


async def get_user():

    await asyncio.sleep(2)

    return "user_data"



async def get_orders():

    await asyncio.sleep(3)

    return "order_data"


async def get_notifications():

    await asyncio.sleep(1)

    return "notification_data"


async def main():

    results = await asyncio.gather(
        get_user(),
        get_orders(),
        get_notifications()
    )

    return results
    # print(results)

results = asyncio.run(main())
print(results)
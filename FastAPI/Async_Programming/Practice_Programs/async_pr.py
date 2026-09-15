import asyncio
import time


async def get_user():

    await asyncio.sleep(2)

    return 'user_data'


async def get_orders():

    await asyncio.sleep(3)

    return 'get_orders'


async def get_notifications():

    await asyncio.sleep(1)

    return 'notifications_data'


async def main():


    user, order, notification = await asyncio.gather(
        get_user(),
        get_orders(),
        get_notifications()
    )

    return user, order, notification


x = asyncio.run(main())
print(x)
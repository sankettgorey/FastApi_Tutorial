import asyncio
import time

async def task1():

    print('task1 started')

    await asyncio.sleep(3)

    print('task1 completed')



async def task2():

    print('task2 started')

    await asyncio.sleep(3)

    print('task 2 completed')


async def main():

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    await t1
    await t2


asyncio.run(main())
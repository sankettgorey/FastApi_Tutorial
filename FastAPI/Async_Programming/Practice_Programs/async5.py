# 5. Write a program that creates three tasks:

# task1 → waits 3 seconds
# task2 → waits 2 seconds
# task3 → waits 1 second

# Schedule all three tasks before waiting for any of them.

import asyncio
import time

async def task1():

    await asyncio.sleep(3)

    print('task 1 finished')


async def task2():

    await asyncio.sleep(2)

    print('task 2 finished')


async def task3():

    await asyncio.sleep(1)

    print('task 3 finished')



async def main():

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())

    await t1
    await t2
    await t3


asyncio.run(main())
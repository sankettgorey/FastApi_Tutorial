# write below using gather
# 5. Write a program that creates three tasks:

# task1 → waits 3 seconds
# task2 → waits 2 seconds
# task3 → waits 1 second

# Schedule all three tasks before waiting for any of them.


import asyncio
import time

async def task1():

    await asyncio.sleep(3)

    print('task1 completed')


async def task2():

    await asyncio.sleep(2)

    print('task2 completed')


async def task3():

    await asyncio.sleep(1)

    print('task3 completed')


async def main():

    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )


asyncio.run(main())
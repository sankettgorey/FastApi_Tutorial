# use of as_completed
'''
as_completed allows us to return results of completed task in a loop
'''

import asyncio
import time


async def task1():

    await asyncio.sleep(3)

    return 'task1 completed'


async def task2():

    await asyncio.sleep(1)

    return 'task2 completed'


async def task3():

    await asyncio.sleep(2)

    return 'task3 completed'


async def main():

    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2()),
        asyncio.create_task(task3())
    ]

    for task in asyncio.as_completed(tasks):

        result = await task
        # print(result)
        return result


result = asyncio.run(main())
print(result)
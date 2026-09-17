import asyncio
import time


async def task1():

    await asyncio.sleep(1)

    return 'task 1 completed'



async def task2():

    await asyncio.sleep(2)

    raise ValueError("task2 failed")


async def task3():

    await asyncio.sleep(3)

    return 'task3 completed'


async def main():

    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2()),
        asyncio.create_task(task3())

    ]

    for task in asyncio.as_completed(tasks):
        try:
            results = await task
            print(results)

        except Exception as e:
            print(e)


asyncio.run(main())
import asyncio

async def task1():

    await asyncio.sleep(3)

    return 'task1 completed'


async def task2():

    await asyncio.sleep(1)

    return 'task2 completed'



async def main():

    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2())
    ]

    for task in asyncio.as_completed(tasks):

        result = await task

        print(result)

asyncio.run(main())
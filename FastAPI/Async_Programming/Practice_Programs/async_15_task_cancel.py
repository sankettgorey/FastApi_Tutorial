import asyncio
import time

async def task1():

    print('task started')

    await asyncio.sleep(3)

    print('task compelted')



async def main():

    task = asyncio.create_task(task1())

    await asyncio.sleep(2)

    task.cancel()

    print('task cancelled')


asyncio.run(main())
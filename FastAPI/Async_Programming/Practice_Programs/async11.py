import time
import asyncio


async def task1():

    print('task 1 started')

    time.sleep(3)

    print('task 1 completed')


async def task2():

    print('task 2 started')


    await asyncio.sleep(3)

    print('task 2 completed')


async def main():

    await asyncio.gather(task1(), task2())


start = time.time()

asyncio.run(main=main())

print(f'total time taken: {time.time() - start}')



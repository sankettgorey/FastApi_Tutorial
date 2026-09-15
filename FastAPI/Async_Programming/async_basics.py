import asyncio
import time

async def task1():

    print('task 1 started')

    await asyncio.sleep(3)

    print('task 1 completed')



async def task2():

    print('task 2 started')

    await asyncio.sleep(3)

    print('task 2 completed')


async def main():

    t1 = asyncio.create_task(task1())   # creating corutines to run using event loop
    t2 = asyncio.create_task(task2())   # creating corutines to run using event loop

    await t1    # asking main to wait till t1 completes
    await t2    # asking main to wait until t1 completes

start = time.time()

asyncio.run(main())     # running final main coroutine using event loop

print(f'total time taken is: {time.time() - start}')
# 3. Write a program where:

# task1() waits 3 seconds.
# task2() waits 1 second.
# Both tasks should be scheduled using asyncio.create_task().
# main() should wait for both tasks to complete.


import asyncio
import time

async def task1():

    await asyncio.sleep(3)

    print('task1 completed')


async def task2():

    await asyncio.sleep(1)

    print('task2 completed')


async def main():

    t1 = asyncio.create_task(task1())

    t2 = asyncio.create_task(task2())

    await t1
    await t2

start = time.time()
asyncio.run(main())

print(f'tasks completed in {time.time() - start}')
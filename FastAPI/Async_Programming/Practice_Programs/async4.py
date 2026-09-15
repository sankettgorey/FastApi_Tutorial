# 4. Write the same program as Question 3, but don't use asyncio.create_task().

# Make both functions run using only await.

# Observe how the execution differs.


import asyncio
import time

async def task1():

    await asyncio.sleep(3)

    print('task1 completed')


async def task2():

    await asyncio.sleep(1)

    print('task2 completed')


async def main():


    await task1()
    await task2()

start = time.time()
asyncio.run(main())

print(f'tasks completed in {time.time() - start}')
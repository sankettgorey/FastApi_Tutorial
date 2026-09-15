# 2. Create two async functions:

# task1() waits for 2 seconds and prints "Task 1 done"
# task2() waits for 3 seconds and prints "Task 2 done"

# Run both from an async main() function.

import asyncio

async def task1():

    await asyncio.sleep(2)

    print('task1 done')

async def task2():

    await asyncio.sleep(2)

    print('task2 done')


async def main():

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    await t1
    await t2

asyncio.run(main())
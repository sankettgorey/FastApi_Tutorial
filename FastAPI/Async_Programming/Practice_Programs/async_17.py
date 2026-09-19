# Task A starts first and takes 5 seconds.
# Task B takes 3 seconds.
# After 1 second, the main() function calls cancel() on Task A.
# Task A is currently waiting at an await.

import asyncio
import time


async def task1():

    try:
        print('task1 started')
        await asyncio.sleep(5)

    # except asyncio.CancelledError:
    except BaseException:
        print('cancellation error in task1')
        raise


async def task2():

    try:
        print('task2 started')
        await asyncio.sleep(3)

        print('task2 completed')

    except BaseException as e:
        print('cancellation error in task2')
        raise


async def main():

    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())

    await asyncio.sleep(1)

    task_1.cancel()
    try:
        await task_1

    except asyncio.CancelledError:
        print('error')

    await task_2

asyncio.run(main())
import asyncio
import time

async def task1():

    try:
        print('task1 started')

        await asyncio.sleep(5)

    except BaseException as e:
        # print('exception in task 1')
        print('cancellation error in task 1')
        raise


async def task2():

    try:
        print('task2 started')

        await asyncio.sleep(4)

        print('task2 finished')

    except BaseException as e:
        print('cancellation error in task 2')
        raise


async def main():

    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())

    await asyncio.sleep(1)
    task_1.cancel()

    # try:
    #     await task_1
    # except BaseException as e:
    #     # print(str(e))
    #     print('error')

    await task_2


asyncio.run(main())
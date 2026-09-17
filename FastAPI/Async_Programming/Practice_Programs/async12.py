import asyncio
import time

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

    return 'task1'

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

    return 'task2'

async def main():
    t1, t2 = await asyncio.gather(task1(), task2())

    return t1, t2

t2 = asyncio.run(main())

print(t2)
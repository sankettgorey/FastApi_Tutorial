import asyncio

async def task1():
    try:
        print("Task started")
        await asyncio.sleep(5)
        print("Task completed")
    except asyncio.CancelledError:
        print("Cleaning up...")
        raise

async def main():
    task = asyncio.create_task(task1())

    await asyncio.sleep(1)

    task.cancel()
    # await task
    try:
        await task
    except asyncio.CancelledError:
        print("Main knows task was cancelled")

asyncio.run(main())
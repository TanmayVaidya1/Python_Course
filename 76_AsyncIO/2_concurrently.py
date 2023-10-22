import asyncio

async def my_async_function1():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World! 1"

async def my_async_function2():
    # asynchronous code here
    await asyncio.sleep(2)
    return "Hello, Async World! 2"

async def my_async_function3():
    # asynchronous code here
    await asyncio.sleep(5)
    return "Hello, Async World! 5"

async def main():
    L = await asyncio.gather(
        my_async_function1(),
        my_async_function2(),
        my_async_function3(),
    )
    print(L)

asyncio.run(main())

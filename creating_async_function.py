import asyncio

async def test1():
    print("this is the first task")
    asyncio.create_task(test2())
    await asyncio.sleep(3)
    print("first task completed")
    
async def test2():
    print("this is the second task")
    asyncio.create_task(test3())
    await asyncio.sleep(2)
    print("second task completed")
    
async def test3():
    print("this is the final task")
    await asyncio.sleep(1)
    print("final task completed")
    
asyncio.run(test1())
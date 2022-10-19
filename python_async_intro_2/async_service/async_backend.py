import asyncio

async def calculate_square(num):
    await asyncio.sleep(1)
    return num ** 2

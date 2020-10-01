import asyncio

async def main():
    print("Await for 5 seconds")
    for i in range(6):
        await asyncio.sleep(1)
        print(".")
    print('Finish awaiting.')

asyncio.run(main())

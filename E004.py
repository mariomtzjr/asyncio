import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Iniciado a las {time.strftime('%X')}")

    await say_after(1, 'Hola')
    await say_after(2, 'Mundo')

    print(f"Finalizado a las {time.strftime('%X')}")

asyncio.run(main())

import asyncio
import time

"""
Función create_task()
Ejecuta subrutinas de manera concurrente como Tareas asyncio
"""
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'Hola'))

    task2 = asyncio.create_task(
        say_after(2, 'Mundo'))

    print(f"Iniciado a las {time.strftime('%X')}")

    # Await until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"Finalizado a las {time.strftime('%X')}")

asyncio.run(main())

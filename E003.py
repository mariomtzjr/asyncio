import asyncio

"""
mensaje: Función que esperará un tiempo determinado, para
luego mostrar el texto.
"""

async def mensaje(texto, s):
    await asyncio.sleep(s)
    print(texto)

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)

# Primera tarea
loop.create_task(mensaje("Este es el mensaje #1", 2))

# Segunda tarea
loop.create_task(mensaje("Este es el mensaje #2", 1))

loop.run_forever()
loop.close()

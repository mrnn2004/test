import websockets
import asyncio

async def listen():
    async with websockets.connect("ws://127.0.0.1:3000") as ws:
        await ws.send("Hello Server!")
        
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())

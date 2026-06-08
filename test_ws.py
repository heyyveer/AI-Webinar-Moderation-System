import asyncio
import websockets

async def test():

    async with websockets.connect(
        "ws://127.0.0.1:8000/ws"
    ) as ws:

        await ws.send(
            "audio not working"
        )

        response = await ws.recv()

        print(response)

asyncio.run(test())
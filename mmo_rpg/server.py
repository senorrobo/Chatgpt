import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main(host="localhost", port=8765):
    async with websockets.serve(handler, host, port):
        print(f"Server running on {host}:{port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

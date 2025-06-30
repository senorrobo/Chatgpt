import asyncio
import json
import websockets

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            # broadcast to all connected clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(json.dumps(data))
    finally:
        connected.remove(websocket)

def main(host='localhost', port=8765):
    start_server = websockets.serve(handler, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    print(f"Server running on {host}:{port}")
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()

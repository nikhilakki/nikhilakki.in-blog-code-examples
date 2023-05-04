import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        number = int(input("How many itterations? "))
        for i in range(number):
            await websocket.send(str(i))
            print(f">>> Sending {i}")

            activity = await websocket.recv()
            print(f"<<< Received {activity}")

if __name__ == "__main__":
    asyncio.run(hello())
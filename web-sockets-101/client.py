import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        question = input("What do you want to do today?\n")

        await websocket.send(question)
        print(f">>> {question}")

        activity = await websocket.recv()
        print(f"<<< {activity}")

if __name__ == "__main__":
    asyncio.run(hello())
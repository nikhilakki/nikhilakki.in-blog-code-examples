import asyncio
import websockets

async def hello(websocket):
    answer = await websocket.recv()
    print(f"<<< {answer}")

    activity = f"I'm thinking... {answer}!"

    await websocket.send(activity)
    print(f">>> {activity}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
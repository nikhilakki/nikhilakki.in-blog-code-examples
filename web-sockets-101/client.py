import asyncio
import websockets

async def send_messages():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Type a message to send to the server: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(send_messages())

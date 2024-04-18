import websockets
from decouple import config


async def test_send_message(message):
    try:
        uri = "ws://localhost:8888/ws/connect/"
        async with websockets.connect(uri) as websocket:
            response1 = await websocket.recv()
            await websocket.send(config("BOT_TOKEN"))

            response2 = await websocket.recv()
            print(f"response1: {response1}\nresponse2: {response2}")
            if str(response2) == "Token accepted":
                await websocket.send(message)
            else:
                print("Server error")
        print("Accepted")
        return str("Accepted")
    except Exception as e:
        print(f"Error: {e}")
        return str(f"Error: {e}")
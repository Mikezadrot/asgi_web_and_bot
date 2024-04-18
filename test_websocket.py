import asyncio
import websockets
from decouple import config


async def speaker_input(websocket):
    data = input("Your input>>")
    try:

        await websocket.send(data)
        return await speaker_output(websocket)
    except Exception as e:
        print(f"Have a problem: {e}")
        if str(e) == "no close frame received or sent":
            return await reconnect(data)


async def speaker_output(websocket):
    try:
        response = await websocket.recv()
        print(f'Output<< {response}')
        if response != "Dont accept":
            return await speaker_input(websocket)

        else:
            speak1 = input("You want continue connecting?\n Enter yes for connect or no for stop program ")

            if speak1 == "yes":
                return await hello()
    except Exception as e:
        print(f"Output Have a problem: {e}")


async def hello():
    try:
        uri = "ws://localhost:8888/ws/connect/"
        async with websockets.connect(uri) as websocket:
            await speaker_output(websocket)
    except Exception as e:
        print(f"Have a problem: {e}")


async def reconnect(data):
    try:
        uri = "ws://localhost:8888/ws/connect/"
        async with websockets.connect(uri) as websocket:
            await websocket.send(config("BOT_TOKEN"))
            await websocket.send(data)
            print("Reconnect, press Enter")
            return await speaker_output(websocket)


    except Exception as e:
        print(f"Have a problem: {e}")

# asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()


async def test_send_message():
    try:
        uri = "ws://localhost:8888/ws/connect/"
        async with websockets.connect(uri) as websocket:
            response1 = await websocket.recv()
            await websocket.send(config("BOT_TOKEN"))

            response2 = await websocket.recv()
            print(f"response1: {response1}\nresponse2: {response2}")
            if str(response2) == "Token accepted":
                await websocket.send("Bot")
            else:
                print("Server error")
        print("Accepted")
        return str("Accepted")
    except Exception as e:
        print(f"Error: {e}")
        return str("Denied")

loop = asyncio.get_event_loop()
loop.run_until_complete(test_send_message())
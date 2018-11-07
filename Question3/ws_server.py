from asyncio import get_event_loop, Queue

from websockets import serve

# This is a web socket broker
# It has two ports: one for consumers (5001)
# and one for producers (5000)
#
# Producer is a Django application, which generates two types of events, namely, "SENSOR ADDED" and "MEASUREMENT ADDED"
# Consumer is a React applications which receives these events

MESSAGE_QUEUE = Queue()


async def consume(message):
    print(message)
    await MESSAGE_QUEUE.put(message)


async def producer_handler(websocket, path):
    while True:
        message = await websocket.recv()
        await consume(message)


async def producer():
    return await MESSAGE_QUEUE.get()


async def consumer_handler(websocket, path):
    keep_running = True
    while keep_running:
        message = await producer()
        try:
            await websocket.send(message)
        except:
            keep_running = False
            await consume(message)


if __name__ == "__main__":
    start_producer = serve(producer_handler, 'localhost', 5000)
    start_consumer = serve(consumer_handler, 'localhost', 5001)
    get_event_loop().run_until_complete(start_consumer)
    get_event_loop().run_until_complete(start_producer)
    get_event_loop().run_forever()

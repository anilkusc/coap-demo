import asyncio
from aiocoap import Context, Message, Code
async def coap_client():
    server_endpoint = "coap://127.0.0.1:5683/humidity"
    request = Message(code=Code.GET, uri=server_endpoint,payload=bytes("measured: 76".encode()))
    context = await Context.create_client_context()
    response = await context.request(request).response
    print("########################################################")
    print("\nResponse Code:", response.code)
    print("Received from:", str(response.remote.hostinfo))
    print("Response Payload:", response.payload.decode('utf-8'))
    print("Options:", response.opt)
    print("MID (Message ID):", response.mid)
    print("Token:", response.token)
    print("########################################################")
# Start Event loop
loop = asyncio.get_event_loop()
# Run async function
loop.run_until_complete(coap_client())
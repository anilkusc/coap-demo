import asyncio
from aiocoap import Context, Message, resource
class MyResource(resource.Resource):
    async def render_get(self, request):
        print("########################################################")
        print("Request received...")
        
        # Print various attributes of the CoAP request
        print("Payload: " + str(request.payload))
        print("Remote Host: " + str(request.remote.hostinfo))
        print("Code: " + str(request.code))
        print("Options: " + str(request.opt))
        print("MID (Message ID): " + str(request.mid))
        print("Token: " + str(request.token))
        print("Options: " + str(request.opt))
        print("########################################################")
        payload = b"Data Received!"
        return Message(payload=payload)
async def main():
    site = resource.Site()
    site.add_resource(['humidity'], MyResource())
    context = await Context.create_server_context(site, bind=("127.0.0.1", 5683))
    print(f"CoAP server started...")
    await asyncio.Event().wait()
asyncio.run(main())
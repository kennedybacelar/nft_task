from aiohttp import web


async def process_transfer(request):
    transfer_payload = await request.json()

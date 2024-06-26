from aiohttp import web

from app.main.controller.transactions import process_transfer_controller


async def process_transfer_handler(request):
    transfer_payload = await request.json()
    response = await process_transfer_controller(transfer_payload)
    return web.json_response(response)

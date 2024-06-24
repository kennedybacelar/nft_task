from aiohttp import web

from app.main.controller.transactions import process_transfer_controller


async def process_transfer_handler(request):
    transfer_payload = await request.json()
    await process_transfer_controller()

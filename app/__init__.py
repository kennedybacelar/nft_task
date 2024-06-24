from aiohttp import web

from app.main.router.transactions import process_transfer_handler


def create_app():
    app = web.Application()
    app.router.add_post("/asset/transfer", process_transfer_handler)
    return app

from aiohttp import web

from app.main.router.transactions import process_transfer

def create_app():
    app = web.Application()
    app.router.add_post("/asset/transfer", process_transfer)
    return app
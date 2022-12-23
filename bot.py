from pyrogram import Client
import os
from aiohttp import web
from plugins import web_server
app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, 8000).start()
        
from config import Config


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=Config.TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()

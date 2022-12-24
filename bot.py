from pyrogram import Client
import os
from aiohttp import web
from plugins import web_server
app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, 8000).start()
        class Bot(Client):

    def init(self):

        super().init(

        "renamer",

        api_id=API_ID,

        api_hash=API_HASH,

        bot_token=BOT_TOKEN,

        plugins=dict(root="plugins"),

        workers=50,

        sleep_threshold=10

        )

    async def start(self):

        await super().start()

        #web-response

        app = web.AppRunner(await web_server())

        await app.setup()

        bind_address = "0.0.0.0"

        await web.TCPSite(app, bind_address, 8000).start()

        print('Bot started')

    async def stop(self, *args):

        await super().stop()
        
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

import discord

from asyncio import sleep
from datetime import datetime
from glob import glob
from pathlib import Path

from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

from ..db import db

PREFIX = ">"
OWNER_IDS = [514069435913469962]
COGS = [p.stem for p in Path(".").glob("./lib/cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()

        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

    def run(self, version):
        self.VERSION = version

        print("starting setup...")

        print("setup complete")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("starting bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print(" bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Блять даун пиши правильно команду или иди нахуй осёл")

        await self.stdout.send("<@514069435913469962> Произошла ебейшая хуйня")
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            # pass
            await ctx.send("Такой команды нет долбоёб")

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(794586989122945053)
            self.stdout = self.get_channel(797869639840825374)
            self.scheduler.start()
            
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(f">хелп (version {self.VERSION})"))

            # embed = Embed(title="[В СЕТИ]", colour=0x00FF00,
            #               timestamp=datetime.utcnow())
            # fields = [("Бот TurboTemuch успешно запущен!", "Bot created and coded by TurboTemuch#7375", True)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline)
            #     embed.set_author(name="TurboTemuch Bot", icon_url=self.guild.icon_url)
            #     embed.set_footer(text="Запущен в работу")
            #     embed.set_thumbnail(url=self.guild.icon_url)
            # await channel.send(embed=embed)
            
            # await channel.send(file=File("./data/images/APNG-cube.png"))

            while not self.cogs_ready.all_ready():
                await sleep(0.5)
            
            await self.stdout.send("Бот активен!")
            self.ready = True
            print(" bot ready")
        
        else:
            print("bot reconnected")    

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


bot = Bot()

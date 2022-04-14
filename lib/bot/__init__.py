import discord
import sqlite3

from asyncio import sleep
from datetime import datetime
from glob import glob
from pathlib import Path
from random import choice

from discord import Intents, Forbidden
from discord.errors import Forbidden
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import (CommandNotFound, MemberNotFound, BadArgument, CheckFailure, MissingRequiredArgument, CommandOnCooldown, ExtensionFailed, ExtensionNotFound, DisabledCommand)

from ..db import db

PREFIX = ";"
OWNER_IDS = [514069435913469962]
COGS = [p.stem for p in Path(".").glob("./lib/cogs/*.py")]
IGNORE_EXCEPTIONS = (ExtensionFailed, ExtensionNotFound)


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
        
    def update_db(self, sqlite3):
        guildneeded = self.get_guild(739553608806301736)

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        for member in guildneeded.members:
            if not member.bot:
                cur.execute("INSERT INTO exp")

        to_remove = []
        stored_members = db.column("SELECT UserID FROM exp")
        for id_ in stored_members:
            if not self.guild.get_member(id_):
                to_remove.append(id_)

        for id_ in to_remove: 
            db.multiexec("DELETE FROM exp WHERE UserID = ?", id_)

        db.commit()
        
        print("db updated")
    
    async def on_connect(self):
        print(" bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send(':tools: Произошла ошибка при выполнении команды.')

#        await self.stdout.send("<@514069435913469962> Произошла ошибка при выполнении команды.")
        raise

    async def on_command_error(self, ctx, exc):
        if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):
            pass
        
        elif isinstance(exc, Forbidden):
            # pass
            await ctx.send(':x: 403 Forbidden: Недостаточно прав для выполнения действия.')
        
        elif isinstance(exc, CommandNotFound):
            # pass
            await ctx.send(f":x: Неизвестная команда. Введите `{PREFIX}help` для просмотра списка команд.")
       
        elif isinstance(exc, MissingRequiredArgument):
            # pass
            await ctx.send(':exclamation: Отсутствует один или более необходимых аргументов.')
            
        elif isinstance(exc, CheckFailure):
            await ctx.send(':no_entry: Недостаточно прав для выполнения этой команды.')
            
        elif isinstance(exc, MemberNotFound):
            await ctx.send(':x: Пользователь не найден.')
            
        elif isinstance(exc, BadArgument):
            await ctx.send(':x: Введён некорректный аргумент.')
            
        elif isinstance(exc, CommandOnCooldown):
            await ctx.send(f":clock1: Вы достигли кулдауна команды! Вы сможете использовать её вновь через {exc.retry_after:,.0f} секунд.")
        
        elif isinstance(exc, DisabledCommand):
            await ctx.send(":no_entry: Эта команда была отключена.")
            
#         elif isinstance(exc, ExtensionFailed):
#             print(f"Failed to load lib.cogs.{cog} cog.")

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(794586989122945053)
            self.stdout = self.get_channel(797869639840825374)
#             self.scheduler.add_job(self.check_members, CronTrigger(second="0, 20, 40"))
            self.scheduler.start()
            
            self.update_db()
            
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{PREFIX}хелп (version {self.VERSION})"))

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

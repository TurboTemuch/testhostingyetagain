import discord

from os import name
from random import choice
from typing import Optional
from datetime import datetime

from discord import Intents
from discord import Member
from discord import Embed, File
from discord.ext.commands import Cog
from discord.ext.commands import command

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="Связь", aliases=["Бот", "связь", "бот"])
    async def some_amazing_command(self, ctx):
        await ctx.send(f"{choice((':white_check_mark:', 'Всё работает!', ':eyes:', '5 минут, полёт нормальный!', 'Я жив!', 'На месте!', 'Спасибо <@514069435913469962>, что я работаю!'))}")

    @command(name="slap", aliases=["hit","ударить"])
    async def slap_member(self, ctx, member:Member, *, reason: Optional[str] = "no reason"):
        await ctx.send(f"{ctx.author.name} ударил {member.mention} по причине: {reason}!")
      
    @command(name="хелп", aliases=["помощь","Помощь"])
    async def help(self, channel):
        embed = Embed(title="Команды:", colour=0x00FF00,
                          timestamp=datetime.utcnow())
        fields = [("Префикс: `>`","Модуль fun: \nСвязь (Бот, связь, бот) - проверка связи с ботом \nslap (hit, ударить) `>slap @участник причина` \nхелп (Помощь, помощь) - список команд \ninfo (инфо) - информация о боте", True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await channel.send(embed=embed)

    @command(name="info", aliases=["инфо"])
    async def info(self, channel):
        embed = Embed(title="[В СЕТИ]", colour=0x00FF00,
                          timestamp=datetime.utcnow())
        fields = [("Бот TurboTemuch успешно запущен!", "Bot created and coded by TurboTemuch#7375", True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="Bot TurboTemuch1")
            embed.set_footer(text="Branch deployed & dyno connected")
        await channel.send(embed=embed)
        
    @command(name="update")
    async def update(self, ctx):
        if ctx.message.author.id ==514069435913469962:
            await ctx.bot.change_presence(status=discord.Status.idle, activity=discord.Game("ОБНОВЛЕНИЕ"))
        else:
            await ctx.send("```- У вас нет доступа к этой команде -```")
                
    @command(name="stable")
    async def stable(self, ctx):
        if ctx.message.author.id ==514069435913469962:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(f">хелп (version {ctx.bot.VERSION})"))
        else:
            await ctx.send("```- У вас нет доступа к этой команде -```")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)

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
        fields = [("Префикс: `>`","Модуль fun:", "Связь (Бот, связь, бот) - проверка связи с ботом", "slap (hit, ударить) `>slap @участник причина`", "Помощь (хелп, help, помощь) - список команд", "info (инфо) - информация о боте", True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="TurboTemuch Bot", icon_url=self.guild.icon_url)
        await channel.send(embed=embed)

    @command(name="info", aliases=["инфо"])
    async def info(self, channel):
        embed = Embed(title="[В СЕТИ]", colour=0x00FF00,
                          timestamp=datetime.utcnow())
        fields = [("Бот TurboTemuch успешно запущен!", "Bot created and coded by TurboTemuch#7375", True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="TurboTemuch1 Bot", icon_url=self.guild.icon_url)
            embed.set_footer(text="Запущен в работу")
            embed.set_thumbnail(url=self.guild.icon_url)
        await channel.send(embed=embed)
            
        await channel.send(file=File("./data/images/APNG-cube.png"))

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)

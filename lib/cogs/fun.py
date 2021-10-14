from random import choice
from typing import Optional

from discord import Member
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
        await ctx.send(f"{ctx.author.name} slapped {member.mention} for {reason}!")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)
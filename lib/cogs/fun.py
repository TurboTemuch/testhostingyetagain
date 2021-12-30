import discord

from os import name
from random import choice
from typing import Optional
from datetime import datetime

from discord import Intents
from discord import Member
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="Связь", aliases=["Бот", "связь", "бот"], description="Проверка связи с ботом.")
    @cooldown(1, 10, BucketType.user)
    async def some_amazing_command(self, ctx):
        """Проверка связи с ботом."""
        
        await ctx.send(f"{choice((':white_check_mark:', 'Всё работает!', ':eyes:', '5 минут, полёт нормальный!', 'Я жив!', 'На месте!', 'Спасибо <@514069435913469962>, что я работаю!'))}")

    @command(name="slap", aliases=["hit","ударить"], description="Ударьте кого-нибудь.")
    @cooldown(1, 5, BucketType.user)
    async def slap_member(self, ctx, member:Member, *, reason: Optional[str] = "просто так"):
        """Ударьте кого-нибудь."""
        
        await ctx.send(f"{ctx.author.name} ударил {member.mention} по причине: {reason}.")

    @command(name="info", aliases=["инфо"], description="Актуальная информация про бота.")
    @cooldown(1, 10, BucketType.user)
    async def info(self, ctx):
        """Актуальная информация про бота."""
        
        embed = Embed(title=f"Версия: `{ctx.bot.VERSION}`", colour=0x00FF00,
                          timestamp=datetime.utcnow())
        fields = [("Bot created and coded by TurboTemuch#7375", "Введите `/help <команда>` для просмотра использования команды", True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name=f"Бот TurboTemuch1 онлайн!")
            embed.set_footer(text="Branch deployed & GitHub repository connected.")
        await ctx.send(embed=embed)
        
    @command(name="update", description="Техническая команда для подготовки к обновлению.")
    @commands.is_owner()
    async def update(self, ctx):
        """Техническая команда для подготовки к обновлению."""
        
        await ctx.bot.change_presence(status=discord.Status.idle, activity=discord.Game("ОБНОВЛЕНИЕ"))
                
    @command(name="stable", description="Техническая команда для завершения обновления.")
    @commands.is_owner()
    async def stable(self, ctx):
        await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(f"/help (version {ctx.bot.VERSION})"))
        
    @command(name="toggle", description="Включение или выключение команд.")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)

        if command is None:
            await ctx.send(":x: Невозможно найти команду с таким именем.")

        elif ctx.command == command:
            embed = discord.Embed(title="ERROR", description="Эту команду невозможно отключить.", color=0xff0000)
            await ctx.send(embed=embed)

        else:
            command.enabled = not command.enabled
            ternary = "включена" if command.enabled else "выключена"
            embed = discord.Embed(title="Toggle", description=f"Команда {command.qualified_name} была успешно {ternary}.", color=0xff00c8)
            await ctx.send(embed=embed)


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)

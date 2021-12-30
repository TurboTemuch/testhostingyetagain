import discord

from os import name
from random import choice
from typing import Optional
from datetime import datetime

from discord import Intents
from discord import Member
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import has_permissions
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

    @command(name="сказать", aliases=["speech", "tts"])
    @commands.is_owner()
    async def tts(self, ctx, *, text:[str]):
        await ctx.send(f"{text}")
        
     
    @command(name="slap", aliases=["hit","ударить"], description="Ударьте кого-нибудь.")
    @cooldown(1, 5, BucketType.user)
    async def slap_member(self, ctx, member:Member, *, reason: Optional[str] = "просто так"):
        """Ударьте кого-нибудь."""
        if member.id == 514069435913469962:
            await ctx.send("Не так быстро, это мой создатель!")
        else:
            await ctx.send(f"{ctx.author.mention} ударил {member.mention} по причине: {reason}.")

    @command(name="basement", aliases=["trap","подвал"], description="Посадите кого-нибудь в подвал.")
    @cooldown(1, 20, BucketType.user)
    async def trap_member(self, ctx, member:Member):
        if member.id == 514069435913469962:
            await ctx.send("Не так быстро, это мой создатель!")
        else:
            await ctx.send(f":house_abandoned: {ctx.author.mention} запер {member.mention} в подвале!")
        
    @command(name="изнасиловать", aliases=["насиловать","rave", "rapish"], description="Изнасилуйте кого-нибудь.")
    @cooldown(1, 20, BucketType.user)
    async def rave_member(self, ctx, member:Member):
        if member.id == 514069435913469962:
            await ctx.send("Не так быстро, это мой создатель!")
        else:
            await ctx.send(f":flushed: {ctx.author.mention} изнасиловал {member.mention}!")    
        
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
        
    @command(name="toggle", aliases=["управление", "вкл", "maintenance"], description="Включение или выключение команд.")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.send(":x: Невозможно найти команду с таким именем.")

        elif ctx.command == command:
            await ctx.send(":x: Невозможно выполнить действие.")

        else:
            command.enabled = not command.enabled
            status = "включена" if command.enabled else "выключена"
            embed = discord.Embed(title="Toggle", description=f"Команда {command.qualified_name} была успешно {status}.", color=ctx.author.color)
            await ctx.send(embed=embed)
            
    @command(name="pancakes", aliases=["add", "блины", "addbal"], description="Быстрая выдача блинов участнику.")
    @commands.has_role("Менеджер конкурсов")
    async def addbalance(self, ctx, member:Member, *, amount:int):
        channel = self.bot.get_channel(779412527062843432)
        await channel.send(f"p!addbal {amount} {member.mention}. {ctx.author.mention}, не забудьте добавить вручную.")


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)

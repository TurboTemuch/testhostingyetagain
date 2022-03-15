import discord
import asyncio

from os import name
from random import choice
from typing import Optional
from datetime import datetime

from discord import Intents
from discord import Member
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import command, has_permissions
from discord.ext.commands import Cog, BucketType, Greedy, CheckFailure
from discord.ext.commands import command, cooldown

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @command(name="Связь", aliases=["Бот", "связь", "бот", "ping", "bot", "Bot"], description="Проверка связи с ботом.")
    @cooldown(1, 10, BucketType.user)
    async def ping_test(self, ctx):
        """Проверка связи с ботом."""
        
        await ctx.send(f"{choice((':white_check_mark:', 'Всё работает!', ':eyes:', '5 минут, полёт нормальный!', 'Я жив!', 'На месте!', 'Спасибо <@514069435913469962>, что я работаю!'))}")

    @command(name="сказать", aliases=["speech", "tts"], description="Скажите что-нибудь от лица бота.")
    @commands.is_owner()
    async def tts(self, ctx, *, text:str):
        """Скажите что-нибудь от лица бота."""
        await ctx.send(f"{text}")
        await ctx.message.delete()
     
    @command(name="ударить", aliases=["hit","slap"], description="Ударьте кого-нибудь.")
    @cooldown(1, 5, BucketType.user)
    async def slap_member(self, ctx, member:Member, *, words: Optional[str] = ""):
        """Ударьте кого-нибудь."""
        if member.id == 514069435913469962:
            await ctx.send("Не так быстро, это мой создатель!")
        elif member.id == 793943860044103721:
            await ctx.send("А вот и нет.")
            await asyncio.sleep(2)
            await ctx.send(f":smiling_imp: TurboTemuch1 ударил {ctx.author.mention}!")
        elif member.id == ctx.author.id:
            await ctx.send(":x: Невозможно выполнить действие.")
        else:
            await ctx.send(f"{ctx.author.mention} ударил {member.mention} со словами: {words}")

    @command(name="подвал", aliases=["trap","basement"], description="Посадите кого-нибудь в подвал.")
    @cooldown(1, 20, BucketType.user)
    async def trap_member(self, ctx, member:Member, *, words: Optional[str] = ""):
        """Посадите кого-нибудь в подвал."""
        if member.id == 514069435913469962:
            await ctx.send("Не так быстро, это мой создатель!")
        elif member.id == 793943860044103721:
            await ctx.send("А вот и нет.")
            await asyncio.sleep(2)
            await ctx.send(f":smiling_imp: TurboTemuch1 запер {ctx.author.mention} в подвале!")
        elif member.id == ctx.author.id:
            await ctx.send(":x: Невозможно выполнить действие.")
        else:
            await ctx.send(f":house_abandoned: {ctx.author.mention} запер {member.mention} в подвале, при этом сказав: {words}")
        
    @command(name="изнасиловать", aliases=["насиловать","rape", "rapish"], description="Изнасилуйте кого-нибудь.")
    @cooldown(1, 20, BucketType.user)
    async def rave_member(self, ctx, member:Member, *, words: Optional[str] = ""):
        """Изнасилуйте кого-нибудь."""
        if member.id == 514069435913469962:
            await ctx.send("Я СЕЙЧАС ТЕБЯ САМ ИЗНАСИЛУЮ А НУ ИДИ СЮДА!")
            await asyncio.sleep(2)
            await ctx.send(f":smiling_imp: TurboTemuch1 изнасиловал {ctx.author.mention}!")
        elif member.id == 793943860044103721:
            await ctx.send("А вот и нет.")
            await asyncio.sleep(2)
            await ctx.send(f":smiling_imp: TurboTemuch1 изнасиловал {ctx.author.mention}!")
        elif member.id == ctx.author.id:
            await ctx.send(":x: Невозможно выполнить действие.")
        else:
            await ctx.send(f":flushed: {ctx.author.mention} изнасиловал {member.mention}, при этом сказав: {words}")    
        
    @command(name="инфо", aliases=["info"], description="Актуальная информация про бота.")
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
        await ctx.message.delete()
                
    @command(name="stable", description="Техническая команда для завершения обновления.")
    @commands.is_owner()
    async def stable(self, ctx):
        """Техническая команда для завершения обновления."""
        await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(f";help (version {ctx.bot.VERSION})"))
        await ctx.message.delete()
        
    @command(name="управление", aliases=["toggle", "вкл", "maintenance"], description="Включение или выключение команд.")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        """Включение или выключение команд."""
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
            
    @command(name="блины", aliases=["add", "pancakes", "addbal"], description="Быстрая выдача блинов участнику.")
    @commands.has_role("Менеджер конкурсов")
    async def addbalance(self, ctx, member:Member, *, amount:int):
        """Быстрая выдача блинов участнику."""
        channel = self.bot.get_channel(779412527062843432)
        await channel.send(f"p!addbal {amount} {member.mention}. {ctx.author.mention}, не забудьте добавить вручную.")
	
    @command(name="кик", aliases=["kick", "выгнать"], description="Исключает пользователя с сервера.")
    @commands.has_permissions(kick_members=True)
    async def kickcmd(self, ctx, targets: Greedy[Member], *, reason: Optional[str]="Причина не указана."):
        """Исключает пользователя с сервера."""
        await self.kick_members(ctx.message, targets, reason)
        await ctx.send("Действие выполнено.")
    
    @kickcmd.error
    async def kick_command_error(self, ctx, exc):
        if isinstance(exc, CheckFailure):
            await ctx.send("Недостаточно прав для выполнения операции.")
        else:
            await ctx.send(":x: Во время выполнения операции произошла неизвестная ошибка.")
    

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))
   # bot.scheduler.add_job(...)

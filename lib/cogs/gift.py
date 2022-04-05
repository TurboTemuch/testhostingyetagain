import random
import discord
import asyncio

from discord import *
from discord import Message, Reaction
from discord.ext.commands import has_permissions
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown

from typing import Optional

def convert(time):
  pos = ["s","m","h","d"]

  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2

  return val * time_dict[unit]

class Gift(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="подарок", aliases=["drop","gift"], description="Команда для сброса подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 5, BucketType.user)
    # async def gift(self, ctx):
    async def gift(self, ctx, *, time: Optional[str] = "30s" ):
        """Команда для сброса подарка."""
#      await ctx.send(":no-entry: Эта команда была отключена.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        timeout = convert(time)
        if timeout == -1:
            await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
            return
        elif timeout == -2:
            await ctx.send(f"Некорректно введено время. Введите целое число.")
        return

        prize = ":gift:"
#         await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")
        embed = discord.Embed(title = "Появился подарок!", description = f"{prize}", color = 0xFFFFFF)

        embed.set_footer(text = f"Открывается через {time}!")

        my_msg = await ctx.send(embed = embed)

        await my_msg.add_reaction("🎁")

        await ctx.message.delete()
      
        await asyncio.sleep(timeout)

        cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
        print(cache_msg.reactions)
      
        users = await cache_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        await ctx.send(f"Подарок забрал {winner.mention}! <@514069435913469962> скоро выдаст приз.")

    @commands.command(name="эпикподарок", aliases=["epicdrop","epicgift"], description="Команда для сброса эпического подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 5, BucketType.user)
    # async def epicgift(self, ctx):
    async def epicgift(self, ctx, *, time: Optional[str] = "45s" ):
        """Команда для сброса эпического подарка."""
#      await ctx.send(":no-entry: Эта команда была отключена.")    
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        timeout = convert(time)
        if timeout == -1:
            await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
            return
        elif timeout == -2:
            await ctx.send(f"Некорректно введено время. Введите целое число.")
            return

        prize = ":gift:"
#         await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")
        embed = discord.Embed(title = "Появился *эпический* подарок!", description = f"{prize}", color = 0x7E13AE)
        embed.set_footer(text = f"Открывается через {time}!")
        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("🎁")
        await ctx.message.delete()
        await asyncio.sleep(timeout)
        cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
        print(cache_msg.reactions)
        users = await cache_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        await ctx.send(f"{winner.mention} забрал *эпический* подарок! <@514069435913469962> скоро выдаст приз.")

    @commands.command(name="мифподарок", aliases=["mythdrop","mythgift"], description="Команда для сброса мифического подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 5, BucketType.user)
    # async def mythgift(self, ctx):
    async def mythgift(self, ctx, *, time: Optional[str] = "60s" ):
        """Команда для сброса мифического подарка."""
#      await ctx.send(":no-entry: Эта команда была отключена.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        timeout = convert(time)
        if timeout == -1:
            await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
            return
        elif timeout == -2:
            await ctx.send(f"Некорректно введено время. Введите целое число.")
            return
  
        prize = ":gift:"
        embed = discord.Embed(title = "Появился **МИФИЧЕСКИЙ** подарок!", description = f"{prize}", color = 0xFF0000)
        embed.set_footer(text = f"Открывается через {time}!")
        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("🎁")
        await ctx.message.delete()  
        await asyncio.sleep(timeout)
        cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
        print(cache_msg.reactions)     
        users = await cache_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        await ctx.send(f"{winner.mention} забрал **МИФИЧЕСКИЙ** подарок! <@514069435913469962> скоро выдаст приз.")

    @commands.command(name="легаподарок", aliases=["legenddrop","legendgift","legendarygift","legendarydrop"], description="Команда для сброса легендарного подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 5, BucketType.user)
    # async def legendarygift(self, ctx):
    async def legendarygift(self, ctx, *, time: Optional[str] = "90s" ):
        """Команда для сброса легендарного подарка."""
#      await ctx.send(":no-entry: Эта команда была отключена.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        timeout = convert(time)
        if timeout == -1:
            await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
            return
        elif timeout == -2:
            await ctx.send(f"Некорректно введено время. Введите целое число.")
            return
 
        prize = ":gift:"
        await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")
        embed = discord.Embed(title = ":crown:Появился **ЛЕГЕНДАРНЫЙ** подарок!:crown: ", description = f"{prize}", color = 0xFFC600)
        embed.set_footer(text = f"Открывается через {time}!")
        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("🎁")
        await ctx.message.delete()
    
        await asyncio.sleep(timeout)

        cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
        print(cache_msg.reactions)     
        users = await cache_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        await ctx.send(f"{winner.mention} забрал :crown: **ЛЕГЕНДАРНЫЙ**:crown:  подарок! <@514069435913469962> скоро выдаст приз.")
      
    @commands.command(name="экзаподарок", aliases=["exoticdrop","exoticgift"], description="Команда для сброса экзотического подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 5, BucketType.user)
    # async def mythgift(self, ctx):
    async def mythgift(self, ctx, *, time: Optional[str] = "60s" ):
        """Команда для сброса экзотического подарка."""
#      await ctx.send(":no-entry: Эта команда была отключена.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        timeout = convert(time)
        if timeout == -1:
            await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
            return
        elif timeout == -2:
            await ctx.send(f"Некорректно введено время. Введите целое число.")
            return
 
        prize = ":gift:"
        embed = discord.Embed(title = "Появился **ЭКЗОТИЧЕСКИЙ** подарок!", description = f"{prize}", color = 0x24FF00)
        embed.set_footer(text = f"Открывается через {time}!")
        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("🎁")
        await ctx.message.delete()
        await asyncio.sleep(timeout)
        cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
        print(cache_msg.reactions)
        users = await cache_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        await ctx.send(f"{winner.mention} забрал **ЭКЗОТИЧЕСКИЙ** подарок! <@514069435913469962> скоро выдаст приз.")
      
    @commands.command(name="incoming", aliases=["dropsoon"], description="Объявление о скором появлении подарков.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 30, BucketType.user)
    async def incoming(self, ctx):
        """Объявление о скором появлении подарков."""
#      await ctx.send(":no-entry: Эта команда была отключена.")
        await ctx.message.delete()
        embed = discord.Embed(title = "Cкоро будет сброшен подарок!", color = 0xFFC600)
        await ctx.send(embed = embed)
      
    @commands.command(name="exoticalincoming", aliases=["exoticaldropsoon"], description="Объявление о скором появлении экзотического подарка.")
    @commands.has_role("Главный Санта")
    @has_permissions(kick_members=True, administrator=True)
    @cooldown(1, 30, BucketType.user)
    async def incoming(self, ctx):
        """Объявление о скором появлении подарков."""
#         await ctx.send(":no-entry: Эта команда была отключена.")
        await ctx.message.delete()
        embed = discord.Embed(title = "Cкоро будет сброшен **ЭКЗОТИЧЕСКИЙ** подарок!", color = 0x24FF00)
        await ctx.send(embed = embed)
      
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("gift")

def setup(bot):
    bot.add_cog(Gift(bot))
   # bot.scheduler.add_job(...)

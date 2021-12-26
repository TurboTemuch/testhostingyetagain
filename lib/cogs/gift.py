import random
import discord
import asyncio

from discord import *
from discord import Message
from discord import Reaction
from discord.ext.commands import has_permissions
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

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

    @commands.command(name="gift", aliases=["drop","подарок"])
    @has_permissions(kick_members=True, administrator=True)
    async def gift(self, ctx, *, imported: Optional[str] = "30s" ):
  
      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      time = convert(imported)
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = ":gift:"

    #   await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")

      embed = discord.Embed(title = "Появился подарок!", description = f"{prize}", color = 0xFFFFFF)

      embed.set_footer(text = f"Открывается через {imported}!")

      my_msg = await ctx.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await ctx.message.delete()
      
      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await ctx.send(f"Подарок забрал {winner.mention}! <@&880169755397464064> скоро выдаст приз.")

    @commands.command(name="epicgift", aliases=["epicdrop","эпикподарок"])
    @has_permissions(kick_members=True, administrator=True)
    async def epicgift(self, ctx, *, imported: Optional[str] = "45s" ):

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      time = convert(imported)
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = ":gift:"

    #   await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")

      embed = discord.Embed(title = "Появился *эпический* подарок!", description = f"{prize}", color = 0x7E13AE)

      embed.set_footer(text = f"Открывается через {imported}!")

      my_msg = await ctx.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await ctx.message.delete()
      
      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await ctx.send(f"{winner.mention} забрал *эпический* подарок! <@&880169755397464064> скоро выдаст приз.")

    @commands.command(name="mythgift", aliases=["mythdrop","мифподарок"])
    @has_permissions(kick_members=True, administrator=True)
    async def mythgift(self, ctx, *, imported: Optional[str] = "60s" ):

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      time = convert(imported)
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = ":gift:"

      embed = discord.Embed(title = "Появился **МИФИЧЕСКИЙ** подарок!", description = f"{prize}", color = 0xFF0000)

      embed.set_footer(text = f"Открывается через {imported}!")

      my_msg = await ctx.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await ctx.message.delete()
      
      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await ctx.send(f"{winner.mention} забрал **МИФИЧЕСКИЙ** подарок! <@&880169755397464064> скоро выдаст приз.")

    @commands.command(name="legendgift", aliases=["legenddrop","легаподарок","legendarygift","legendarydrop"])
    @has_permissions(kick_members=True, administrator=True)
    async def legendarygift(self, ctx, *, imported: Optional[str] = "90s" ):

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      time = convert(imported)
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = ":gift:"

    #   await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")

      embed = discord.Embed(title = ":crown:Появился **ЛЕГЕНДАРНЫЙ** подарок!:crown: ", description = f"{prize}", color = 0xFFC600)

      embed.set_footer(text = f"Открывается через {imported}!")

      my_msg = await ctx.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await ctx.message.delete()
      
      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await ctx.send(f"{winner.mention} забрал :crown: **ЛЕГЕНДАРНЫЙ**:crown:  подарок! <@&880169755397464064> скоро выдаст приз.")
      
    @commands.command(name="incoming", aliases=["dropsoon"])
    @has_permissions(kick_members=True, administrator=True)
    async def incoming(self, ctx):
      await ctx.message.delete()
      embed = discord.Embed(title = "Cкоро будет сброшен подарок!", color = 0xFFC600)
      
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("gift")

def setup(bot):
    bot.add_cog(Gift(bot))
   # bot.scheduler.add_job(...)

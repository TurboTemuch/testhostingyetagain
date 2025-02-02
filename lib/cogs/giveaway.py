import random
import discord
import asyncio

from discord import *
from typing import Optional
from discord import Message
from discord import Reaction
from discord.ext.commands import has_permissions
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown

def convertval(time):
  pos = ["s","m","h","d"]
  
  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

  unit = time[-1]
  
  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2

  return val

def convertdisplay(time):
  pos = ["s","m","h","d"]
  
  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

  unit = time[-1]
  
  display = str()
  
  if unit == "s":
    display = " секунд"
  elif unit == "m":
    display = " минут"
  elif unit == "h":
    display = " часов"
  elif unit == "d":
    display = " дней"
  elif unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2
  
  return display

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

class Giveaway(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="конкурс", aliases=["раздача","gw","giveaway","к"], description="Команда для запуска конкурса.")
    @commands.has_role("Менеджер конкурсов")
    @cooldown(1, 10, BucketType.user)
    async def giveaway(self, ctx):
      """Команда для запуска конкурса."""
      
      await ctx.send("Давайте начнём!")

      questions = ["Где проводим розыгрыш?", "Через сколько опубликовать итоги? (s|m|h|d)", "Какой приз?"]

      answers = []

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      for i in questions:
        await ctx.send(i)

        try:
          msg = await self.bot.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await ctx.send('Вы отвечали слишком долго.')
          return
        else: 
          answers.append(msg.content)

      try:
        c_id = int(answers[0][2:-1])
      except:
        await ctx.send(f"Неправильно упомянут канал. Используйте {ctx.channel.mention}.")
        return

      channel = self.bot.get_channel(c_id)

      value = convertval(answers[1])
      disp = convertdisplay(answers[1])
      time = convert(answers[1])
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = answers[2]

      await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]}!")

      embed = discord.Embed(title = "РОЗЫГРЫШ!", description = f"{prize}", color = ctx.author.color)

      embed.add_field(name = "Проводит:", value = ctx.author.mention)

      embed.set_footer(text = f"Заканчивается через {value}{disp}!")

      my_msg = await channel.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      #print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await channel.send(f"У нас есть победитель! {winner.mention} выиграл: {prize}! *<@&790531068746006548> скоро выдаст его.*")


    @commands.command(name="перерозыгрыш", aliases=["reroll","реролл"], description="Команда для выбора нового победителя конкурса.")
    @commands.has_role("Менеджер конкурсов")
    @cooldown(1, 10, BucketType.user)
    async def reroll(self, ctx, msgid : Optional[int]):
      """Команда для выбора нового победителя конкурса."""
      
      try:
        global new_msg
        new_msg = await ctx.fetch_message(msgid)
      except:
        return await ctx.send("Неправильный ID сообщения с розыгрышем.")
      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await ctx.send(f"Новый победитель: {winner.mention}! (Перерозыгрыш)")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("giveaway")

def setup(bot):
    bot.add_cog(Giveaway(bot))
   # bot.scheduler.add_job(...)

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

    @commands.command(name="giveaway", aliases=["раздача","gw"])
    @has_permissions(kick_members=True, administrator=True)
    async def giveaway(self, ctx):
      await ctx.send("Ответьте на каждый вопрос за 15 секунд")

      questions = ["Где проводим розыгрыш?", "Через сколько опубликовать итоги? (s|m|h|d)", "Какой приз?"]

      answers = []

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      for i in questions:
        await ctx.send(i)

        try:
          msg = await self.bot.wait_for('message', timeout=15.0, check=check)
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

      time = convert(answers[1])
      if time == -1:
        await ctx.send(f"Некорректно введено обозначение. Используйте (s|m|h|d).")
        return
      elif time == -2:
        await ctx.send(f"Некорректно введено время. Введите целое число.")
        return
  
      prize = answers[2]

      await ctx.send(f"Розыгрыш будет проведён в {channel.mention} и итоги будут опубликованы через {answers[1]} секунд!")

      embed = discord.Embed(title = "РОЗЫГРЫШ!", description = f"{prize}", color = ctx.author.color)

      embed.add_field(name = "Проводит:", value = ctx.author.mention)

      embed.set_footer(text = f"Заканчивается через {answers[1]}!")

      my_msg = await channel.send(embed = embed)

      await my_msg.add_reaction("🎉")

      await asyncio.sleep(time)

      cache_msg = discord.utils.get(self.bot.cached_messages, id=my_msg.id) #or client.messages depending on your variable
      print(cache_msg.reactions)
      
      users = await cache_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot.user))

      winner = random.choice(users)

      await channel.send(f"У нас есть победитель! {winner.mention} выиграл: {prize}!")


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def reroll(self, ctx, channel : discord.TextChannel, id_ : int):
      try:
        new_msg = await channel.fetch_message(id_)
      except:
        await ctx.send("Неправильный ID сообщения с розыгрышем.")
      users = await new_msg.reactions[0].users().flatten()
      users.pop(users.index(self.bot))

      winner = random.choice(users)

      await channel.send(f"Новый победитель: {winner.mention}! (Перерозыгрыш)")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("giveaway")

def setup(bot):
    bot.add_cog(Giveaway(bot))
   # bot.scheduler.add_job(...)

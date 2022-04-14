from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions
from random import randint

from ..db import db

class Exp(Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @command(name="префикс")
  @has_permissions(manage_guild=True)
  async def changeprefix(self, ctx, newprefix: str):
    if len(newprefix)>2:
      await ctx.send("Префикс не может быть длиннее 2-х символов!")
    
    else:
      db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", newprefix, ctx.guild.id)
      await ctx.send(f"Префикс изменён на `{newprefix}`.")
  
  @changeprefix.error
  async def changeprefix_error(self, ctx, exc):
    if isinstance(exc, CheckFailure):
      await ctx.send(":lock: Необходимо право управления сервером.")

  async def process_xp(self, message):
    xp, lcl, xplock = db.record("SELECT XP, Level, XPLock FROM exp WHERE UserID = ?", message.author.id)

    if datetime.fromisoformat(xplock) > datetime.utcnow():
      await self.add_xp(message, xp, lvl)
   
  async def add_xp(self, message, xp, lvl):
    xp_to_add = randint(5, 10)
    
    if (new_lvl := int(((xp+xp_add)//42) ** 0.55)) > lvl:
      db.execute("UPDATE exp SET XP = XP + ?, Level = ? WHERE UserID = ?", message.author.id)
    
    db.execute("UPDATE exp SET XP = XP + ? WHERE UserID = ?", xp_add, new_lvl, message.author.id)
    
    if new_lvl > lvl:
      await self.channellvlup.send(f"Поздравляю {message.author.mention} с получением уровня {new_lvl:,}!")
    
  @Cog.listener()
  async def on_message(self, message):
    if not message.author.bot:
      await self.process_xp(message)
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.channellvlup = self.bot.get_channel(964079078665756712)
      self.bot.cogs_ready.ready_up("exp")

def setup(bot):
  bot.add_cog(Exp(bot))

from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions

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

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("exp")

def setup(bot):
  bot.add_cog(Exp(bot))

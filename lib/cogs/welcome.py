from discord.errors import Forbidden
from discord.ext.commands import Cog, command

from ..db import db

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("welcome")
    
    @Cog.listener()
    async def on_member_join(self, member):
        await self.bot.get_channel(821776825616695316).send(f"Добро пожаловать на сервер **{member.guild.name}** {member.mention}! Не забудьте прочитать правила в канале <#742651335262076938>!")
        try:
            await member.send(f"Добро пожаловать на сервер **{member.guild.name}**! Чувствуйте себя, как дома!")
        except Forbidden:
            pass

    @Cog.listener()
    async def on_member_leave(self, member):
        await self.bot.get_channel(821776825616695316).send(f"{member.mention} покинул сервер.")


def setup(bot):
    bot.add_cog(Welcome(bot))

from typing import Optional
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
from discord.ext.menus import MenuPages, ListPageSource
from discord import Embed, embeds
from discord.utils import get


def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

    params = " ".join(params)

    return f"```{cmd_and_aliases} {params}```"


class HelpMenu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx

        super().__init__(data, per_page=3)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = Embed(title="Помощь", description="Добро пожаловать в интерактивную команду помощи!", colour=self.ctx.author.colour)
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} из {len_data:,} команд.")

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, entries):
        fields = []

        for command in entries:
            fields.append((command.description or "Описание отсутствует.", syntax(command)))

        return await self.write_page(menu, fields)

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    async def cmd_help(self, ctx, command):
        embed = Embed(title=f"Помощь с `{command}`", description=syntax(command), colour=ctx.author.colour)
        embed.add_field(name="Описание команды", value=command.help)
        await ctx.send(embed=embed)
    
    @command(name="хелп", aliases=["help","помощь"], description="Интерактивная команда помощи.")
    @cooldown(1, 10, BucketType.user)
    async def show_help(self, ctx, cmd: Optional[str]):
        """Интерактивная команда помощи."""
        if cmd is None:
            menu = MenuPages(source=HelpMenu(ctx, list(self.bot.commands)), delete_message_after=True, timeout=60.0)

            await menu.start(ctx)

        else:
            if (command := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)

            else:
                await ctx.send(":x: Такой команды не существует.")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("help")
    

def setup(bot):
    bot.add_cog(Help(bot))

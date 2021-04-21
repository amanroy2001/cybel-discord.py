"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""

from discord import Intents
from discord.ext import commands

from src.utils import utils

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   case_insensitive=True)

# load cogs
bot.load_extension("src.cogs.autoCommands") # collection of auto triggered command like:> on_member_join
bot.load_extension("src.cogs.adminCommands") # collection of admin commands: like:> Ban, Kick
#bot.load_extension("src.cogs.experimentalCommands") # collection of experimental commands #only in beta version
bot.load_extension("src.cogs.apiBasedCommands") # collection of external api base commands: like:> cat api
bot.load_extension("src.cogs.otherCommands") # collection of other useful commands

if __name__ == '__main__':
    bot.run(utils.TOKEN)

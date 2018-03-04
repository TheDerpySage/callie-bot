#MISS_CALLIE

import discord
from discord.ext import commands
import sys, traceback
import callie_config

desc = '''Callie Bot
Helps text your friends.
While also being cute.
Responds to c$
Written and Developed by TheDerpySage'''

def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
    prefixes = ['c$', 'Callie, ']
    # Check to see if we are outside of a guild. e.g DM's etc.
    if msg.channel is None:
        return ''
    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, msg)

startup_extensions = ['simple', 'text', 'admin']
bot = commands.Bot(command_prefix=get_prefix,description=desc)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Use c$help'))
    #In order to edit her appearence, new parameters can be entered here.
    #fp = open("text_assets/text.png", "rb")
    #await bot.edit_profile(password=None, username="callie-bot", avatar=fp.read())
    if __name__ == '__main__':
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print('Failed to load extension ' + extension, file=sys.stderr)
                traceback.print_exc()
    print('Successfully logged in and booted...!')

bot.run(callie_config.bot_token, reconnect=True)

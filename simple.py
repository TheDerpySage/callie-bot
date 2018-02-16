import discord
from discord.ext import commands
import random

class SimpleCog:
    '''The base stuff'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Greet the bot."""
        await self.bot.say('Hi.')

    @commands.command()
    async def choose(self, ctx, *choices : str):
        """Chooses between multiple choices."""
        random.seed()
        if (len(choices) < 2):
            await self.bot.say("What are you doing? :/")
        else: await self.bot.say(random.choice(choices))

    @commands.command(pass_context=True)
    async def ask(self, ctx, *, message: str = None):
        """Ask a Yes or No Question."""
        if message != None:
            random.seed()
            intensity = random.randint(0,10)
            if intensity == 0:
                await self.bot.say("Absolutely not.")
            elif intensity < 5:
                await self.bot.say("No.")
            elif intensity == 5:
                await self.bot.say("Maybe.")
            elif intensity < 10:
                await self.bot.say("Yes.")
            elif intensity == 10:
                await self.bot.say("Definitely.")
            else: await self.bot.say("Go fuck yourself.")
        else: await self.bot.say("You must include a question, my child.")

def setup(bot):
    bot.add_cog(SimpleCog(bot))

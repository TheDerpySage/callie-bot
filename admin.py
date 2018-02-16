import discord
from discord.ext import commands

class AdminCog:
	'''Server Owner Only stuff'''

	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=True, pass_context=True)
	async def echo(self, ctx, *, message: str):
		if(ctx.message.author == ctx.message.server.owner):
			await self.bot.say(message)
		else : await self.bot.say("Nah.")

	@commands.command(hidden=True, pass_context=True)
	async def reset(self, ctx):
		if(ctx.message.author == ctx.message.server.owner):
			await self.bot.say(":0 Ok! Hold on one second.")
			exit()
		await self.bot.say("No.")

	@commands.command()
	async def credits(self):
		'''Show credits.'''
		await bot.say("`Callie Texting Bot created by TheDerpySage.`")
		await bot.say("`Questions/Concerns? Add via Discord`")
		await bot.say("`@TheDerpySage#2049`")

def setup(bot):
	bot.add_cog(AdminCog(bot))

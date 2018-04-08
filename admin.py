import discord
from discord.ext import commands

class AdminCog:
	'''Server Owner Only stuff'''

	def __init__(self, bot):
		self.bot = bot

	# Self made check since is_owner() doesnt appear to be working and includes server owner
	def is_super(ctx):
		return (ctx.message.author.id == "89033229100683264") or (ctx.message.author == ctx.message.server.owner)

	@commands.command(hidden=True, pass_context=True)
	@commands.check(is_super)
	async def echo(self, ctx, *, message: str):
		await self.bot.say(message)


	@commands.command(hidden=True, pass_context=True)
	@commands.check(is_super)
	async def reset(self, ctx):
		await self.bot.say(":0 Ok! Hold on one second.")
		exit()

	@commands.command()
	async def credits(self):
		'''Show credits.'''
		await bot.say("`Callie Texting Bot created by TheDerpySage.`")
		await bot.say("`Questions/Concerns? Add via Discord`")
		await bot.say("`@TheDerpySage#2049`")

def setup(bot):
	bot.add_cog(AdminCog(bot))

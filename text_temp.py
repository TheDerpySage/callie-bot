import discord
from discord.ext import commands
from email_functions import gmailer
import callie_config

class TextCog:
	'''Texting Functions'''

	def __init__(self, bot):
		self.bot = bot
		self.mailer = gmailer(callie_config.email_sender, callie_config.email_token)

		#This is the base command. Texting uses an SMS gateway email address for sending to phones.
		#Info on this can be found at https://en.wikipedia.org/wiki/SMS_gateway
		#The command can also be repeated with a different name each time ad infinitum

	@commands.command(pass_context=True)
	async def text_SOMEONE(self, ctx, *, message: str):
		"""Text SOMEONE's Phone."""
		await self.bot.send_typing(ctx.message.channel)
		user = ctx.message.author.name
		place = ctx.message.server.name
		self.mailer.send_email("ENTER SMS EMAIL", "Message from Discord", format_text(user, message, place))
		await self.bot.say("Message sent to SOMEONE.")

def format_text(givenUser, givenText, givenPlace):
	return givenUser + ": " + givenText + "\n\nFrom " + givenPlace + " on Discord.\nDo not Reply"

def setup(bot):
	bot.add_cog(TextCog(bot))

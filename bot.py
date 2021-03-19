import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
	print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(822472620913328208)
	await channel.send(f"{member} join!")


@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(822472652832768020)
	await channel.send(f"{member} leave")

bot.run("ODIyMjcwNzU1MjE0NzIxMDc0.YFP1UQ.g2qGDXNcoDs-ilN_F76JlIYZiuo")
	
 

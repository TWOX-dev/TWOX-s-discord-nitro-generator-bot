import discord 
from discord.ext import commands
from time import sleep 
import random
import string
token = '' #your bot's token/сюда нужен токен вашего бота
bot = commands.Bot(command_prefix='Nitro.')
@bot.event
async def on_ready():
	print('<Bot working>')
@bot.command()
async def generate(ctx):
	while True:
		await ctx.send("https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=24)))
		sleep(1) #delay/задержка
bot.run(token)

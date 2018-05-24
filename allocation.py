#Allocation discord bot by YwM#3829


import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

client = discord.Client()


bot = commands.Bot(command_prefix = "#")

bot.remove_command('help')

my_user_id = "312615388854878208"

@bot.event
async def on_ready():
    print("Allocation is now running!")
    print("It's ID is" + (bot.user.id))

@bot.command(pass_context = True)
async def version(ctx):
    await bot.say("This is Allocation pre release.")

@bot.command(pass_context = True)
@commands.has_role("Bot Admin")
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)

@bot.command(pass_context = True)
async def info(ctx):
    await bot.say("Allocation bot pre release, made by me (YwM#3829). Only to be used in my server.")

@bot.command(pass_context = True)
@commands.has_role("Bot Owner")
async def dm(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)

@bot.command(pass_context = True)
@commands.has_role("Bot Owner")
async def shutdown(ctx):
    await bot.logout()

@bot.command(pass_context = True)
@commands.has_role("Bot Owner")
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
    await bot.delete_message(ctx.message)

#@bot.command(pass_context=True)
#async def buy(ctx):
#    await bot.send_message(ctx.message.author, "Please respond with '#sendkey YOUR GIFT CARD CODE'")

#@bot.command(pass_context=True)
#async def sendkey(ctx, *, response):
#    owner = await bot.get_user_info(my_user_id)
#    await bot.send_message(owner, "{} responded: {}".format(ctx.message.author.name, response))






bot.run(TOKEN)

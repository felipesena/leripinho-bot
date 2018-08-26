import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Quita que tá lento!!")


TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)

from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Quita que tá lento!!")


bot.run('NDgyMzM5NDE2NTc3NDA5MDI0.DmIp_Q.Ex35Kr8K5bC2txZ4apbX28hEbO0')

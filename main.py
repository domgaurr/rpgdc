import discord, os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

async def cogs():
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    await cogs()
    print(f'Conectado como "{bot.user.display_name}" em {len(bot.guilds)} servidores.')

@bot.command()
async def syncmds(ctx: commands.Context):
    if ctx.author.id == 1261464275503943753:
        comandos = await bot.tree.sync()
        await ctx.message.delete(delay=3)
        await ctx.send(f'{len(comandos)} comandos sincronizados.', delete_after=3)
    else:
        await ctx.send('Você não tem permissão para usar esse comando.')

bot.run(DISCORD_TOKEN)
import keyboard
import time
import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix='$', intents=disnake.Intents.all())

msg_recipient = "ItzMeFred"


def mcprint(text):
    keyboard.press("T")
    time.sleep(0.001)
    keyboard.release("T")
    time.sleep(0.1)
    keyboard.write(text, delay=0)
    time.sleep(0.5)
    keyboard.press_and_release("enter")


@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work.')
    await bot.change_presence(status=disnake.Status.online)


@bot.slash_command(description='# /rg addmember blurry16 {toadd} INGAME')
async def addmember(ctx, nickname):

    print(f"{ctx.user} executed addmember {nickname} slash command.")
    mcprint(f'/rg addmember blurry16 {nickname}')
    mcprint(f'/msg {msg_recipient} Player {nickname} was added.')
    mcprint(f'/msg {nickname} You are added.')
    await ctx.send(f'Added {nickname}')


@bot.slash_command(description='# /rg removemember blurry16 {toremove} INGAME')
async def removemember(ctx, nickname):

    print(f"{ctx.user} executed removemember {nickname} slash command.")
    mcprint(f'/rg removemember blurry16 {nickname}')
    mcprint(f'/msg {msg_recipient} Player {nickname} was removed.')
    await ctx.send(f'Removed {nickname}')


@bot.slash_command(description='# /rg flag blurry16 {flag_name} {ALLOW/DENY} INGAME')
async def rgflag(ctx, flag, allowdeny):

    print(f"{ctx.user} executed rgflag {flag} {allowdeny} slash command.")
    mcprint(f'/rg flag blurry16 {flag} {allowdeny}')
    mcprint(f'/msg {msg_recipient} flag "{flag}" updated with "{allowdeny}"')
    await ctx.send(f'Changed flag {flag} on {allowdeny}')


@bot.command()
@commands.is_owner()
async def chat(ctx, message):
    print(f"was successfully used $chat {message} command.")
    mcprint(f'# {message}')
    # mcprint(f'/msg {msg_recipient} /chat {message} done')
    await ctx.send(f'Done.')

if __name__ == "__main__":
    bot.run('token')

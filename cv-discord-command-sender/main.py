import keyboard
import time
import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix='$', intents=disnake.Intents.all())

# Admins list.
admins = ['blurry16', 'itsmefred']

# Logging in chat through /msg. (Can be None if you don't want to receive log in chat)
msg_recipient = "ItzMeFred"

# Name of the region where you want to make changes.
region_name = "blurry16"


# Typing function
def mcprint(text):
    keyboard.press("T")
    time.sleep(0.001)
    keyboard.release("T")
    time.sleep(0.1)
    keyboard.write(text, delay=0)
    time.sleep(0.5)
    keyboard.press_and_release("enter")


# Bot start event
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work.')
    await bot.change_presence(status=disnake.Status.online)


# Message logging in terminal
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    author = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{author} said: {user_message} in ({channel}).')


# /addmember command | /rg addmember {region_name} {nickname}
@bot.slash_command(description=f'# /rg addmember {region_name} [nickname] INGAME')
async def addmember(ctx, nickname):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed addmember {nickname} slash command.")
            mcprint(f'/rg addmember {region_name} {nickname}')
            if msg_recipient is not None:
                mcprint(f'/msg {msg_recipient} Player {nickname} was added.')
            await ctx.send(f'Added {nickname}')
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} executed addmember {nickname} slash command. (NO PERMISSIONS)')


# /removemember command | /rg removemember {region_name} {nickname}
@bot.slash_command(description=f'# /rg removemember {region_name} [nickname] INGAME')
async def removemember(ctx, nickname):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed removemember {nickname} slash command.")
            mcprint(f'/rg removemember {region_name} {nickname}')
            if msg_recipient is not None:
                mcprint(f'/msg {msg_recipient} Player {nickname} was removed.')
            await ctx.send(f'Removed {nickname}')
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} executed addmember {nickname} slash command. (NO PERMISSIONS)')


# /flag command | /rg flag {region_name} {flag_name} {flag_option}
@bot.slash_command(description=f'# /rg flag {region_name} [flag_name] [flag_option] INGAME')
async def flag(ctx, flag_name, flag_option):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed rgflag {flag_name} {flag_option} slash command.")
            mcprint(f'/rg flag {region_name} {flag_name} {flag_option}')
            if msg_recipient is not None:
                mcprint(f'/msg {msg_recipient} flag "{flag_name}" updated with "{flag_option}"')
            await ctx.send(f'Changed flag {flag_name} on {flag_option}')
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} executed flag {flag_name} {flag_option} slash command. (NO PERMISSIONS)')


# Help command
@bot.slash_command(description=f'Help for new admins')
async def helpme(ctx):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed /helpme slash command.")
            await ctx.send(f'`List of commands:\n'
                           f'/helpme - this command :p\n'
                           f'/addmember - the same as /rg addmember blurry16 <nickname>. Just put the nickname and the player will be added\n'
                           f'/removemember - the same as /rg removemember blurry16 <nickname>. Just put the nickname and the player will be removed.\n'
                           f'/rgflag - the same as /rg flag blurry16 <flag_name> <flag_option>. <flag_option> can be not only ALLOW/DENY! It is better to check flags in game before executing this command.\n'
                           f'The bot will not be on 24/7. It is online only when blurry16 is afk or sleeping.`', ephemeral=True)
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} used /helpme (NO PERMISSIONS)')

@bot.slash_command(description=f'local chat')
async def chat(ctx, message):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed /chat {message} command")
            mcprint(f'~{message}')
            mcprint(f'/msg blurry16 {user} just used /chat {message} command')
            await ctx.send(f'Successfully sent')
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} used /chat {message} (NO PERMISSIONS)')


# Bot run
if __name__ == "__main__":
    bot.run('token')

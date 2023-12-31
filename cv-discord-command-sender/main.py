import keyboard
import time
import disnake
import json
from mojang import API
from disnake.ext import commands
bot = commands.Bot(command_prefix='$', intents=disnake.Intents.all())
mojang_api = API()
cfg = json.load(open("config.json"))

# Admins list (discord nicknames) can be changed in config.json file
admins = cfg["cfg"]["admins"]

# Logging in chat through /msg. (Can be None if you don't want to receive log in chat)
#                                          IDs can be checked with /getuuid command or with NameMC
msg_recipient = str(mojang_api.get_profile("8eba079e7e9448aa96c06ec4998ab8c3").name)
# msg_recipient = None

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
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Game('on cubeville.org'))


# Message logging in terminal
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    author = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{author} said: {user_message} in ({channel}).')


# Help command
@bot.slash_command(description=f'Help for new admins')
async def helpme(ctx):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed /helpme slash command.")
            await ctx.send(f'`List of commands:\n'
                           f'/helpme - this command :p\n'
                           f'/addmember - the same as /rg addmember blurry16 <nickname>. Just put the nickname and the '
                           f'player will be added\n'
                           f'/removemember - the same as /rg removemember blurry16 <nickname>. Just put the nickname '
                           f'and the player will be removed.\n'
                           f'/rgflag - the same as /rg flag blurry16 <flag_name> <flag_option>. <flag_option> can be '
                           f'not only ALLOW/DENY! It is better to check flags in game before executing this command.\n'
                           f'/chat - local chat using\n'
                           f'/uuid - get uuid of someone with their mojang nickname\n'
                           f'The bot will not be on 24/7. It is online only when blurry16 is afk or sleeping.`',
                           ephemeral=True)
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} used /helpme (NO PERMISSIONS)')


# /addmember command | /rg addmember {region_name} {nickname}
@bot.slash_command(description=f'# /rg addmember {region_name} [nickname] INGAME')
async def addmember(ctx, nickname):
    user = str(ctx.user)
    nickname = str(nickname)
    for admin in admins:
        if user == admin:
            try:
                uuid = str(mojang_api.get_uuid(nickname))
                if uuid is not False:
                    profile = mojang_api.get_profile(uuid)
                    nickname = str(profile.name)
                    print(f"{user} executed addmember {nickname} ({uuid}) slash command.")
                    mcprint(f'/rg addmember {region_name} {nickname}')
                    if msg_recipient is not None:
                        mcprint(f'/msg {msg_recipient} Player {nickname} ({uuid}) was added.')
                    await ctx.send(f'Added {nickname} ({uuid})')
                    break
            except:
                print(f"{user} executed removemember {nickname} slash command (Profile doesn't exits)")
                await ctx.send(f"This profile doesn't exist. ({nickname})")
                break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} executed addmember {nickname} slash command. (NO PERMISSIONS)')


# /removemember command | /rg removemember {region_name} {nickname}
@bot.slash_command(description=f'# /rg removemember {region_name} [nickname] INGAME')
async def removemember(ctx, nickname):
    user = str(ctx.user)
    nickname = str(nickname)
    for admin in admins:
        if user == admin:
            try:
                uuid = str(mojang_api.get_uuid(nickname))
                if uuid is not False:
                    profile = mojang_api.get_profile(uuid)
                    nickname = str(profile.name)
                    print(f"{user} executed removemember {nickname} ({uuid}) slash command.")
                    mcprint(f'/rg removemember {region_name} {nickname}')
                    if msg_recipient is not None:
                        mcprint(f'/msg {msg_recipient} Player {nickname} ({uuid}) was removed.')
                    await ctx.send(f'Removed {nickname} ({uuid})')
                    break
            except:
                print(f"{user} executed removemember {nickname} slash command (Profile doesn't exits)")
                await ctx.send(f"This profile doesn't exist. ({nickname})")
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


# Local chat command
@bot.slash_command(description=f'local chat')
async def chat(ctx, message):
    user = str(ctx.user)
    for admin in admins:
        if user == admin:
            print(f"{user} executed /chat {message} command")
            mcprint(f'~{message}')
            await ctx.send(f'Successfully sent')
            break
    else:
        await ctx.send(f'No permissions.', ephemeral=True)
        print(f'{user} used /chat {message} (NO PERMISSIONS)')


# Get UUID of a Mojang account command
@bot.slash_command(description=f'Mojang account UUID getter')
async def getuuid(ctx, nickname):
    user = str(ctx.user)

    print(f'{user} executed /getuuid {nickname} command')
    try:
        uuid = str(mojang_api.get_uuid(nickname))
        if uuid is not False:
            profile = mojang_api.get_profile(uuid)
            nickname = str(profile.name)
            await ctx.send(f'{nickname}\'s UUID is - {uuid}')
            print(f'{user} got UUID of {nickname} ({uuid})')

    except:
        await ctx.send(f'This profile does not exist. ({nickname})')
        print(f'{user} did not get UUID of {nickname}. THIS PROFILE DOES NOT EXIST')


# Bot run
if __name__ == "__main__":
    bot.run(str(cfg["cfg"]["token"]))

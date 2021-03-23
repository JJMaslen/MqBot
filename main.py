# Main Imports

# Discord Imports
import discord
import discord.ext
from discord.ext import commands

# Local File Imports
import genericBot
import RaidScheduler

bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Mq Bot is online!")
    print("Name: Mq Bot")
    print("TD: {}".format(client.user.id))

@client.command()
async def test(ctx):
    await ctx.send("Hello World")

@client.command()
async def beans(ctx):
    await ctx.send("Beans")

@client.command()
async def addRole(ctx, role):
    user = ctx.message.author
    roleList = user.guild.roles

    newRole = genericBot.searchRoles(roleList, role)
    try:
        if newRole is not None:
            if newRole not in user.roles:
                await user.add_roles(newRole)
                await ctx.send("Enjoy your new role!")
        else:
            await ctx.send("That isn't a role! Current roles you can have are: Fractal")
    except:
        await ctx.send("That role isn't available")

@client.command()
async def removeRole(ctx, role):
    user = ctx.message.author
    roleList = user.guild.roles

    newRole = genericBot.searchRoles(roleList, role)

    try:
        if newRole is not None:
            await user.remove_roles(newRole)
            await ctx.send("Role has been removed")

        else:
            await ctx.send("That isn't a role! Current roles you can have are: Fractal")
    except:
        await ctx.send("That role isn't available")

@client.command()
async def scheduleRaid(ctx, time, *args):
    inputTime = time
    user = ctx.message.author

    await ctx.send("{} is hosting a Raid at: {}. They will be doing the following wings: {}. To sign up for this raid, please react to this message with a :thumbsup:. To remove yourself from the signup, remove the :thumbsup: from this message.".format(user, inputTime, args))

@client.event
async def on_reaction_add(reaction, user):
    print("added")
    #do things to add person to the list

@client.event
async def on_raw_reaction_remove(reaction):
    print("removed")
    #do things to remove person from the list

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if "quaggan" in message.content.lower():
        await message.channel.send("Quaggan")

    await client.process_commands(message)

file = open("token.txt", "r")
token = str(file.read())
file.close()
client.run(token)
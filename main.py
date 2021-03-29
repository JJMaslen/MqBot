# Main Imports

# Discord Imports
import discord
import discord.ext
from discord.ext import commands

# Local File Imports
import genericBot
import RaidScheduler

# for testing only remove at end
import dbMethods

bot_prefix = "!"
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Mq Bot is online!")
    print("Name: Mq Bot")
    print("TD: {}".format(bot.user.id))

@bot.command()
async def test(ctx):
    await ctx.send("Hello World")

@bot.command()
async def beans(ctx):
    await ctx.send("Beans")

@bot.command()
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

@bot.command()
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

@bot.command()
@commands.has_any_role('Leader','Officer')
async def scheduleRaid(ctx, time, *args):
    inputTime = time
    user = ctx.message.author.name
    raidMessageID = ctx.message.id
    print(raidMessageID)

    if not RaidScheduler.checkRaid(user):
        RaidScheduler.createRaidEvent(user, time, str(args))
        message = await ctx.send("{} is hosting a Raid at: {} (GMT). They will be playing the following wings: {}. To sign up for this raid, please react to this message with a :thumbsup:. To remove yourself from the signup, remove the :thumbsup: from this message.".format(user, inputTime, args))
        await message.add_reaction("👍")
    else:
        await ctx.send("You already have a raid scheduled, use !checkRaid to see it")

@bot.command()
@commands.has_any_role('Leader','Officer')
async def checkRaid(ctx):
    user = ctx.message.author

@bot.command()
@commands.has_any_role('Leader', 'Officer')
async def cancelRaid(ctx):
    user = ctx.message.author.name

    if RaidScheduler.checkRaid(user):
        RaidScheduler.deleteRaidEvent(user)
        await ctx.send("Your scheduled raid has been cancelled")
    else:
        await ctx.send("You do not currently have a raid scheduled to cancel")

@bot.event
async def on_raw_reaction_add(payload):

    # Pull information from payload
    user = payload.member
    userName = user.name
    print(userName)
    messageID = payload.message_id
    channelID = payload.channel_id

    # Cancels if user is bot
    if user.bot:
        return

    # Get message from id's, get channel -> get message
    channel = await bot.fetch_channel(channelID)
    message = await channel.fetch_message(messageID)

    # THIS NEEDS TO BE FIXED, CURRENTLY GETS THE BOT AS THE HOST
    host = message.author.name
    # Raid Schedule reaction check
    if message.author.bot:
        if "is hosting a Raid at" in message.content:
            print(host + " AND " + userName)
            RaidScheduler.addToList(host, userName)

    # Test things
    print("An Emote has been added")
    #print(user)
    #print(await reaction.users().flatten())

@bot.event
async def on_raw_reaction_remove(payload):
    # Pull information from payload
    userID = payload.user_id
    user = bot.get_user(userID)
    messageID = payload.message_id
    channelID = payload.channel_id

    # Cancels if user is bot
    if user.bot:
        return

    # Get message from id's, get channel -> get message
    channel = await bot.fetch_channel(channelID)
    message = await channel.fetch_message(messageID)

    host = message.author.name

    #test things
    print("An Emote has been removed")

file = open("token.txt", "r")
token = str(file.read())
file.close()
bot.run(token)
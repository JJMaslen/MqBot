# Main Imports

# Discord Imports
import discord.ext
from discord.ext import commands

# Local File Imports
import genericBot
import RaidScheduler

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
    await ctx.send("Hello World", delete_after=10)
    
@bot.command()
async def quaggan(ctx):
    await ctx.send("Quaggan")

@bot.command()
async def voteThing(ctx):
    message = await ctx.send("Vote Thing")
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")
    await message.add_reaction("4️⃣")
    await message.add_reaction("5️⃣")
    await message.add_reaction("6️⃣")
    await message.add_reaction("7️⃣")
    await message.add_reaction("8️⃣")

@bot.command()
async def voteThingy(ctx):
    message = await ctx.send("Vote Thing")
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")
    await message.add_reaction("4️⃣")
    await message.add_reaction("5️⃣")
    await message.add_reaction("6️⃣")
    await message.add_reaction("7️⃣")
    await message.add_reaction("8️⃣")

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
            await ctx.send("That isn't a role! Current roles you can have are: Fractal, Raid, Strike, PvP, WvW")
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
            await ctx.send("That isn't a role! Current roles you can have are: Fractal, Raid, Strike, PvP, WvW")
    except:
        await ctx.send("That role isn't available")

@bot.command()
@commands.has_any_role('Leader','Officer')
async def scheduleRaid(ctx, time, *args):
    inputTime = time
    user = ctx.message.author.display_name
    userID = ctx.message.author.id

    if not RaidScheduler.checkRaid(user):
        RaidScheduler.createRaidEvent(userID, time, str(args))
        RaidScheduler.cr
        channel = bot.get_channel(922494025687269417)
        message = await channel.send("{} is hosting a Raid at: {} (GMT). They will be playing the following wings: {}. To sign up for this raid, please react to this message with a :thumbsup:. To remove yourself from the signup, remove the :thumbsup: from this message. <@&821039188634763324>".format(user, inputTime, args))
        await message.add_reaction("👍")
    else:
        await ctx.send("You already have a raid scheduled, use !checkRaid to see it")

@bot.command()
@commands.has_any_role('Leader','Officer')
async def viewRaid(ctx):
    user = ctx.message.author.display_name.split()[0]
    raidPlayers = RaidScheduler.postRaid(user)

    await ctx.send(raidPlayers)

@bot.command()
@commands.has_any_role('Leader', 'Officer')
async def cancelRaid(ctx):
    user = ctx.message.author.display_name.split()[0]

    if RaidScheduler.checkRaid(user):
        RaidScheduler.deleteRaidEvent(user)
        await ctx.send("Your scheduled raid has been cancelled")
    else:
        await ctx.send("You do not currently have a raid scheduled to cancel")

@bot.event
async def on_raw_reaction_add(payload):

    # Pull information from payload
    user = payload.member
    userDisplayName = user.display_name

    messageID = payload.message_id
    channelID = payload.channel_id

    # Cancels if user is bot
    if user.bot:
        return

    # Get message from id's, get channel -> get message
    channel = await bot.fetch_channel(channelID)
    message = await channel.fetch_message(messageID)

    # Raid Schedule reaction check
    if message.author.bot:
        if "is hosting a Raid at" in message.content:
            host = message.content.split()[0]
            RaidScheduler.addToList(host, userDisplayName)

    # Test things
    #print("An Emote has been added")

@bot.event
async def on_raw_reaction_remove(payload):
    # Pull information from payload
    userID = payload.user_id
    guild = bot.get_guild(751842622888476722)

    user = guild.get_member(userID)
    userDisplayName = user.display_name

    messageID = payload.message_id
    channelID = payload.channel_id

    # Cancels if user is bot
    if user.bot:
        return

    # Get message from id's, get channel -> get message
    channel = await bot.fetch_channel(channelID)
    message = await channel.fetch_message(messageID)

    if message.author.bot:
        if "is hosting a Raid at" in message.content:
            host = message.content.split()[0]
            RaidScheduler.addToList(host, userDisplayName)

    #test things
    #print("An Emote has been removed")

@bot.command()
async def playThatFunkyMusic(ctx):
    channel = ctx.message.author.voice.channel
    voc = await channel.connect()
    voc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('mambo.mp3')))
    voc.source.volume = 0.05

@bot.command()
async def disconnect(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

file = open("token.txt", "r")
token = str(file.read())
file.close()
bot.run(token)
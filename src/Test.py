import discord
import asyncio

client = discord.Client()

#PERSONAL BOT TOKEN FOR DISCORD BOT
token = "MTkzNTA2ODAwMjc0ODk4OTQ1.CkdJtA.5LSCdpqpfFndHTbVAFgYI4BZfMg"

#----------------------------------------------------------------------------------------------------------------------#
@client.event

# RUNS WHEN EXECUTION IS COMPLETE

async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------")

    # a pandamonia detection function
    member_list = []

    for member in list(client.get_all_members()):
        member_list.append(str(member))

    for m in member_list:
        if 'Panda' in m:
            print('Pandamonia Detected')

    # who's online and is the object iterable? (i.e not a generator object)
    print(sorted(member_list))
    print(type(member_list))


@client.event
async def on_message(message):
    #TRYING TO FIGURE OUT HOW TO MAKE "MEMBERS" OR "USER" OBJECTS FOR SPECIFIC PEOPLE
    max = discord.Member()

    #SPECIFIC ID FOR CHANNELS "148334555856764929" = BAINBOW BIX BIEGE CHANNEL
    myChannel = client.get_channel("148334555856764929")
    myServer = client.get_server("148334555856764928")

    '''
    LISTENS TO TEXT CHANNELS FOR COMMANDS
    '''
    if message.content.startswith("!max"):
        await client.send_message(message.channel, max.display_name)
    #JOINS CHANNEL "YOU" ARE CURRENTLY IN
    if message.content.startswith("!join"):
        await client.send_message(message.channel, "Channel identified: {}".format(myChannel))
        await client.join_voice_channel(myChannel)
    if message.content.startswith("!logout"):
        await client.logout()
    if message.content.startswith("!channel"):
        await client.send_message(message.channel, myServer.default_channel)

    '''
    RUN SOUND FILE [TESTING]
    '''
    #if message.content.startswith("!peasant_test"):
    #    voice = await client.join_voice_channel(myChannel)
    #    player = voice.create_ffmpeg_player("E:\Programs\Coding\Eclipse\workspace\Discord Bots\src\sound files\Human - Yes_mi_lord.mp3")
    #    player.start()



client.run(token)



# This example requires the 'message_content' intent.

import discord
from discord import guild, MemberCacheFlags

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)

from discord.ext import commands

intents = discord.Intents.all()
intents.reactions = True
intents.members = True
intents.guilds = True
intents.message_content = True
# client = commands.Bot(member_cache_flags=MemberCacheFlags.all(), command_prefix='bday ', intents=intents)
# client = commands.Bot(command_prefix='', intents=intents)
# client = discord.Client(member_cache_flags=MemberCacheFlags.all(), intents=intents)
# intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="!", sort_commands=False)
# client = discord.Client(intents=intents)

# intents = discord.Intents.none()
# intents.reactions = True
# intents.members = True
# intents.guilds = True
# client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # members = client.get_all_members()
    # print('members', list(members))
    # for member in list(members):
    #     print('members.name', member.name)
    #
    # channels = client.get_all_channels()
    # print('channels', list(channels))
    # for channel in list(channels):
    #     print('channel.name', channel.name)
    #
    # async for guild in client.fetch_guilds(limit=150):
    #     print(guild.name)

    # try:
    #     guild = await client.fetch_guild(1106403018389336095)
    #     print('guild', guild)
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     server = client.get_guild(1106403018389336095)
    #     print('server', server)
    # except Exception as e:
    #     print(e)

    try:
        guild = (client.get_guild(1106403018389336095) or await client.fetch_guild(1106403018389336095))
        print('guild', guild)
        await guild.send("This is a test.")
    except Exception as e:
        print(e)

    try:
        channel = (client.get_channel(1151068722841272351) or await client.fetch_channel(1151068722841272351))
        print('channel', channel)
        await channel.send("This is a test.")
    except Exception as e:
        print(e)

    # try:
    #     user = client.get_user(1106403018389336095)
    #     print('user', user)
    #     await user.send('👀')
    # except Exception as e:
    #     print(e)


# @client.event
# async def on_connect():
#     print(f'We have on_connect in as {client.user}')

    # members = client.get_all_members()
    # print('members', list(members))
    # for member in list(members):
    #     print('members.name', member.name)
    #
    # channels = client.get_all_channels()
    # print('channels', list(channels))
    # for channel in list(channels):
    #     print('channel.name', channel.name)


# @client.command()
# # Command works in DMs only
# @commands.dm_only()
# async def new_thread(ctx):
#     guild = client.get_guild(1106403018389336095)
#     print('guild', guild)
#     await ctx.send(guild.id)
#     # await guild.create_text_channel(channel_name)


client.run('MTE1MTA1OTUzMDY0MjM3MDU5MA.Go3Ihu.4ANMEpfKdhxtX_UI1ndDWdZ0uLLvulZ14PU1iQ')

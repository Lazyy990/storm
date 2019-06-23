import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Being epic'))
    print('I\'m ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server. :(')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=1):
    await ctx.message.channel.purge(limit=amount+1)
    await ctx.message.channel.send("Message deleted")

@client.command()
async def clearchannel(ctx):
    await ctx.channel.purge()

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='ping', value='Tells your ping.', inline=False)
    embed.add_field(name='kick @Member', value='Kicks someone.', inline=False)
    embed.add_field(name='ban @Member', value='Bans someone.', inline=False)
    embed.add_field(name='unban @Member', value='Unbans someone.', inline=False)
    embed.add_field(name='clear *amount*', value='Clears the amount of messages in that channel.', inline=False)
    embed.add_field(name='clearchannel', value='Clears the channel.', inline=False)

    await ctx.send(author, embed=embed)
    

client.run(str(os.environ.get('NTU3NjA4ODk2MzQwOTUxMDYw.XQ7mFQ.qIaivXIP3gTJY9fmFjs7hxJfhys')))

import discord  #you would have to download the discord library 

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print("we have loged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$"):
    await message.channel.send("hello !!!")


client.run("")

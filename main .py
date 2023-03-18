import discord  #you would have to download the discord library 

client = discord.Client(intents=discord.Intents.default())

# when the bot is online 
@client.event
async def on_ready():
#it prints out this statement 
  print("we have loged in as {0.user}".format(client))

# when someone sends a message to the bots dms or includes it in a message on a server containing $
@client.event
#checks so that the bot dosent continue to respond to itself
async def on_message(message):
  if message.author == client.user:
    return
  
#it sends "Hello!!"
  if message.content.startswith("$"):
    await message.channel.send("hello !!!")


client.run("") #put your bot token here 

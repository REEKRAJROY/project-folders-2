from discord.ext import commands
import aysncio

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("ready")
    while True:
        print("cleared")
        await asyncio.sleep(10)
        with open("spam_detect.txt","r+") as file:
            file.truncate(0)

@client.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt","r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1

        file.writelines(f"{str(message.author.id)}\n")
        if counter > 10:
            await message.guild.ban(message.author,reason="spam")
            await asyncio.sleep(1)
            await message.guild.unban(message.author)
            print("uh oh")

client.run("ODI4Njk2Nzc4MjgyMzY5MDQ1.YGtWBA.2NYB7kI_d232JcsfBH94M0VTvYI")
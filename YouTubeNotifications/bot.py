import os
import disnake


from disnake.ext import commands


intents = disnake.Intents.all() 
bot = commands.Bot(command_prefix=".", intents=intents, test_guilds=[...])

#id test_guilds id server




num = 0
for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        num += 1
        print(f">> Module [{filename[:-3]}] Loaded")
print(f"\n>> Cogs loaded: {num}\n")


        


bot.run("YOU TOKEN")
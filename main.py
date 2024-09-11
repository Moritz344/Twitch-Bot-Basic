from twitchio.ext import commands
from dotenv import load_dotenv
import os

load_dotenv("secret.env")
Twitch_token = os.getenv("TOKEN")
channel = "pennti"


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=Twitch_token,prefix="!",initial_channels=[channel])

    async def event_ready(self):
        print(f"Bot ist bereit und verbunden mit {self.nick} im Kanal {channel}")
        self.count = 0
    @commands.command(name="hello")
    async def Hello(self,ctx):
        await ctx.send(f"Hallo, {ctx.author.name}")


    @commands.command(name="count")
    async def Count(self,ctx):
        self.count += 1
        await ctx.send(f"{self.count} {ctx.author.name}")
    @commands.command(name="github")
    async def github(self,ctx):
        await ctx.send(f"PunchTrees Mein Github: https://github.com/Moritz344 {ctx.author.name}")
    @commands.command(name="heute")
    async def today(self,ctx):
        await ctx.send(f"Heute ehhhm ka {ctx.author.name}")
    @commands.command(name="lurk")
    async def lurker(self,ctx):
        await ctx.send(f"{ctx.author.name} ist im Lurk! MrDestructoid")
    @commands.command(name="Texteditor")
    async def editor(self,ctx):
        await ctx.send("Ich benutze LunarVim: https://www.lunarvim.org/ GlitchCat")

    async def event_message(self,message):
        if message.author is not None:
            await self.handle_commands(message)
        try:        
            print(f"{message.author.name}: {message.content}")
        except AttributeError:
            print("User hat einen Befehl geschrieben!")

if __name__ == "__main__":
        bot = Bot()
        bot.run()

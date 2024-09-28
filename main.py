from twitchio.ext import commands
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv("secret.env")
Twitch_token = os.getenv("TOKEN")
channel = "pennti"

class Bot(commands.Bot):
    def __init__(self):
        with open("data.json","r",encoding="utf-8") as file:
            bad_words_data = json.load(file)
            self.bad_words = bad_words_data["BAD_WORDS"]

        super().__init__(token=Twitch_token,prefix="!",initial_channels=[channel])
        self.date_now = datetime.now().strftime("%H:%M")



    async def event_ready(self):
        print(f"Bot ist bereit und verbunden mit {self.nick} im Kanal {channel}")
        self.count = 0
    @commands.command(name="hallo")
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

    @commands.command(name="editor")
    async def editor(self,ctx):
        await ctx.send("Ich benutze Nvim: https://neovim.io/ GlitchCat")
    
    @commands.command(name="theme")
    async def colorscheme(self,ctx):
        await ctx.send("Ich benutze zurzeit oft: gruber-darker")

  

    async def event_message(self,message):
        try:
            if message.author is not None:
                await self.handle_commands(message)
            elif message.author is None:
                return

        except Exception as e:
            print(e)

        if message.author.name == self.nick:
            return

        for bad in self.bad_words:
            if bad in message.content.lower():
                await message.channel.send(f"NotLikeThis Bitte verwende keine schlechten Wörter! {message.author.name}")
                return


        try:        
            print(f"[{self.date_now}] {message.author.name}: {message.content}")

        except AttributeError:
            print("User hat einen Befehl geschrieben!")
        except Exception as e:
            print(e)
    

if __name__ == "__main__":
    bot = Bot()
    bot.run()

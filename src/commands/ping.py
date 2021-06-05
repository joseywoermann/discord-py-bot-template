from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['p'])
    async def ping(self, ctx):

        await ctx.reply(f"Pong! {round(self.client.latency * 1000)} milliseconds!")

def setup(client):
    client.add_cog(Ping(client))

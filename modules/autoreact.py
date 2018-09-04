# RIEN A EDIT DANS CE CODE

import discord
# from __main__ import settings
import asyncio

class reactions:
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, message):
        channel = message.channel
        if message.author.id != self.bot.user.id:
            try:
                if message.content == "lmao":
                    L = "\U0001f1f1"
                    M = "\U0001f1f2"
                    A = "\U0001f1e6"
                    O = "\U0001f1f4"
                    joy = "\U0001f602"
                    cjoy = "\U0001f639"

                    async for x in self.bot.logs_from(channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, L)
                        await self.bot.add_reaction(x, M)
                        await self.bot.add_reaction(x, A)
                        await self.bot.add_reaction(x, O)
                        await self.bot.add_reaction(x, joy)
                        await self.bot.add_reaction(x, cjoy)
                if message.content == "rekt":
                    R = "\U0001f1f7"
                    E = "\U0001f1ea"
                    K = "\U0001f1f0"
                    T = "\U0001f1f9"
                    FINGERMIDDLE = "\U0001f595"
                    FINGERCROSS = "\U0001f91e"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, R)
                        await self.bot.add_reaction(x, E)
                        await self.bot.add_reaction(x, K)
                        await self.bot.add_reaction(x, T)
                        await self.bot.add_reaction(x, FINGERMIDDLE)
                        await self.bot.add_reaction(x, FINGERCROSS)

                if message.content == "fucker":
                    MIDDLEFINGER = "\U0001f595"
                    F = "\U0001f1eb"
                    U = "\U0001f1fa"
                    C = "\U0001f1e8"
                    K = "\U0001f1f0"
                    Y = "\U0001f1fe"
                    O = "\U0001f1f4"
                    E = "\U0001f1ea"
                    R = "\U0001f1f7"
                    point = "\U0001f446"
                    FIST = "\U0001f91c"
                    bump = "\U0001f91b"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                        await self.bot.add_reaction(x, MIDDLEFINGER)
                        await self.bot.add_reaction(x, F)
                        await self.bot.add_reaction(x, U)
                        await self.bot.add_reaction(x, C)
                        await self.bot.add_reaction(x, K)
                        await self.bot.add_reaction(x, E)
                        await self.bot.add_reaction(x, R)
                        await self.bot.add_reaction(x, bump)

                if message.content == "nsfw":
                    DUCKPICS = "\U0001F346"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                            await self.bot.add_reaction(x, DUCKPICS)

                if message.content == "mdr":
                    M = "\U0001f1f2"
                    D = "\U0001F1E9"
                    R = "\U0001f1f7"
                    joy = "\U0001f602"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                           await self.bot.add_reaction(x, M)
                           await self.bot.add_reaction(x, D)
                           await self.bot.add_reaction(x, R)
                           await self.bot.add_reaction(x, joy)
                
                if message.content == "nudes":
                    PEACH = "\U0001F351"
                    N = "\U0001F1F3"
                    U = "\U0001f1fa"
                    D = "\U0001F1E9"
                    E = "\U0001f1ea"
                    S = "\U0001F1F8"
                    DUCKPICS = "\U0001F346"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                           await self.bot.add_reaction(x, PEACH)
                           await self.bot.add_reaction(x, N)
                           await self.bot.add_reaction(x, U)
                           await self.bot.add_reaction(x, D)
                           await self.bot.add_reaction(x, E)
                           await self.bot.add_reaction(x, S)
                           await self.bot.add_reaction(x, DUCKPICS)
                
                if message.content == "gay":
                    G = "\U0001F1EC"
                    A = "\U0001f1e6"
                    Y = "\U0001f1fe"
                    E = "\U0001f1ea"
                    RAINBOW = "\U0001F308"

                    async for x in self.bot.logs_from(message.channel, before=message.timestamp, limit=1):
                           await self.bot.add_reaction(x, G)
                           await self.bot.add_reaction(x, A)
                           await self.bot.add_reaction(x, Y)
                           await self.bot.add_reaction(x, RAINBOW)


            except discord.Forbidden:
                pass

def setup(bot):
    n = reactions(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)
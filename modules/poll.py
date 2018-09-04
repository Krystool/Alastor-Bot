import discord
from discord.ext import commands

from time import strftime
import random



class Sondage:
    """"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str, a=None, c=None):
        if c is None:
            c = random.randint(0, 16777215)
        if len(options) <= 1:
            await self.bot.say('Vous avez besoin de plus d\'une option pour faire un sondage!')
            return
        if len(options) > 10:
            await self.bot.say('Vous ne pouvez pas faire un sondage pour plus de 10 choses!')
            return

        if len(options) == 2 and options[0] == 'oui' and options[1] == 'non':
            reactions = ['👍', '👎']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), colour=c)
        react_message = await self.bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await self.bot.add_reaction(react_message, reaction)
        if a is not None:
            author = a.name + '#' + a.discriminator
            embed.set_author(
                name=author, 
                icon_url=a.avatar_url
            )
        embed.set_footer(
            text='Propulsé par VooDoo | dear-voodoo.com | Poll ID: {}'.format(react_message.id),
            icon_url="http://dear-voodoo.com/coding/discord-bot/Only-V-little.png"
        )
        await self.bot.edit_message(react_message, embed=embed)

    @commands.command(pass_context=True)
    async def tally(self, ctx, id):
        poll_message = await self.bot.get_message(ctx.message.channel, id)
        if not poll_message.embeds:
            return
        embed = poll_message.embeds[0]
        if poll_message.author != ctx.message.server.me:
            return
        if not embed['footer']['text'].startswith('Poll ID:'):
            return
        unformatted_options = [x.strip() for x in embed['description'].split('\n')]
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [ctx.message.server.me.id]  # add the bot's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await self.bot.get_reaction_users(reaction)
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)

        output = 'Results of the poll for "{}":\n'.format(embed['title']) + \
                 '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await self.bot.say(output)


def setup(bot):
    bot.add_cog(Sondage(bot))
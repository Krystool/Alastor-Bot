# -*- coding: utf8 -*-
import codecs
from datetime import datetime
import os

from discord.utils import find


class Log:
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def output(a, sysout=True):
        """ Output the string 'a' """
        a = a.encode('utf-8', 'replace').decode('utf-8', 'ignore')
        p = a.encode('utf-8', 'replace').decode('ascii', 'ignore')
        today = datetime.today()
        filename = "log-{0}-{1}-{2}.log".format(str(today.month), str(today.day), str(today.year))
        prefix = "[{0}:{1}:{2}]: ".format(str(today.hour), str(today.minute), str(today.second))
        if sysout:
            print(prefix + p)
        if not os.path.exists('./logs'):
            os.makedirs('./logs')
        with codecs.open('./logs/' + filename, 'a', encoding='utf8') as f:
            # OH YEAH AND DON'T USE NOTEPAD... USE A BETTER ONE LIKE NOTEPAD++
            f.write(prefix + a + "\n")
            f.close()

    # All them event overrides....
    async def on_message(self, msg):
        if msg.content.startswith(self.bot.command_prefix):
            cmdused = msg.author.name + " a essayé d'utiliser la commande: `" + msg.content + "`"
            self.output(cmdused)
            modlog = find(lambda c: c.name == "modlog", msg.server.channels)
            if modlog == None:
                return
            await self.bot.send_message(modlog, cmdused)

    async def on_member_join(self, member):
        self.output(member.name + " a rejoint le serveur en " + member.server.name, False)

    async def on_member_remove(self, member):
        self.output(member.name + " a quitté le serveur en " + member.server.name, False)

    async def on_message_delete(self, msg):
        if msg.author == self.bot.user:
            return
        result = '{0} a supprimé le message suivant: \n`{1}`'.format(msg.author.name, msg.content)
        modlog = find(lambda c: c.name == "modlog", msg.server.channels)
        if modlog is None:
            return
        await self.bot.send_message(modlog, result)

    async def on_message_edit(self, before, after):
        if before.author == self.bot.user:
            return
        if before.content == after.content:
            return
        msg = '{0} édite le message suivant: \nAvant: `{1}`\n Après: `{2}`'.format(
            before.author.name,
            before.content,
            after.content
        )
        modlog = find(lambda c: c.name == "modlog", before.server.channels)
        if modlog is None:
            return
        await self.bot.send_message(modlog, msg)

def setup(bot):
    """Setup Log.py"""
    bot.add_cog(Log(bot))

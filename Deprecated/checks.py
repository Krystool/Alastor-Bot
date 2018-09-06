import configparser
config = configparser.ConfigParser()
config.read("config.ini")
OWNER = config["GENERAL"]["owner"]
def checkdev(message):
    """Checks if the developer used the command. AKA ME"""
    return message.author.id == OWNER

def checkignorelist(message, ignore):
    """If on the list, return true; if not, return false."""
    for serverid in ignore["servers"]:
        if serverid == message.channel.server.id:
            return True

    for channelid in ignore["channels"]:
        if channelid == message.channel.id:
            return True

    for userid in ignore["users"]:
        if userid == message.author.id:
            return True

    return False

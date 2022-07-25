import bot


async def get_guilds_id():
    guilds = []
    servers = bot.bot.guilds
    for guild in servers:
        guilds.append(guild.id)
    return guilds
import discord
from discord.utils import get
import random
import re

from youtube_dl import YoutubeDL

import cfg
from bot.db import core_db

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


db = core_db.db()


async def play_core(ctx, arg, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    id_g = db.guild_exist(guild_id=ctx.guild.id)[0]
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(int(db.channel_afk_get(id_g=id_g)))
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(arg, download=False)

                URL = info['formats'][0]['url']

                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg, source=URL, **FFMPEG_OPTIONS))
            else:
                vc = await voice_channel.connect()
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(arg, download=False)

                URL = info['formats'][0]['url']

                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg, source=URL, **FFMPEG_OPTIONS))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def voice_command_new(message, bot, path, amount, numb="", pic=""):  # for handler
    voice = get(bot.voice_clients, guild=message.guild)
    if message.channel.id == cfg.music_channel:
        voice_channel = message.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if int(amount) > 1 and numb == "":
            numb = random.randint(1, int(amount))
        if voice_channel is not None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(path) + str(numb) + ".mp3"))
                if pic != "":
                    await message.channel.send(str(pic))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(path) + str(numb) + ".mp3"))
                if pic != "":
                    await message.channel.send(str(pic))
        else:
            await message.channel.send('Не вижу тебя в нужном канале.')
    else:
        await message.channel.send('Пиши в "cmd".')


async def music_handler(message, bot):
    channel = message.channel
    if channel == message.channel:  # данный if исключает повторное вызывание команд бота
        if re.search('!''(?P<name>[a-z0-9.-]+)', message.content) is not None:
            command = re.findall('!''(?P<name>[a-z0-9.-]+)', message.content)
            if re.search('!''[a-z0-9.-]+'' ''(?P<number>\d+)', message.content) is not None:
                number = re.findall('!''[a-z0-9.-]+'' ''(?P<number>\d+)', message.content)
                numb = number[0]
            else:
                numb = ""
            if hasattr(channel, 'guild'):
                id_g = db.guild_exist(guild_id=channel.guild.id)[0]
                if re.search('[\']' + str(command[0]) + '[\']', db.voice_commands_get(id_g=id_g)) is not None:
                    path = db.voice_path_get(id_g=id_g, command=command[0])
                    pic = db.voice_pic_get(id_g=id_g, command=command[0])
                    amount = db.voice_amount_get(id_g=id_g, command=command[0])
                    await voice_command_new(message=message, bot=bot, path=path, amount=amount, numb=numb, pic=pic)
                else:
                    pass

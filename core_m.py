import discord
from discord.utils import get
import random
import re

# import rhinoscriptsyntax as rs
import json

from youtube_dl import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

import cfg


async def play_core(ctx, arg, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
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


# async def voice_command_old(ctx, bot, path, numb="", pic=""):  # for cmd
#     voice = get(bot.voice_clients, guild=ctx.guild)
#     if ctx.channel.id == cfg.music_channel:
#         voice_channel = ctx.author.voice.channel
#         afk_channel = bot.get_channel(cfg.afk_channel)
#         if voice_channel is not None and voice_channel != afk_channel:
#             if voice and voice.is_connected():
#                 voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
#                                                   source=str(path) + str(numb) + ".mp3"))
#                 if pic != "":
#                     await ctx.send(str(pic))
#             else:
#                 vc = await voice_channel.connect()
#                 vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
#                                                source=str(path) + str(numb) + ".mp3"))
#                 if pic != "":
#                     await ctx.send(str(pic))
#         else:
#             await ctx.send('Не вижу тебя в нужном канале.')
#     else:
#         await ctx.send('Пиши в "cmd".')


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
            with open(r'/root/bots/discord/rut/voice_info.json', 'r') as f:
                datastore = json.load(f)
            check = (datastore["music"]["music_commands"]["music_commands_name"])
            if re.search('[\']' + str(command[0]) + '[\']', str(check)) is not None:

                path = (datastore["music"]["music_commands"][str(command[0])]["path"])
                pic = (datastore["music"]["music_commands"][str(command[0])]["pic"])
                amount = (datastore["music"]["music_commands"][str(command[0])]["amount"])

                await voice_command_new(message=message, bot=bot, path=path, amount=amount, numb=numb, pic=pic)
            else:
                pass

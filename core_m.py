import discord
from discord.utils import get
import random

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


async def voice_command(ctx, bot, path, numb="", pic=""):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel is not None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(path) + str(numb) + ".mp3"))
                if pic != "":
                    await ctx.send(str(pic))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(path) + str(numb) + ".mp3"))
                if pic != "":
                    await ctx.send(str(pic))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')
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


async def kak_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.kakayu) + ".mp3"))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.kakayu) + ".mp3"))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def gmv_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.gmv) + ".mp3"))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.gmv) + ".mp3"))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def uwu_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.uwu) + ".mp3"))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.uwu) + ".mp3"))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def blyat_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.blyat) + ".mp3"))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.blyat) + ".mp3"))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def deb_core(ctx, a, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if 14 > int(a) > 0:
            if voice_channel != None and voice_channel != afk_channel:
                if voice and voice.is_connected():
                    voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                      source=str(cfg.debil) + str(a) + ".mp3"))
                else:
                    vc = await voice_channel.connect()
                    vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                   source=str(cfg.debil) + str(a) + ".mp3"))
            else:
                await ctx.send('Не вижу тебя в нужном канале.')
        else:
            await ctx.send('Такого дебила нет.')
    else:
        await ctx.send('Пиши в "cmd".')


async def debil_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        a = (random.randint(1, 13))
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.debil) + str(a) + ".mp3"))
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.debil) + str(a) + ".mp3"))
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')


async def cow_core(ctx, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.channel.id == cfg.music_channel:
        voice_channel = ctx.author.voice.channel
        afk_channel = bot.get_channel(cfg.afk_channel)
        if voice_channel != None and voice_channel != afk_channel:
            if voice and voice.is_connected():
                voice.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                                  source=str(cfg.cow) + ".mp3"))
                await ctx.send('https://i.gifer.com/Za9e.gif')
            else:
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable=cfg.ffmpeg,
                                               source=str(cfg.cow) + ".mp3"))
                await ctx.send('https://i.gifer.com/Za9e.gif')
        else:
            await ctx.send('Не вижу тебя в нужном канале.')
    else:
        await ctx.send('Пиши в "cmd".')
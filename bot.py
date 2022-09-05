import asyncio
import random
import os
import re
from datetime import date, datetime, timedelta
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
from os import system
from discord.ext import commands
import schedule
import time

import answers
import cfg
import core
import core_m

import core_db
db = core_db.db()

bot: Bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Tom is ready')
    servers = bot.guilds
    for guild in servers:
        print(str(guild.name) + ' ' + str(guild.id))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(db.bot_status_get())))


@bot.event  # реакция бота на вход нового пользователя на сервер
async def on_member_join(member):
    print(str(member) + ' join the guild')
    guild_id_db = db.guild_exist(guild_id=member.guild.id)
    channel = bot.get_channel(int(db.channel_general_get(id_g=guild_id_db)))
    await channel.send(str(member.mention) + ", добро пожаловать на наш сервер :smiley_cat:")


@bot.event  # реакция бота на выход пользователя с сервера
async def on_member_remove(member):
    print(str(member) + ' left the guild')
    guild_id_db = db.guild_exist(guild_id=member.guild.id)
    channel = bot.get_channel(int(db.channel_general_get(id_g=guild_id_db)))
    await channel.send('**' + str(member) + '**' + " ушел от нас, пока-пока :ghost:")


@bot.event
async def on_guild_join(guild):
    db.guild_add(guild_id=guild.id, name=guild.name, status='1')


@bot.event
async def on_guild_remove(guild):
    db.guild_remove(guild_id=guild.id, status='0')


@bot.command()  # вывод дат с подсчетом
async def dates(ctx):
    dimatmp = core.datecheck(2000, 8, 28)
    makstmp = core.datecheck(2000, 10, 13)
    katyatmp = core.datecheck(2000, 2, 11)
    sertmp = core.datecheck(2000, 6, 30)
    bortmp = core.datecheck(2000, 9, 7)
    nytmp = core.datecheck(2000, 1, 1)
    summertmp = core.datecheck(2000, 6, 1)
    # ruttmp = core.datecheck(2000, 9, 26)

    await ctx.send("```Даты: \n\n" +
                   "До дня рождения Димы " + str(dimatmp) + ". (28 августа)\n" +
                   "До дня рождения Макса " + str(makstmp) + ". (13 октября)\n" +
                   "До дня рождения Кати " + str(katyatmp) + ". (11 февраля)\n" +
                   "До дня рождения Серёги " + str(sertmp) + ". (30 июня)\n" +
                   "До дня рождения Бори " + str(bortmp) + ". (7 сентября)\n\n" +
                   "До нового года осталось " + str(nytmp) + ".\n" +
                   "До лета осталось " + str(summertmp) + ".\n```"
                   )


@bot.command()  # изменение статуса Тома
@commands.has_permissions(administrator=True)
async def status(ctx, s: int, text: str):
    if s == 1:
        db.bot_status_mod(text=text)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
    if s == 2:
        db.bot_status_mod(text=text)
        await bot.change_presence(activity=discord.Game(name=text))
    if s == 3:
        db.bot_status_mod(text=text)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))


@status.error  # ошибка изменения статуса
async def status_error(ctx, error):
    await ctx.send(random.choice(answers.error_list))
    print(error)


@bot.remove_command('help')  # удаление стандартной команды help
@bot.command()  # команда help
async def help(ctx):
    await ctx.send(answers.help)


@bot.command()  # команда helpm (help music)
async def helpm(ctx):
    await ctx.send(answers.helpm)


@bot.command()  # ссылка на дискорд
async def dis(ctx):
    await ctx.send("https://discord.gg/mkXgVXq")


@bot.command()
async def web(ctx):
    embed = discord.Embed(
        title="Tom Web",
        url="http://37.230.114.133:8000/",
        color=discord.Colour.dark_gold()
    )
    await ctx.send(embed=embed)


@bot.command()  # команда рандомного числа в диапазоне
async def flip(ctx, a: int, b: int):
    if a > 0 and b < 10001:
        await ctx.send(random.randint(a, b))
    else:
        await ctx.send("Что-то не так, друг, максимальный диапазон от 1 до 10000")


@bot.command()  # команда для спама
@commands.has_role("Admin")
async def spam(ctx, a: int):
    if a < 21:
        for a in range(a):
            await ctx.send(a + 1)
    else:
        await ctx.send("Нельзя!")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)


@spam.error  # ошибка команды спама
async def spam_error(ctx, error):
    await ctx.send(random.choice(answers.error_list))
    print(error)


@bot.command(pass_context=True)  # чистка чата
@commands.has_permissions(administrator=True)
async def clear(ctx, n: int):
    await ctx.channel.purge(limit=n + 1)
    await ctx.send("Я съел `" + str(n) + "` сообщений")
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)


@clear.error  # ошибка команды читстки чата
async def clear_error(ctx, error):
    await ctx.send(random.choice(answers.error_list))
    print(error)


@bot.command()  # команда day ДОДЕЛАТЬ!!!!!!!!!!!!!!
async def day(ctx):
    await ctx.send("Команда находится в разработке")


@bot.command(pass_context=True, aliases=['j'])  # join
@commands.has_permissions(administrator=True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    await channel.connect()


@join.error  # ошибка join music
async def join_error(ctx, error):
    await ctx.send(random.choice(answers.error_list))
    print(error)


@bot.command(pass_context=True, aliases=['l'])  # leave
@commands.has_permissions(administrator=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Откуда ?")


@leave.error  # ошибка leave music
async def leave_error(ctx, error):
    await ctx.send(random.choice(answers.error_list))
    print(error)


# @bot.command(pass_context=True, aliases=['korova'])  # Корова
# @commands.has_role("Admin")
# async def cow(ctx):
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.cow, pic=cfg.cow_pic)
#
#
# @cow.error  # ошибка Коровы
# async def cow_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True)  # Дебил(Гоблин) по номеру
# @commands.has_role("Admin")
# async def deb(ctx, numb=""):
#     if numb == "":
#         numb = str((random.randint(1, 13)))
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.debil, numb=numb)
#
#
# @deb.error  # ошибка Дебила по номеру
# async def deb_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True, aliases=['bl'])  # Blyat Маша
# @commands.has_role("Admin")
# async def blyat(ctx):
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.blyat)
#
#
# @blyat.error  # ошибка Blyat
# async def blyat_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True)  # UwU
# @commands.has_role("Admin")
# async def uwu(ctx):
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.uwu)
#
#
# @uwu.error  # ошибка uwu
# async def uwu_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True)  # Good morning Vietnam
# @commands.has_role("Admin")
# async def gmv(ctx):
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.gmv)
#
#
# @gmv.error  # ошибка gmv
# async def gmv_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True)  # Какаю в туалете
# @commands.has_role("Admin")
# async def kak(ctx):
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.kak)
#
#
# @kak.error  # ошибка какаю в туалете
# async def kak_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)
#
#
# @bot.command(pass_context=True)  # Какаю в туалете
# @commands.has_role("Admin")
# async def bam(ctx, numb=""):
#     if numb == "":
#         numb = str((random.randint(1, 2)))
#     await core_m.voice_command(ctx=ctx, bot=bot, path=cfg.bam, numb=numb)
#
#
# @bam.error  # ошибка какаю в туалете
# async def bam_error(ctx, error):
#     await ctx.send(random.choice(answers.error_music))
#     print(error)


@bot.command()
async def play(ctx, arg):
    await core_m.play_core(ctx=ctx, arg=arg, bot=bot)


@play.error  # ошибка play
async def play_error(ctx, error):
    await ctx.send(random.choice(answers.error_music))
    print(error)


@bot.command(pass_context=True)  # установить канал для сообщений от имени бота
async def channel(ctx, a: int):
    global m_channel
    if ctx.author.id == cfg.owner_id:
        m_channel = a
        await ctx.send('Принял')
    else:
        await ctx.send('У тебя нет прав')


@bot.command(pass_context=True)  # отправка сообщений от имени бота
async def m(ctx, message):
    if ctx.author.id == cfg.owner_id:
        channel_m = bot.get_channel(int(m_channel))
        await channel_m.send(message)
    else:
        await ctx.send('У тебя нет прав')


@bot.command(pass_context=True)  # одобрить последнюю ссылку
@commands.has_permissions(administrator=True)
async def yes(ctx):
    with open(r'/root/bots/discord/rut/url_tmp.txt', 'r') as f:
        url = f.readlines()
        f.close()
    with open(r'/root/bots/discord/rut/url_white.txt', 'a') as f:
        f.write(str(url[0]))
        f.close()
    await ctx.send(':white_medium_square: Ссылка в вайт листе')


@bot.command(pass_context=True)  # занести в блэк лист последнюю ссылку
@commands.has_permissions(administrator=True)
async def no(ctx):
    with open(r'/root/bots/discord/rut/url_tmp.txt', 'r') as f:
        url = f.readlines()
        f.close()
    with open(r'/root/bots/discord/rut/url_black.txt', 'a') as f:
        f.write(str(url[0]))
        f.close()
    await ctx.send(':black_medium_square: Ссылка в блэк листе')


# @bot.command(pass_context=True)
# @commands.has_role("Admin")
# async def maf(ctx):
#     await ctx.send('Играем в мафию\nСколько людей ?')
#     count = await bot.wait_for('message')
#     n = int(count.content)
#     if n > 3:
#         players = [0] * n
#         for i in range(n):
#             await ctx.send(str(i + 1) + '-й игрок:')
#             players[i] = await bot.wait_for('message')
#         mafia = (random.randint(0, n - 1))
#         police = (random.randint(0, n - 1))
#         while mafia == police:
#             police = (random.randint(0, n - 1))
#         maf = players[mafia]
#         pol = players[police]
#         members = []
#         # for i in range(n):
#         #     if players[i].content != maf.content and players[i].content != pol.content:
#         #         members.append(players[i].content)
#         maf_pm = bot.get_user(int(maf.content))
#         pol_pm = bot.get_user(int(pol.content))
#         # for i in range(n - 2):
#         #     members_pm = bot.get_user(int(members[i]))
#         #     await members_pm.send('Ты мирный житель :farmer:')
#         await maf_pm.send('Ты мафия :spy:')
#         await pol_pm.send('Ты комиссар :cop:')
#         alive = n
#         dead = 0
#         mafia_is_dead = False
#         for i in range(n):
#             tmp = bot.get_user(int(players[i].content))
#             await ctx.send('Твоя минута, ' + str(tmp.mention))
#             await asyncio.sleep(5)
#             await ctx.send('Адыхай!')
#         await ctx.send('Наступила ночь... Выключаем микрофоны, господа и дамы.')
#         while alive > 2:
#             await maf_pm.send('0 - никого не убивать.')
#             for i in range(alive):
#                 tmp1 = bot.get_user(int(players[i].content))
#                 await maf_pm.send(str(i + 1) + ' - ' + str(tmp1))
#             await maf_pm.send('Кого убьешь этой ночью ?')
#             kill = await bot.wait_for('message')
#             for i in range(alive):
#                 tmp2 = bot.get_user(int(players[i].content))
#                 await pol_pm.send(str(i + 1) + ' - ' + str(tmp2))
#             await pol_pm.send('Кого будешь проверять ?')
#             confirm = await bot.wait_for('message')
#             if int(players[int(confirm.content) - 1].content) != int(maf.content):
#                 await pol_pm.send('Он не мафия')
#             elif int(players[int(confirm.content) - 1].content) == int(maf.content):
#                 await pol_pm.send('Он мафия!')
#             await asyncio.sleep(5)
#             await ctx.send('Доброе утро, жители Дискорда!')
#             await asyncio.sleep(5)
#             if kill.content == 0:
#                 await ctx.send('На сегодняшний день все живы!')
#             else:
#                 await ctx.send('Этой ночью убили' + str(players[int(kill.content) - 1].content))
#                 alive = alive - 1
#                 del players[int(kill.content) - 1]
#                 kill = None
#             for i in range(alive):
#                 tmp = bot.get_user(int(players[i].content))
#                 await ctx.send('Твоя минута, ' + str(tmp.mention))
#                 await asyncio.sleep(5)
#                 await ctx.send('Адыхай!')
#             await asyncio.sleep(5)
#             await ctx.send('Время голосовать (итог голосования пишет 1 человек)!\n0 - никого не кикаем')
#             for i in range(alive):
#                 await ctx.send(str(i + 1) + ' - ' + str(players[i].content))
#             kick = await bot.wait_for('message')
#             if kick.content == 0:
#                 pass
#             elif int(players[int(kick.content) - 1].content) == int(maf.content):
#                 await ctx.send('Мирные жители победили.')
#                 break
#             else:
#                 await ctx.send(str(players[int(kick.content) - 1].content) + ' больше нет с нами.')
#                 alive = alive - 1
#                 del players[int(kick.content) - 1]
#                 kick = None
#     else:
#         await ctx.send('Для игры в мафию нужно минимум 4 человека')


# @bot.command()
# async def check(ctx, arg):
#     if isinstance(ctx.channel, discord.channel.DMChannel):
#         await ctx.send(arg)

########################################################################## Event
# async def ny():
#     await bot.wait_until_ready()
#     ny = date(2022, 2, 11)
#     channel = bot.get_channel(cfg.private_channel)
#     while not bot.is_closed():
#         checkpoint = 0
#         if ny == date.today():
#             await channel.send(answers.katya)
#             checkpoint = checkpoint + 1
#         await asyncio.sleep(120)
#         if checkpoint == 1:
#             break


# async def reminder():
#     await bot.wait_until_ready()
#     ff = date(2000, 1, 13)
#     channel = bot.get_channel(cfg.private_channel)
#     while not bot.is_closed():
#         if ff == date.today():
#             await channel.send("Ёмжик")
#             if ff.year % 4 == 0:
#                 ff = ff + timedelta(days=366)
#             else:
#                 ff = ff + timedelta(days=365)
#             print(ff)
#         await asyncio.sleep(120)


@bot.event  # разговоры с Томом
async def on_message(message):
    await core.message_handler(message=message)
    await core_m.music_handler(message=message, bot=bot)
    # await core.danger_handler(message=message)
    await bot.process_commands(message)  # исключает повторное вызывание команд бота


# bot.loop.create_task(ny())
# bot.loop.create_task(reminder())
bot.run(cfg.token_id)
